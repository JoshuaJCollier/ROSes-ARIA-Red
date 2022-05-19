#!/usr/bin/env python3
import rospy
import sys
import time
import math

# Predefined message data
from geometry_msgs.msg import Twist
from megamind.msg import Decision
from sensor_msgs.msg import NavSatFix

decision = Decision()
pub = rospy.Publisher("gui", Marker, queue_size=10) # change topic name

def decisionCallback(data):
	global decision
	decision = data 
 
def publisherCallback(event):
    global decision

    msg = Marker()
    msg.ns = ""
    msg.id = 0
    msg.header.frame_id = self.global_frame  # don't need?
    msg.id = self.marker_idx
    msg.type = marker.TEXT_VIEW_FACING
    msg.action = 0                          # 0 = add/modify, 1 = (deprecated), 2 = delete, (New in Indigo) 3 = deleteall

    msg.pose.position.x = 0.0
    msg.pose.position.y = 1.0
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

    msg.text = "Current state: {}".format(message)

    msg.scale.x = 10.0
    msg.scale.y = 10.0
    msg.scale.z = 1.0
        
    msg.color.r = 1.0
    msg.color.g = 0.0
    msg.color.b = 0.0
    msg.color.a = 0.0

    pub.publish(msg)


def main():
	megaTopic = rospy.get_param('~topic', 'fix')
	rospy.Subscriber(megaTopic, Decision, decisionCallback)
	timer = rospy.Timer(rospy.Duration(0.2), publisherCallback)
	rospy.spin()
	timer.shutdown()


