# Can create object tracker using histogram detection!


# Copyright 2021 Scott Horton
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# Adapted from various Luxonis DepthAI sample applications.
#
# Includes Blazepose tracking with DepthAI
# From https://github.com/geaxgx/depthai_blazepose
# Credit:  geaxgx

import threading
import sys
import time
import pathlib

import numpy as np
import cv2

import depthai as dai

import rclpy
from rclpy.node import Node
from cv_bridge import CvBridge
from sensor_msgs.msg import Image

from object_detection_msgs.msg import ObjectDescArray
from object_detection_msgs.msg import ObjectDesc
from robot_head_interfaces.msg import TrackStatus, SaveImage, DetectedPose, EnablePoseDetection, HeadImu

from pose_interp import analyze_pose

import mediapipe_utils as mpu
from BlazeposeDepthai import BlazeposeDepthai, to_planar

# Fix - not working since updating to latest Depthai - 
human_pose = False
human_pose_process = True

ball_detect = True

show_depth = False
cam_out_use_preview = True
use_tracker = True
print_detections = False
show_det_info = True
show_edge_image = True
syncNN = False
use_tyolo_v4 = False
use_imu = True
pub_detection_frame = True

frame_rate = 15.0

labelMap_MNetSSD = [
    "background", "aeroplane", "bicycle", "bird", "boat", "bottle", "bus", "car", "cat", "chair", "cow",
    "diningtable", "dog", "horse", "motorbike", "person", "pottedplant", "sheep", "sofa", "train", "tvmonitor"]

labelMap_TYolo4 = [
    "person",         "bicycle",    "car",           "motorbike",     "aeroplane",   "bus",           "train",
    "truck",          "boat",       "traffic light", "fire hydrant",  "stop sign",   "parking meter", "bench",
    "bird",           "cat",        "dog",           "horse",         "sheep",       "cow",           "elephant",
    "bear",           "zebra",      "giraffe",       "backpack",      "umbrella",    "handbag",       "tie",
    "suitcase",       "frisbee",    "skis",          "snowboard",     "sports ball", "kite",          "baseball bat",
    "baseball glove", "skateboard", "surfboard",     "tennis racket", "bottle",      "wine glass",    "cup",
    "fork",           "knife",      "spoon",         "bowl",          "banana",      "apple",         "sandwich",
    "orange",         "broccoli",   "carrot",        "hot dog",       "pizza",       "donut",         "cake",
    "chair",          "sofa",       "pottedplant",   "bed",           "diningtable", "toilet",        "tvmonitor",
    "laptop",         "mouse",      "remote",        "keyboard",      "cell phone",  "microwave",     "oven",
    "toaster",        "sink",       "refrigerator",  "book",          "clock",       "vase",          "scissors",
    "teddy bear",     "hair drier", "toothbrush"]

def get_model_path(model_name):
    return str(pathlib.Path(__file__).parent.absolute()) + '/models/' + model_name

# Helper for displaying overlay text on an image
def OverlayTextOnBox(img, x, y, xpad, ypad, text, bg_color, alpha, font, font_scale, text_color, text_thick):
    #Fix
    try:
        w = 0
        hmax = 0
        for t in text:
            if t == None:
                continue
            (tw, th) = cv2.getTextSize(t, font, fontScale=font_scale, thickness=text_thick)[0]
            w = max(w, 2*xpad + tw)
            hmax = max(hmax, th)
        h = (ypad + hmax)*len(text) + ypad

        sub = img[y:y+h, x:x+w]
        bg = np.zeros_like(sub)
        bg[:] = bg_color
        blend = cv2.addWeighted(sub, 1.0 - alpha, bg, alpha, 0)

        yy = 0
        for t in text:
            if t == None:
                continue
            cv2.putText(blend, t, (xpad, yy + ypad + hmax), font, font_scale, text_color, text_thick, cv2.LINE_AA)
            yy += ypad + hmax
        img[y:y+h, x:x+w] = blend
        return x, y, x + w, y + h
    except:
        return None

