# REFERENCE: https://www.youtube.com/watch?v=vtKAUafeOl0

# JET COLOUR GRADIENT FROM TWO STEREOS: DISPARITY MAP
# high in value / close to camera == RED
# low in value / far away == BLUE
# Operational Range (from 40cm)
# Issue 1: there will be an outline around objects of far distance (that are incorrect) - becuase one of the cameras can see edge and other cannot -- occlusion 
# Issue 2: doesn't work closer than 40cm because of triangulation - when rectified, all corresponding points lie on the same 1D scan line -- the closer an object to the camera, the larger the disparity.
    # At ~ 40cm, the object match does not lie within the area searched in rectification -- no longer within disparity range
    # If increase the disparity range - reduced the range limitation but reduce the speed due to computational hindrance
    # Baseline distance between two identical cameras (wider baseline allows further depth perception but seatch becomes more noisy - can only match pixels because they still look similar)
    # Doesn't perform well for shiny objects because it does not reflect light equally in all directions (as do lambertian objects)
    # Low light conditions make it difficult to match objects - can have projector camera (not feasible outdoors)

from inspect import modulesbyfile
from lzma import MODE_NORMAL
import cv2
import depthai as dai
import numpy as np

def getMonoCamera(pipeline, isLeft):                    # single camera
    mono = pipelone.createMonoCamera()
    mono.setResolution(dai.MonoCameraProperties.SensorResolution.THE_400_P)
    if isLeft:
        mono.setBoardSocket(dai.CameraBoardSocket.LEFT)
    else :
        mono.setBoardSocket(dai.CameraBoardSocket.RIGHT)
    return mono

def getStereoPair(pipeline, monoLeft, monoRight):       # create node for stereo pair
    stereo = pipeline.createStereoDepth()               # attach node to the pipeline
    stereo.setLeftRightCheck(True)                      # indicate wrong depth for edges of objects

    monoLeft.out.link(stereo.left)                      # link left camera
    monoRight.out.link(stereo.right)                    # link right camera
    # output depth map and rectified stereo views
    return stereo

def drawLine(event,x,y,flags,param):
    global mouseX, mouseY
    if event == cv2.EVENT_LBUTTONDOWN:
        mouseX = x                                      # tracks x point 
        mouseY = y                                      # tracks y point 

if __name__ == '__main__':
    mouseX = 0
    mouseY = 640
    pipeline = dai.Pipeline()                           # define pipeline

    monoLeft = getMonoCamera(pipeline, isLeft = True)   # setup left camera
    monoRight = getMonoCamera(pipeline, isLeft = False) # setup right camera

    # stereo depth node: attach left and right cameras to depth stereo pair
    stereo = getStereoPair(pipeline, monoLeft, monoRight) # form stereo pair by combining cameras

    xoutDepth = pipeline.createXLinkOut()               # output node for depth
    xoutDepth.setStreamName("depth")

    xoutDisp = pipeline.createXLinkOut()                # output node for disparity
    xoutDisp.setStreamName("disparity")

    xoutRectifiedLeft = pipeline.createXLinkOut()       # output node for left rectified image 
    xoutRectifiedLeft.setStreamName("rectifiedLeft")

    xoutRectifiedRight = pipeline.createXLinkOut()      # output node for right rectified image
    xoutRectifiedRight.setStreamName("rectifiedRight")

    # can also create output nodes for syncedLeft, syncedRight

    stereo.depth.link(xoutDepth.input)
    stereo.disparity.link(xoutDisp.input)

    monoLeft.out.link(xoutRectifiedLeft.input)
    monoRight.out.link(xoutRectifiedRight.input)

    stereo.rectifiedLeft.link(xoutRectifiedLeft.input)  # rectified stereo output
    stereo.rectifiedRight.link(xoutRectifiedRight.input)    

    # completed defining pipeline
    # now connect to device

    with dai.Device(pipeline) as device:
        # get queues to derive rgb frames and nn data from outputs
        depthQueue = device.getOutputQueue(name="depth",makSize=1, blocking=False)
        dispQueue = device.getOutputQueue(name="disparity",makSize=1, blocking=False)

        rectifiedLeftQueue = device.getOutputQueue(name="rectifiedLeft", maxSize=1, blocking=False)
        rectifiedRightQueue = device.getOutputQueue(name="rectifiedRight", maxSize=1, blocking=False)

        disparityMultiplier = 255/stereo.getMaxDisparity()  # multiplier for colourmapping the disparity map

        # measure where the mouse was clicked and draw line
        imOut = np.zeros((480, 1280, 3))
        cv2.namedWindow("Stereo Pair")
        cv2.setMouseCallback("Stereo Pair", drawLine)
        cv2.imshow("Stereo Pair", imOut)

        while True:
            disparity = dispQueue.get()

            im = disparity.getCvFrame()
            im = (im*disparityMultiplier).astype(np.uint8)
            im = cv2.applyColorMap(im, cv2.COLORMAP_JET)

            cv2.imshow("Disparity", im)

            left = rectifiedLeftQueue.get()
            leftFrame = left.getCvFrame()

            right = rectifiedRightQueue.get()
            rightFrame = right.getCvFrame()

            imOut = np.hstack((leftFrame,rightFrame))
            imOut = cv2.cvtColor(imOut,cv2.COLOR_GRAY2RGB)

            imOut = cv2.line(imOut,(mouseX, mouseY),(1280, mouseY),(0,0,255),2)
            imOut = cv2.circle(imOut, (mouseX, mouseY), 2, (255, 255, 128), 2)
            cv2.imshow("Stereo Pair", imOut)
            cv2.imshow("Frames", np.uint8(leftFrame/2 + rightFrame/2))

            if cv2.waitKey(1) == ord('q'):
                break



