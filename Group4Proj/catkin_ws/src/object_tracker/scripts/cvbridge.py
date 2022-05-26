import roslib
roslib.load_manifest('object_tracker')
import sys
import rospy
import numpy as np
import cv2
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError
from object_tracker.msg import Objects
from megamind.msg import Decision
import math 
import time

count = 0
index = 0
decision = Decision()
DIR = r'~/Desktop/Group4Proj/pictures/'

class image_converter:
    def __init__(self):
        self.image_pub = rospy.Publisher("image_out",Image,queue_size=10)
        self.tracker_pub = rospy.Publisher("object_detect",Objects,queue_size=10)

        self.bridge = CvBridge()
        self.image_sub = rospy.Subscriber("/rgb_stereo_publisher/color/image",Image,self.callback)
        self.mega_sub = rospy.Subscriber("decision",Decision,self.megacall)

    def takePhoto(self,image):
        global index
        cv2.imwrite(('{}cone{}.png'.format(DIR,int(index))), image)
        index += 0.5
        time.sleep(1)
        
    def megaCall(self,data):
        global decision
        decision = data
        
    def callback(self,data):
        global count, decision
        try:
            cv_image = self.bridge.imgmsg_to_cv2(data, "bgr8")
        except CvBridgeError:
            print('error')

        count += 1

        if count%10==0:
            # Image Processing
            print(type(cv_image))
            print(cv_image)
            #define kernel size  
            kernelc = np.ones((7,7),np.uint8)
            kernelb = np.ones((7,7),np.uint8)
            kernelo = np.ones((7,7),np.uint8)

            # convert to hsv colorspace 
            hsv = cv2.cvtColor(cv_image, cv2.COLOR_BGR2HSV)

            # cone - blue bounding box
            lower_boundc = np.array([165, 100, 60])     
            upper_boundc = np.array([180, 255, 255])

            # bucket -- green bounding box
            lower_boundb = np.array([0, 190, 150])
            upper_boundb = np.array([4, 255, 255])

            # blue object 
            lower_boundo = np.array([107, 20, 40])
            upper_boundo = np.array([108, 255, 100])

            # find the colors within the boundaries
            maskc = cv2.inRange(hsv, lower_boundc, upper_boundc)
            maskb = cv2.inRange(hsv, lower_boundb, upper_boundb)
            masko = cv2.inRange(hsv, lower_boundo, upper_boundo)

            # use pixel area?
            # Remove unnecessary noise from mask

            maskc = cv2.morphologyEx(maskc, cv2.MORPH_CLOSE, kernelc)
            maskc = cv2.morphologyEx(maskc, cv2.MORPH_OPEN, kernelc)

            maskb = cv2.morphologyEx(maskb, cv2.MORPH_CLOSE, kernelb)
            maskb = cv2.morphologyEx(maskb, cv2.MORPH_OPEN, kernelb)

            masko = cv2.morphologyEx(masko, cv2.MORPH_CLOSE, kernelo)
            masko = cv2.morphologyEx(masko, cv2.MORPH_OPEN, kernelo)

            # Segment only the detected region

            segmented_imgc = cv2.bitwise_and(cv_image, cv_image, mask=maskc)
            segmented_imgb = cv2.bitwise_and(cv_image, cv_image, mask=maskb)

            # Find contours from the mask

            contoursc, hierarchy = cv2.findContours(maskc.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
            contoursb, hierarchy = cv2.findContours(maskb.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
            contourso, hierarchy = cv2.findContours(masko.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

            output = cv2.drawContours(cv_image, contoursc, -1, (255, 0, 0), 3)
            output = cv2.drawContours(cv_image, contoursb, -1, (0, 255, 0), 3)
            output = cv2.drawContours(cv_image, contourso, -1, (0, 0, 255), 3)

            cntc = sorted(contoursc, key = cv2.contourArea, reverse = True)[:5]
            cntb = sorted(contoursb, key = cv2.contourArea, reverse = True)[:5]
            cnto = sorted(contourso, key = cv2.contourArea, reverse = True)[:5]
            # loop over the contours
            tracker = Objects()

            for c in cntc:
                # approximate the contour
                peri = cv2.arcLength(c, True)
                approx = cv2.approxPolyDP(c, 0.065 * peri, True)
                area = cv2.contourArea(c)
                # if our approximated contour has four points, then we
                # can assume that we have found our screen
                if len(approx) == 3 and area > 10000:
                    xc, yc, wc, hc = cv2.boundingRect(c); contc = cv2.rectangle(cv_image,(xc,yc),(xc+wc,yc+hc),(250,0,0),4)
                    cv2.putText(cv_image, text= "cone", org=(xc+20,yc+30),
                    fontFace= cv2.FONT_HERSHEY_DUPLEX, fontScale=2, color=(0,0,0),
                    thickness=2, lineType=cv2.LINE_AA)
                    tracker.coneX = xc
                    tracker.coneY = 2000-yc
                    tracker.coneW = wc
                    tracker.coneH = hc
                    tracker.coneDist = 30/math.sqrt(hc)
                    tracker.cone = 1
                    
                    cv2.putText(cv_image, text= '{:.2f}m'.format(tracker.coneDist), org=(xo+20,yo+60),
                    fontFace= cv2.FONT_HERSHEY_DUPLEX, fontScale=2, color=(0,0,0),
                    thickness=2, lineType=cv2.LINE_AA)

                if len(approx) == 4 and area > 10000:
                    xc, yc, wc, hc = cv2.boundingRect(c); contc = cv2.rectangle(cv_image,(xc,yc),(xc+wc,yc+hc),(0,250,0),4)
                    cv2.putText(cv_image, text= "bucket", org=(xc+20,yc+30),
                    fontFace= cv2.FONT_HERSHEY_DUPLEX, fontScale=2, color=(0,0,0),
                    thickness=2, lineType=cv2.LINE_AA)
                    tracker.bucketX = xc
                    tracker.bucketY = 2000-yc
                    tracker.bucketW = wc
                    tracker.bucketH = hc
                    tracker.bucketDist = 90/math.sqrt(hc)
                    tracker.bucket = 1
                    
                    cv2.putText(cv_image, text= '{:.2f}m'.format(tracker.bucketDist), org=(xo+20,yo+70),
                    fontFace= cv2.FONT_HERSHEY_DUPLEX, fontScale=2, color=(0,0,0),
                    thickness=2, lineType=cv2.LINE_AA)

            for c in cntb:
                # approximate the contour
                peri = cv2.arcLength(c, True)
                approx = cv2.approxPolyDP(c, 0.1 * peri, True)
                area = cv2.contourArea(c)
                if len(approx) == 3 and area > 5000:
                    xb, yb, wb, hb = cv2.boundingRect(c); contc = cv2.rectangle(cv_image,(xb,yb),(xb+wb,yb+hb),(0,250,255),2)
                    cv2.putText(cv_image, text= "cone", org=(xb+20,yb+30),
                    fontFace= cv2.FONT_HERSHEY_DUPLEX, fontScale=2, color=(0,0,0),
                    thickness=2, lineType=cv2.LINE_AA)
                    tracker.coneX = xb
                    tracker.coneY = 2000-yb
                    tracker.coneW = wb
                    tracker.coneH = hb
                    tracker.coneDist = 30/math.sqrt(hb)
                    tracker.cone = 1
                    
                    cv2.putText(cv_image, text= '{:.2f}m'.format(tracker.coneDist), org=(xo+20,yo+60),
                    fontFace= cv2.FONT_HERSHEY_DUPLEX, fontScale=2, color=(0,0,0),
                    thickness=2, lineType=cv2.LINE_AA)

                if len(approx) == 4 and area > 5000:
                    xb, yb, wb, hb = cv2.boundingRect(c); contc = cv2.rectangle(cv_image,(xb,yb),(xb+wb,yb+hb),(250,0,255),2)
                    cv2.putText(cv_image, text= "bucket", org=(xb+20,yb+30),
                    fontFace= cv2.FONT_HERSHEY_DUPLEX, fontScale=2, color=(0,0,0),
                    thickness=2, lineType=cv2.LINE_AA)
                    tracker.bucketX = xb
                    tracker.bucketY = 2000-yb
                    tracker.bucketW = wb
                    tracker.bucketH = hb
                    tracker.bucketDist = 90/math.sqrt(hb)
                    tracker.bucket = 1
                    
                    cv2.putText(cv_image, text= '{:.2f}m'.format(tracker.bucketDist), org=(xo+20,yo+70),
                    fontFace= cv2.FONT_HERSHEY_DUPLEX, fontScale=2, color=(0,0,0),
                    thickness=2, lineType=cv2.LINE_AA)


            for c in cnto:
                # approximate the contour
                peri = cv2.arcLength(c, True)
                approx = cv2.approxPolyDP(c, 0.065 * peri, True)
                area = cv2.contourArea(c)
                # if our approximated contour has four points, then we
                # can assume that we have found our screen
                if len(approx) == 4 and area > 10000:
                    xo, yo, wo, ho = cv2.boundingRect(c); contc = cv2.rectangle(cv_image,(xo,yo),(xo+wo,yo+ho),(250,0,0),4)
                    cv2.putText(cv_image, text= "object", org=(xo+20,yo+30),
                    fontFace= cv2.FONT_HERSHEY_DUPLEX, fontScale=2, color=(0,0,0),
                    thickness=2, lineType=cv2.LINE_AA)
                    tracker.objectX = xo
                    tracker.objectY = 2000-yo
                    tracker.objectW = wo
                    tracker.objectH = ho
                    tracker.objectDist = 30/math.sqrt(ho)
                    tracker.object = 1
                    
                    cv2.putText(cv_image, text= '{:.2f}m'.format(tracker.objectDist), org=(xo+20,yo+70),
                    fontFace= cv2.FONT_HERSHEY_DUPLEX, fontScale=2, color=(0,0,0),
                    thickness=2, lineType=cv2.LINE_AA)
                    
            if (decision.takePhoto == 1):
                self.takePhoto(cv_image)
            cv2.imshow("Image window", cv_image)
            cv2.waitKey(3)

            try:
                self.image_pub.publish(self.bridge.cv2_to_imgmsg(cv_image, "bgr8"))
                self.tracker_pub.publish(tracker)
            except CvBridgeError:
                print("error")
        
def main(args):
    ic = image_converter()
    rospy.init_node('image_converter', anonymous=True)
    try:
        rospy.spin()
    except KeyboardInterrupt:
        print("Shutting down")
    cv2.DestroyAllWindows()

if __name__ == '__main__':
    main(sys.argv)