class RobotVision(Node):
    def __init__(self):
        super().__init__('robot_vision')

        self.image = None
        # Publisher for camera color image
        self.imagePub = self.create_publisher(Image, '/color/image', 10)
        self.bridge = CvBridge()

        # Publisher for camera color image
        self.detectionImagePub = self.create_publisher(Image, '/detection_image', 10)

        # Publisher for list of detected objects
        self.objectPublisher = self.create_publisher(
            ObjectDescArray,
            '/head/detected_objects',
            10)

        # Publisher for list of target objects
        self.targetPublisher = self.create_publisher(
            ObjectDescArray,
            '/head/detected_targets',
            10)

        # Publisher for detected human pose
        self.posePublisher = self.create_publisher(
            DetectedPose,
            '/head/detected_pose',
             1)

        # Publisher for head rotation
        self.headImuPublisher = self.create_publisher(
            HeadImu,
            '/head/imu',
             1)

        # Subscribe to topic for enabling/disabling pose detection
        self.subPoseDetectEnable = self.create_subscription(
            EnablePoseDetection,
            '/head/enable_pose_detect',
            self.pose_detect_enable_callback,
            1)

        # Subscribe to topic specifying which object is being
        # tracked by the Tracker node
        self.subTracked = self.create_subscription(
            TrackStatus,
            '/head/tracked',
            self.tracked_callback,
            1)

        # Subscribe to topic for triggering an image save
        self.subSaveImage = self.create_subscription(
            SaveImage,
            '/head/save_image',
            self.save_image_callback,
            1)

        self.setWinPos = True

        self.tracked = None
        self.save_image = None

        pose_last = None

        blaze_pose = BlazeposeDepthai(multi_detection = True)

        with dai.Device(self.create_pipeline()) as device:
            self.get_logger().debug("Starting pipeline...")
            device.startPipeline()

            previewQueueCAM = device.getOutputQueue(name="cam_out", maxSize=1, blocking=False)

            detectionNNQueue = device.getOutputQueue(name="detections", maxSize=1, blocking=False)
            xoutBoundingBoxDepthMapping = device.getOutputQueue(name="boundingBoxDepthMapping", maxSize=2, blocking=False)
            if show_depth:
                depthQueue = device.getOutputQueue(name="depth", maxSize=1, blocking=False)
            if human_pose:
                q_pd_out = device.getOutputQueue(name="pd_out", maxSize=1, blocking=False)
                q_lm_out = device.getOutputQueue(name="lm_out", maxSize=2, blocking=False)
                q_lm_in = device.getInputQueue(name="lm_in")
            if ball_detect:
                edgeImgQueue = device.getOutputQueue(name="edge_image", maxSize=4, blocking=False)
                ballDetectionNNQueue = device.getOutputQueue(name="ball_detections", maxSize=4, blocking=False)
            if use_imu:
                imuQueue = device.getOutputQueue(name="imu", maxSize=2, blocking=False)

            frame = None
            edgeFrame = None
            inEdgeFrame = None
            inBallDetectNN = None
            imuData = None
            tracklets = []

            startTime = time.monotonic()
            counter = 0
            fps = 0
            white = (255, 255, 255)
            color = (0, 255, 0)
            rect_color = (128, 128, 128)
            font = cv2.FONT_HERSHEY_SIMPLEX
            font_scale = 0.5
            disp_cnt = 0

            flipCAM = False

            last_region = None
            last_poses = None

            save_cnt = 0

            while True:

                rclpy.spin_once(self, timeout_sec=0.001)

                try:
                    inPreviewCAM = previewQueueCAM.tryGet()

