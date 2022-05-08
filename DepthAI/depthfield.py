# Reference: https://www.youtube.com/watch?v=vtKAUafeOl0

import cv2
import numpy as np
import depthai as dai

def getFrame(queue):
    frame = queue.get()                         # get last frame from queue
    return frame.getCvFrame()                   # convert to openCV format

def getMonoCamera(pipeline, isLeft):            # takes in the pipeline
    mono = pipeline.createMonoCamera()          # creates mono camera -- one camera
    # set camera resolution: (need the "THE" because can't have number as the first letter of constant)
    mono.setResolution(dai.MonoCameraProperties.SensorResolution.THE_400_P)

    if isLeft:                                  # choose left or right camera
        mono.setBoardSocket(dai.CameraBoardSocket.LEFT)  # link to left camera
    else :
        mono.setBoardSocket(dai.CameraBoardSocket.RIGHT) # link to right camera
    return mono

if __name__ == '__main__':
    pipeline = dai.Pipeline()                   # define pipeline - collection of nodes
    monoLeft = getMonoCamera(pipeline, isLeft = True)   # setup left camera
    monoRight = getMonoCamera(pipeline, isLeft = False) # setup right camera

    # create XLinks for left and right cameras to communicate with host (input or output)
    xoutLeft = pipeline.createXLinkOut()
    xoutLeft.setStreamName("left")              # name output node
    xoutRight = pipeline.createXLinkOut()
    xoutRight.setStreamName("right")            # name output node

    # attach XLinks to output of cameras
    monoLeft.out.link(xoutLeft.input)           # link left node
    monoRight.out.link(xoutRight.input)         # link right node

    # until here working on host because hasn't been uploaded to device yet
    with dai.Device(pipeline) as device:        # upload to device

        # queue a number of frames (in this case only 1 frame) - first in first out
        # can also set blocking variable here --> if set to false and queue full, will override the last element of queue
        leftQueue = device.getOutputQueue(name="left", maxSize=1)   # left XLink
        rightQueue = device.getOutputQueue(name="right", maxSize=1) # right XLink

        cv2.namedWindow("Stereo Pair")          # set display window name
        sideBySide = True                       # side by side view (not one frame view)
    
    while True:
        leftFrame = getFrame(leftQueue)         # get left frame and convert to opencv format
        rightFrame = getFrame(rightQueue)       # get right frame and convert to opencv format

        if sideBySide:                          # side by side view 
            imOut = np.hstack((leftFrame, rightFrame))
        else :                                  # merged view of overlapping frames
            imOut = np.uint8(leftFrame/2 + rightFrame/2)

        cv2.imshow("Stereo Pair", imOut)        # display output image  

        key = cv2.waitKey(1)                    # check for a keyboard input
        if key == ord('q'):                     # quit if q pressed
            break
        elif key == ord('t'):                   # toggle display view if t pressed
            sideBySide = not sideBySide

# distance sensed - the greater the disparity of objects between the two frames, the closer they are to the camera
# 30 Q size is used by default
# frame Q memory is managed on OAKD
# frame = queue.get()                         # allows decoding of multiple frames
# gather frames and process last frame - get last frame from queue


