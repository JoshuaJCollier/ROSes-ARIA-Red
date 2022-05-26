#!/usr/bin/env python
import rospy
import sys
import time
import math

# Predefined message data
from geometry_msgs.msg import Twist
from megamind.msg import Decision
from sensor_msgs.msg import NavSatFix
from visualization_msgs.msg import Marker

decision = Decision()
pub = rospy.Publisher("visualization_marker", Marker, queue_size=100) # change topic name
lastState = -1
gpsStarted = False

SPHERE           = 2
CYLINDER         = 3
LINE_STRIP       = 4
POINTS           = 8
TEXT_VIEW_FACING = 9

ADD = 0

textYPos = 1.0

coneID = 1
bucketID = 1
pointID = 1

startlat, startlong = 0, 0

currentGPSPos = (0,0)

def gpsPosCallback(data):
    global gpsStarted, currentGPSPos
    currentGPSPos = (data.latitude, data.longitude)

    if (not gpsStarted):
        gpsStarted = True

def decisionCallback(data):
	global decision
	decision = data

def publisherCallback(event):
    global decision, lastState, bucketID, coneID, pointID, startlat, startlong, currentGPSPos

    if ((lastState == -1) and gpsStarted):
        startlat = currentGPSPos[0]
        startlong = currentGPSPos[1]
    
    # Display robot path by placing a marker at every point it travels to

    if (gpsStarted):
        point = Marker()
        point.header.frame_id = "odom"
        point.ns = "Robot-path"
        pointID = pointID + 1
        point.id = pointID            # ID should increase with every point - not sure how to increase
        point.type = SPHERE 
        point.action = ADD
        point.pose.position.x = (currentGPSPos[0] - startlat) * 100000  # latitude
        point.pose.position.y = (currentGPSPos[1] - startlong) * 100000 # longitude
        point.pose.position.z = 0
        point.color.r = 1.0
        point.color.g = 0.0
        point.color.b = 0.0
        point.color.a = 1.0
        point.scale.x = 0.2     # size of the point
        point.scale.y = 0.2

        pub.publish(point)

    if (gpsStarted and (decision.mindState != lastState)):
        lastState = decision.mindState

        # Display text of current state

        msg = Marker()
        msg.ns = "Current-state"
        msg.header.frame_id = "odom"
        msg.id = 1
        msg.type = msg.TEXT_VIEW_FACING
        msg.action = ADD                          # 0 = add/modify, 1 = (deprecated), 2 = delete, (New in Indigo) 3 = deleteall
        msg.pose.position.x = 0.0
        msg.pose.position.y = textYPos + 3
        msg.pose.position.z = 0.0
        msg.pose.orientation.x = 0.0
        msg.pose.orientation.y = 0.0
        msg.pose.orientation.z = 0.0
        msg.pose.orientation.w = 1.0

        if (decision.mindState == 0) and (decision.gps_travel_on == 0):
            message = "finding heading"
        elif (decision.mindState == 0) and (decision.gps_travel_on == 1):
            message = "goal seeking"
        elif decision.mindState == 1:
            message = "avoiding object"
        elif decision.mindState == 2:
            message = "finding cone"
        elif decision.mindState == 3:
            message = "taking cone picture"
        elif decision.mindState == 4:
            message = "taking bucket picture"

        msg.text = "Current state: {}, {}.".format(decision.mindState, message)
       
        msg.scale.x = 1.0
        msg.scale.y = 1.0
        msg.scale.z = 1.0
        msg.color.r = 0.0
        msg.color.g = 1.0
        msg.color.b = 1.0
        msg.color.a = 1.0

        pub.publish(msg)

        # Display next intended state

        nextState = Marker()
        nextState.ns = "Intended-state"
        nextState.header.frame_id = "odom"
        nextState.id = 1
        nextState.type = nextState.TEXT_VIEW_FACING
        nextState.action = ADD       
        nextState.pose.position.x = 0.0
        nextState.pose.position.y = textYPos + 1.5
        nextState.pose.position.z = 0.0
        nextState.pose.orientation.x = 0.0
        nextState.pose.orientation.y = 0.0
        nextState.pose.orientation.z = 0.0
        nextState.pose.orientation.w = 1.0

        if (decision.mindState == 0):
            NSmessage = "goal seeking"
        elif (decision.mindState == 0):
            NSmessage = "avoiding object"
        elif decision.mindState == 1:
            NSmessage = "finding cone"
        elif decision.mindState == 2:
            NSmessage = "taking cone picture"
        elif decision.mindState == 3:
            NSmessage = "taking bucket picture"
        elif decision.mindState == 4:
            NSmessage = "finding heading"

        nextState.text = "Next intended state: {}, {}.".format(NSmessage)
        nextState.scale.x = 1.0
        nextState.scale.y = 1.0
        nextState.scale.z = 1.0
        nextState.color.r = 0.0
        nextState.color.g = 1.0
        nextState.color.b = 1.0
        nextState.color.a = 1.0

        pub.publish(nextState)

        # Display orange cone if at taking cone picture
        if (decision.mindState == 3):
            cone = Marker()
            cone.ns = "Robot-path"
            coneID = coneID + 1
            cone.id = coneID         
            cone.type = CYLINDER    # can use POINTS=8, SPHERES=2, or LINE_STRIP=4 but need last point
            cone.action = ADD
            cone.pose.position.x = (currentGPSPos[0] - startlat) * 100000 + 2   # Could use heading to place it a bit in front
            cone.pose.position.y = (currentGPSPos[1] - startlat) * 100000
            cone.pose.position.z = 0
            cone.color.r = 1.0      # orange colour
            cone.color.g = 0.5
            cone.color.b = 0.0
            cone.color.a = 1.0
            cone.scale.x = 1.0      # size is 0.1m
            cone.scale.y = 1.0
            cone.scale.z = 2.0
            pub.publish(cone)

        # Display red bucket if taking bucket picture

        if (decision.mindState == 4):
            bucket = Marker()
            bucket.ns = "Robot-bucket"
            bucketID = bucketID + 1
            bucket.id = bucketID           
            bucket.type = CYLINDER      # can use POINTS=8, SPHERES=2, or LINE_STRIP=4 but need last point
            bucket.action = ADD
            bucket.pose.position.x = (currentGPSPos[0] - startlat) * 100000 - 2   # Could use heading to place it a bit in front
            bucket.pose.position.y = (currentGPSPos[1] - startlat) * 100000
            bucket.pose.position.z = 0
            bucket.color.r = 1.0        # red colour
            bucket.color.g = 0.0
            bucket.color.b = 0.0
            bucket.color.a = 1.0
            bucket.scale.x = 1.0        # size is 1m
            bucket.scale.y = 1.0
            bucket.scale.z = 1.5        # height  

            pub.publish(bucket)

    # Display calculated distance to bucket

    if ((decision.mindState == 4) and decision.bucketDist):
        dist = Marker()
        dist.ns = "Bucket-dist"
        dist.header.frame_id = "odom"
        dist.id = 1
        dist.type = dist.TEXT_VIEW_FACING
        dist.action = ADD                          # 0 = add/modify, 1 = (deprecated), 2 = delete, (New in Indigo) 3 = deleteall

        dist.pose.position.x = 0.0
        dist.pose.position.y = textYPos
        dist.pose.position.z = 0.0

        dist.pose.orientation.x = 0.0
        dist.pose.orientation.y = 0.0
        dist.pose.orientation.z = 0.0
        dist.pose.orientation.w = 1.0

        dist.text = "Distance to bucket: {}.".format(decision.bucketDist)

        dist.scale.x = 1.0
        dist.scale.y = 1.0
        dist.scale.z = 1.0
            
        dist.color.r = 0.0
        dist.color.g = 1.0
        dist.color.b = 1.0
        dist.color.a = 1.0 


def main():
    rospy.init_node('GUI', anonymous=True)
    gpsTopic = rospy.get_param('~topic', 'fix')
    megaTopic = rospy.get_param('~topic', 'decision')
    rospy.Subscriber(gpsTopic, NavSatFix, gpsPosCallback)
    rospy.Subscriber(megaTopic, Decision, decisionCallback)
    timer = rospy.Timer(rospy.Duration(0.2), publisherCallback)

    rospy.spin()
    timer.shutdown()

if __name__ == '__main__':
    print("running")
    main()