#                    inPreviewCAM = previewQueueCAM.tryGet()
                    inNN = detectionNNQueue.tryGet()

                    if ball_detect:
                        if show_edge_image:
                            inEdgeFrame = edgeImgQueue.tryGet()
                        if inEdgeFrame:
                            inBallDetectNN = ballDetectionNNQueue.tryGet()

                    if use_imu:
                        imuData = imuQueue.tryGet()

                except:
                    self.get_logger().error("Failed to read from queue.")
                    continue

                if inNN != None:
                    tracklets = inNN.tracklets

                    # For debug
                    if print_detections:
                        for tracklet in tracklets:
                            self.get_logger().debug("------------")
                            self.get_logger().debug("id: %d" % tracklet.id)
                            self.get_logger().debug("label: %s" % self.labelMap[tracklet.label])
                            roi = tracklet.roi.denormalize(640, 360)
                            self.get_logger().debug("roi: %d,%d -- %d,%d" % (int(roi.topLeft().x), int(roi.topLeft().y), int(roi.bottomRight().x), int(roi.bottomRight().y)))
                            self.get_logger().debug("spacial: %f, %f, %f" % (tracklet.spatialCoordinates.x, tracklet.spatialCoordinates.y, tracklet.spatialCoordinates.z))

                            #if tracklet.srcImgDetection.label != "NoneType":
                            #    label = labelMap[tracklet.srcImgDetection.label]
                            #else:
                            #    label = "none"
                            self.get_logger().debug("label %s, conf %f, xmin %f, ymin %f, xmax %f, ymax %f" % (self.labelMap[int(tracklet.srcImgDetection.label)], \
                                tracklet.srcImgDetection.confidence, tracklet.srcImgDetection.xmin, tracklet.srcImgDetection.ymin, \
                                tracklet.srcImgDetection.xmax, tracklet.srcImgDetection.ymax))
                            self.get_logger().debug(tracklet.status)

                    # Publish detections
                    self.publish_detections(self.labelMap, tracklets, "oakd_center_camera", self.objectPublisher)

                if inPreviewCAM == None:
                    continue

                if ball_detect and inEdgeFrame:
                    try:
                        edgeFrame = inEdgeFrame.getCvFrame()
                    except:
                        self.get_logger().error("Failed to read edge frame")
                    else:
                        if show_edge_image:
                            height = edgeFrame.shape[0]
                            width = edgeFrame.shape[1]

                            if inBallDetectNN != None:
                                # Display detections
                                for tracklet in inBallDetectNN.tracklets:
                                    # Denormalize bounding box
                                    x1 = int(tracklet.srcImgDetection.xmin*width)
                                    x2 = int(tracklet.srcImgDetection.xmax*width)
                                    y1 = int(tracklet.srcImgDetection.ymin*height)
                                    y2 = int(tracklet.srcImgDetection.ymax*height)

                                    conf = "{:.2f}".format(tracklet.srcImgDetection.confidence*100)
                                    self.get_logger().debug(f"id: {tracklet.id}, Conf {conf}, bb {x1},{y1} - {x2},{y2}, xyz {int(tracklet.spatialCoordinates.x)}, {int(tracklet.spatialCoordinates.y)}, {int(tracklet.spatialCoordinates.z)}")

                                    cv2.putText(edgeFrame, f"{int(tracklet.id)}", (x2 + 10, y1 + 0), cv2.FONT_HERSHEY_TRIPLEX, 0.50, 255)
                                    cv2.putText(edgeFrame, "{:.2f}".format(tracklet.srcImgDetection.confidence*100), (x2 + 10, y1 + 20), cv2.FONT_HERSHEY_TRIPLEX, 0.25, 255)
                                    cv2.putText(edgeFrame, f"X: {int(tracklet.spatialCoordinates.x)}", (x2 + 10, y1 + 35), cv2.FONT_HERSHEY_TRIPLEX, 0.25, 255)
                                    cv2.putText(edgeFrame, f"Y: {int(tracklet.spatialCoordinates.y)}", (x2 + 10, y1 + 50), cv2.FONT_HERSHEY_TRIPLEX, 0.25, 255)
                                    cv2.putText(edgeFrame, f"Z: {int(tracklet.spatialCoordinates.z)}", (x2 + 10, y1 + 65), cv2.FONT_HERSHEY_TRIPLEX, 0.25, 255)

                                    cv2.rectangle(edgeFrame, (x1, y1), (x2, y2), (255, 255, 0), cv2.FONT_HERSHEY_SIMPLEX)

                                self.publish_detections(["ball"], inBallDetectNN.tracklets, "oakd_right_camera", self.targetPublisher)

                            cv2.imshow("Edge", edgeFrame)
                            if pub_detection_frame:
                                self.detectionImagePub.publish(self.bridge.cv2_to_imgmsg(edgeFrame, "mono8"))

                try:
                    frameCAM = inPreviewCAM.getCvFrame()
                except:
                    self.get_logger().error("Failed to read preview frame")
                    continue

                # The Pose landmark NN input needs to be square.
                # Determine the xoffset on the left and right side of the image around
                # the square area.  This assumes a wider than taller image.
                heightCAM, widthCAM = frameCAM.shape[0:2]
                frame_size_lm = heightCAM
                xoffset = int((widthCAM - frame_size_lm)/2)

                counter += 1
                current_time = time.monotonic()
                if (current_time - startTime) > 1 :
                    fps = counter / (current_time - startTime)
                    counter = 0
                    startTime = current_time

                disp_cnt += 1
                show_frame = False
                pub_frame = (disp_cnt % 2) == 0

                # Blazepose post/host-side processing
                if human_pose and human_pose_process:
                    frameCAMOrig = frameCAM.copy()

                    # Get pose detection
                    inference = q_pd_out.tryGet()
                    if inference != None:
                        regions = blaze_pose.pd_postprocess(inference, frame_size_lm)
                        blaze_pose.pd_render(frameCAM, frame_size_lm, xoffset)

                        # Try to find a region (person) that corresponds to the
                        # the detected person reported by the Tracker node
                        sel_region = None
                        if self.tracked != None and self.tracked.tracking:
                            tracked_x = (self.tracked.object.x_min + self.tracked.object.x_max)/2
                            closest_diff = 0.0

                            for i,r in enumerate(regions):
                                # Calc normalized center of detected person
                                x = ((r.rect_points[0][1] + r.rect_points[3][1])/2 + xoffset)/widthCAM
                                diff = abs(x - tracked_x)
                                #self.get_logger().debug("region= %d, x center= %f, tracked_x= %f" % (i, x, tracked_x))
                                if sel_region == None or closest_diff > diff:
                                    sel_region = i
                                    closest_diff = diff

                        # Landmarks
                        blaze_pose.nb_active_regions = 0
                        for i,r in enumerate(regions):
                            if i != sel_region:
                                continue

                            video_frame = frameCAMOrig[0:(frame_size_lm+1),xoffset:(xoffset+frame_size_lm)]
                            frame_nn = mpu.warp_rect_img(r.rect_points, video_frame, blaze_pose.lm_input_length, blaze_pose.lm_input_length)

                            nn_data = dai.NNData()
                            nn_data.setLayer("input_1", to_planar(frame_nn, (blaze_pose.lm_input_length, blaze_pose.lm_input_length)))
                            q_lm_in.send(nn_data)

                            # Get landmarks
                            inference = q_lm_out.get()
                            blaze_pose.lm_postprocess(r, inference, xoffset)
                            #blaze_pose.lm_postprocess(r, inference)
                            last_region = r

                            last_poses = analyze_pose(r)
                            if last_poses != None:
                                self.publish_poses(last_poses)

                        blaze_pose.check_filter_reset()
                        if blaze_pose.nb_active_regions == 0:
                            last_region = None
                            last_pose = None
                    else:
                        last_poses = None

                # For debug
                if show_depth:
                    depth = depthQueue.get()
                    depthFrame = depth.getFrame()

                    depthFrameColor = cv2.normalize(depthFrame, None, 255, 0, cv2.NORM_INF, cv2.CV_8UC1)
                    depthFrameColor = cv2.equalizeHist(depthFrameColor)
                    depthFrameColor = cv2.applyColorMap(depthFrameColor, cv2.COLORMAP_HOT)

                    #if len(detections) != 0:

                    boundingBoxMapping = xoutBoundingBoxDepthMapping.get()
                    if boundingBoxMapping != None:
                        roiDatas = boundingBoxMapping.getConfigData()

                        for roiData in roiDatas:
                            roi = roiData.roi
                            roi = roi.denormalize(depthFrameColor.shape[1], depthFrameColor.shape[0])
                            topLeft = roi.topLeft()
                            bottomRight = roi.bottomRight()
                            xmin = int(topLeft.x)
                            ymin = int(topLeft.y)
                            xmax = int(bottomRight.x)
                            ymax = int(bottomRight.y)

                            cv2.rectangle(depthFrameColor, (xmin, ymin), (xmax, ymax), color, cv2.FONT_HERSHEY_SCRIPT_SIMPLEX)

                    cv2.imshow("depth", depthFrameColor)

                # Image annotations
                if show_frame or pub_frame:

                    if last_region != None:
                        blaze_pose.lm_render(frameCAM, last_region)

                    if flipCAM:
                        frameCAM = cv2.flip(frameCAM, 1)

                    if last_poses != None:
                        lp = last_poses['left']
                        rp = last_poses['right']
                    else:
                        lp = rp = "none"
                    OverlayTextOnBox(frameCAM, 0, 0, 10, 10, [f"PoseL: {lp}", f"PoseR: {rp}"], (0, 0, 0), 0.4, font, 0.6, white, 1)

                    # Display detections
                    for tracklet in tracklets:
                        try:
                            label = self.labelMap[tracklet.label]
                        except:
                            label = tracklet.label
                        if label != 'person' or tracklet.status != dai.Tracklet.TrackingStatus.TRACKED:
                            continue

                        # Denormalize bounding box
                        x1 = int(tracklet.srcImgDetection.xmin*widthCAM)
                        x2 = int(tracklet.srcImgDetection.xmax*widthCAM)
                        y1 = int(tracklet.srcImgDetection.ymin*heightCAM)
                        y2 = int(tracklet.srcImgDetection.ymax*heightCAM)

                        if flipCAM:
                            swap = x2
                            x2 = max(0, widthCAM - x1)
                            x1 = max(0, widthCAM - swap)

                        y1 = max(0, y1)
                        y2 = max(0, y2)

                        if show_det_info and self.tracked != None and self.tracked.object.id == tracklet.id:
                            #conf = "{:d}%".format(int(tracklet.srcImgDetection.confidence*100))
                            conf = None
                            pos_x = f"x: {int(tracklet.spatialCoordinates.z)}"
                            pos_y = f"y: {int(tracklet.spatialCoordinates.x)*-1}"
                            pos_z = f"z: {int(tracklet.spatialCoordinates.y)}"
                            trk_id = f'id: {tracklet.id}'
                            OverlayTextOnBox(frameCAM, x1 + 2, y1 + 2, 5, 5, [conf, pos_x, pos_y, pos_z, trk_id], (0, 0, 0), 0.4, font, font_scale, white, 1)

                        cv2.rectangle(frameCAM, (x1, y1), (x2, y2), white, font)

                    OverlayTextOnBox(frameCAM, 0, frameCAM.shape[0] - 25, 5, 5, ["fps: {:.2f}".format(fps)], (0, 0, 0), 0.4, font, font_scale, white, 1)

                    # Normally image is shown by Viewer node when showing
                    # on robot display
                    if show_frame:
                        cv2.imshow("camera", frameCAM)
                        if self.setWinPos:
                            self.setWinPos = False
                            cv2.moveWindow("camera", 78, 30)

                    # Publish image to other nodes
                    if pub_frame:
                        self.imagePub.publish(self.bridge.cv2_to_imgmsg(frameCAM, "bgr8"))

                    # Frame capture to file when commanded from another node
                    if self.save_image != None:
                        if self.save_image.filepath.find("#") != -1:
                            self.save_image.filepath = self.save_image.filepath.replace("#", str(save_cnt))
                            save_cnt += 1

                        cv2.imwrite(self.save_image.filepath, frameCAMOrig)
                        self.get_logger().debug("Saved frame to [%s]" % self.save_image.filepath)
                        self.save_image = None

                if use_imu and imuData != None:
                    imuPackets = imuData.packets
                    for imuPacket in imuPackets:
                        rVvalues = imuPacket.rotationVector
                        acceleroValues = imuPacket.acceleroMeter
                        self.publish_head_rotation(rVvalues, acceleroValues)

                if cv2.waitKey(1) == ord('q'):
                    break

    def create_ball_detector(self, pipeline, stereo):
        imageManip = pipeline.create(dai.node.ImageManip)
        imageManip.initialConfig.setResize(512, 320)
        imageManip.setKeepAspectRatio(False)
        # Its input
        stereo.rectifiedRight.link(imageManip.inputImage)

        edgeDetector = pipeline.create(dai.node.EdgeDetector)
        # Its input
        imageManip.out.link(edgeDetector.inputImage)

        xoutEdge = pipeline.create(dai.node.XLinkOut)
        xoutEdge.setStreamName("edge_image")
        edgeDetector.outputImage.link(xoutEdge.input)

        spatialDetectionNetwork = pipeline.create(dai.node.YoloSpatialDetectionNetwork)
        spatialDetectionNetwork.setConfidenceThreshold(0.40)
        spatialDetectionNetwork.setBlobPath(get_model_path('ball_detect_yolo_v4_tiny_openvino_2021.4_5shave.blob'))
        spatialDetectionNetwork.setNumInferenceThreads(2)

        spatialDetectionNetwork.input.setBlocking(False)
        spatialDetectionNetwork.setBoundingBoxScaleFactor(0.5)
        spatialDetectionNetwork.setDepthLowerThreshold(100)
        spatialDetectionNetwork.setDepthUpperThreshold(5000)

        spatialDetectionNetwork.setNumClasses(1)
        spatialDetectionNetwork.setCoordinateSize(4)
        spatialDetectionNetwork.setAnchors(np.array([10,14, 23,27, 37,58, 81,82, 135,169, 344,319]))
        spatialDetectionNetwork.setAnchorMasks({ "side32": np.array([0,1,2]), "side16": np.array([3,4,5]) })
        spatialDetectionNetwork.setIouThreshold(0.3)
        # Its inputs
        stereo.depth.link(spatialDetectionNetwork.inputDepth)
        edgeDetector.outputImage.link(spatialDetectionNetwork.input)


        # Create object tracker
        objectTracker = pipeline.createObjectTracker()
        # track only person
        # possible tracking types: ZERO_TERM_COLOR_HISTOGRAM, ZERO_TERM_IMAGELESS
        objectTracker.setTrackerType(dai.TrackerType.SHORT_TERM_IMAGELESS)
        # Not in depthai 2.14.1.0
        #objectTracker.setTrackerIdAssigmentPolicy(dai.TrackerIdAssigmentPolicy.UNIQUE_ID)
        # Its input
        spatialDetectionNetwork.passthrough.link(objectTracker.inputTrackerFrame)
        spatialDetectionNetwork.passthrough.link(objectTracker.inputDetectionFrame)
        spatialDetectionNetwork.out.link(objectTracker.inputDetections)

        nnBallDetOut = pipeline.create(dai.node.XLinkOut)
        nnBallDetOut.setStreamName("ball_detections")
        # Its input
        objectTracker.out.link(nnBallDetOut.input)
    
    def setup_imu(self, pipeline):
        imu = pipeline.create(dai.node.IMU)
        xlinkOut = pipeline.create(dai.node.XLinkOut)
        xlinkOut.setStreamName("imu")

        # enable ROTATION_VECTOR at 10 hz rate
        imu.enableIMUSensor([dai.IMUSensor.ROTATION_VECTOR, dai.IMUSensor.ACCELEROMETER_RAW], 10)
        imu.setBatchReportThreshold(1)
        imu.setMaxBatchReports(10)
        # Link plugins IMU -> XLINK
        imu.out.link(xlinkOut.input)

    def create_pipeline(self):
        # Start defining a pipeline
        pipeline = dai.Pipeline()
#        pipeline.setOpenVINOVersion(version = dai.OpenVINO.Version.VERSION_2021_2)
        pipeline.setOpenVINOVersion(version = dai.OpenVINO.Version.VERSION_2021_4)

        monoLeft = pipeline.createMonoCamera()
        monoRight = pipeline.createMonoCamera()
        monoLeft.setResolution(dai.MonoCameraProperties.SensorResolution.THE_400_P)
        monoLeft.setBoardSocket(dai.CameraBoardSocket.LEFT)
        monoLeft.setFps(frame_rate);
        monoRight.setResolution(dai.MonoCameraProperties.SensorResolution.THE_400_P)
        monoRight.setBoardSocket(dai.CameraBoardSocket.RIGHT)
        monoLeft.setFps(frame_rate);

        # Stereo Depth
        stereo = pipeline.createStereoDepth()
        stereo.setConfidenceThreshold(255)
        #stereo.setMedianFilter(dai.StereoDepthProperties.MedianFilter.KERNEL_7x7)
        # Its inputs
        monoLeft.out.link(stereo.left)
        monoRight.out.link(stereo.right)

        # Color camera
        colorCam = pipeline.createColorCamera()
        colorCam.setPreviewSize(640, 360)

        colorCam.setResolution(dai.ColorCameraProperties.SensorResolution.THE_1080_P)
        colorCam.setInterleaved(False)
        colorCam.setColorOrder(dai.ColorCameraProperties.ColorOrder.BGR)
        colorCam.setFps(frame_rate)
        colorCam.setPreviewKeepAspectRatio(False)

        # Scale video from 1920x1080 to 640x360
        # (This was a workaround for an issue with depthai)
        colorCam.setIspScale((1,3))

        manip_mn = pipeline.createImageManip()
        if use_tyolo_v4:
            manip_mn.initialConfig.setResize(416, 416)
        else:
            manip_mn.initialConfig.setResize(300, 300)
        #manip_mn.setKeepAspectRatio(True)
        manip_mn.setKeepAspectRatio(False)
        colorCam.preview.link(manip_mn.inputImage)

        # Spatial detection network
        if use_tyolo_v4:
            spatialDetectionNetwork = pipeline.createYoloSpatialDetectionNetwork()
            spatialDetectionNetwork.setBlobPath(get_model_path('tiny-yolo-v4_openvino_2021.2_6shave.blob'))
            spatialDetectionNetwork.setNumClasses(80)
            spatialDetectionNetwork.setCoordinateSize(4)
            spatialDetectionNetwork.setAnchors(np.array([10,14, 23,27, 37,58, 81,82, 135,169, 344,319]))
            spatialDetectionNetwork.setAnchorMasks({ "side26": np.array([1,2,3]), "side13": np.array([3,4,5]) })
            spatialDetectionNetwork.setIouThreshold(0.5)
            self.labelMap = labelMap_TYolo4
            # person
            track_types = [0]
        else:
            spatialDetectionNetwork = pipeline.createMobileNetSpatialDetectionNetwork()
#            spatialDetectionNetwork.setBlobPath(get_model_path('mobilenet-ssd_openvino_2021.2_6shave.blob'))
            spatialDetectionNetwork.setBlobPath(get_model_path('mobilenet-ssd_openvino_2021.4_5shave.blob'))
            self.labelMap = labelMap_MNetSSD
            # person
            track_types = [15]

        spatialDetectionNetwork.setNumInferenceThreads(1)
        spatialDetectionNetwork.setConfidenceThreshold(0.3)
        spatialDetectionNetwork.input.setQueueSize(1)
        spatialDetectionNetwork.input.setBlocking(False)
        spatialDetectionNetwork.setBoundingBoxScaleFactor(0.3)
        spatialDetectionNetwork.setDepthLowerThreshold(100)
        spatialDetectionNetwork.setDepthUpperThreshold(10000)
        # Its inputs
        manip_mn.out.link(spatialDetectionNetwork.input)
        #colorCam.preview.link(spatialDetectionNetwork.input)
        stereo.depth.link(spatialDetectionNetwork.inputDepth)

        if use_tracker:
            # Create object tracker
            objectTracker = pipeline.createObjectTracker()
            # track only person
            objectTracker.setDetectionLabelsToTrack(track_types)
            # possible tracking types: ZERO_TERM_COLOR_HISTOGRAM, ZERO_TERM_IMAGELESS
            objectTracker.setTrackerType(dai.TrackerType.ZERO_TERM_COLOR_HISTOGRAM)
            # Not in depthai 2.14.1.0
            #objectTracker.setTrackerIdAssigmentPolicy(dai.TrackerIdAssigmentPolicy.UNIQUE_ID)
            # Its input
            spatialDetectionNetwork.passthrough.link(objectTracker.inputTrackerFrame)
            spatialDetectionNetwork.passthrough.link(objectTracker.inputDetectionFrame)
            spatialDetectionNetwork.out.link(objectTracker.inputDetections)

        # Create outputs to the host
        xoutCam = pipeline.createXLinkOut()
        xoutCam.setStreamName("cam_out")
        if cam_out_use_preview:
            if syncNN:
                spatialDetectionNetwork.passthrough.link(xoutCam.input)
            else:
                colorCam.preview.link(xoutCam.input)
        else:
            colorCam.video.link(xoutCam.input)

        depthRoiMap = pipeline.createXLinkOut()
        depthRoiMap.setStreamName("boundingBoxDepthMapping")
        spatialDetectionNetwork.boundingBoxMapping.link(depthRoiMap.input)

        if show_depth:
            xoutDepth = pipeline.createXLinkOut()
            xoutDepth.setStreamName("depth")
            spatialDetectionNetwork.passthroughDepth.link(xoutDepth.input)

        nnOut = pipeline.createXLinkOut()
        nnOut.setStreamName("detections")

        if use_tracker:
            objectTracker.out.link(nnOut.input)
        else:
            spatialDetectionNetwork.out.link(nnOut.input)

        ######################################################
        # Ball detector

        if ball_detect:
            self.create_ball_detector(pipeline, stereo)

        ######################################################
        # Human Pose Detection, Blazepose

        if human_pose:
            # Scale cam preview output for Blazepose person detector
            manip_bp = pipeline.createImageManip()
            manip_bp.initialConfig.setResize(128, 128)
            manip_bp.setKeepAspectRatio(True)
            # Its input
            colorCam.preview.link(manip_bp.inputImage)

            # First stage pose detector
            self.get_logger().debug("Creating Pose Detection Neural Network...")
            pd_nn = pipeline.createNeuralNetwork()
            pd_nn.setBlobPath(get_model_path("pose_detection.blob"))
            # Increase threads for detection
            # pd_nn.setNumInferenceThreads(2)
            # Specify that network takes latest arriving frame in non-blocking manner
            # Pose detection input
            pd_nn.input.setQueueSize(1)
            pd_nn.input.setBlocking(False)
            # Its input
            manip_bp.out.link(pd_nn.input)

            # Pose detection output
            pd_out = pipeline.createXLinkOut()
            pd_out.setStreamName("pd_out")
            pd_nn.out.link(pd_out.input)

             # Define landmark model
            self.get_logger().debug("Creating Landmark Neural Network...")
            lm_nn = pipeline.createNeuralNetwork()
            lm_nn.setBlobPath(get_model_path("pose_landmark_full_body.blob"))
            lm_nn.setNumInferenceThreads(1)

            # Landmark input
            lm_in = pipeline.createXLinkIn()
            lm_in.setStreamName("lm_in")
            lm_in.out.link(lm_nn.input)

            # Landmark output
            lm_out = pipeline.createXLinkOut()
            lm_out.setStreamName("lm_out")
            lm_nn.out.link(lm_out.input)

        if use_imu:
            self.setup_imu(pipeline)

        self.get_logger().debug("Pipeline created.")
        return pipeline

    # Publish detections to other ROS nodes
    # Uses a custom message.
    def publish_detections(self, labelMap, tracklets, camera, publisher):
        # Build a message containing the objects.  Uses
        # a custom message format
        objList = []

        self.get_logger().debug("Publishing detections for camera: %s" % camera)


        for tracklet in tracklets:
            try:
                label = labelMap[tracklet.label]
            except:
                label = tracklet.label

            # Hack to avoid false person detection of blank wall
            if (label == 'person' and (tracklet.srcImgDetection.xmax - tracklet.srcImgDetection.xmin) > 0.7):
                continue

            desc = ObjectDesc()
            desc.frame = camera
            desc.id = tracklet.id
            desc.track_status = str(tracklet.status).split(".")[1]
            desc.name = str(label)
            desc.confidence = tracklet.srcImgDetection.confidence
            # Map to ROS convention
            desc.x = tracklet.spatialCoordinates.z
            desc.y = -1*tracklet.spatialCoordinates.x
            desc.z = tracklet.spatialCoordinates.y
            desc.c = 0
            desc.x_min = tracklet.srcImgDetection.xmin
            desc.x_max = tracklet.srcImgDetection.xmax
            desc.y_min = tracklet.srcImgDetection.ymin
            desc.y_max = tracklet.srcImgDetection.ymax
            objList += (desc,)

        # Publish the object message to our topic
        msgObjects = ObjectDescArray()
        msgObjects.objects = objList
        publisher.publish(msgObjects)

    # Publish the interpreted pose from the Blazepose detection
    def publish_poses(self, poses):
        msg = DetectedPose()
        msg.detected = poses["detected"]
        msg.left = poses['left']
        msg.right = poses['right']
        msg.num_points = poses['num_points']
        self.posePublisher.publish(msg)

    # Subscribed-to topic for enabling/disabling pose detection
    def pose_detect_enable_callback(self, msg):
        global human_pose_process
        self.get_logger().info('Received EnablePoseDetect msg: mode: %d' % msg.enable)
        human_pose_process = msg.enable
        if msg.enable is False:
            last_region = None

    # Subscribed-to topic specifying which object is of interest
    # and should be annotated in the image.
    def tracked_callback(self, msg):
        self.tracked = msg
        self.get_logger().debug("tracked_callback, id= %d" % msg.id)

    # Subscribed-to topic for triggering an image capture
    def save_image_callback(self, msg):
        self.save_image = msg
        self.get_logger().debug("save_image_callback, fname= %s" % msg.filepath)

    # Publish the head (camera) orientation as measured by the IMU
    def publish_head_rotation(self, q, a):
        msg = HeadImu()
        msg.rotation.x = q.i
        msg.rotation.y = q.j
        msg.rotation.z = q.k
        msg.rotation.w = q.real
        msg.accelx = a.x
        msg.accely = a.y
        msg.accelz = a.z
        self.get_logger().debug('accely: %f' % a.y)        
        self.headImuPublisher.publish(msg)

def main(args=None):
    rclpy.init(args=args)
    depthai_publisher = RobotVision()

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    depthai_publisher.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()