#!/usr/bin/env python
import rospy
import sys
import time
import math

# Predefined message data
from geometry_msgs.msg import Twist
from megamind.msg import CurrentGoal
from sensor_msgs.msg import NavSatFix

currentGPSPos = (0, 0)
currentGoal = 0
start = 0
gps_travel_cmd_vel_msg = Twist()

megaMindStarted = False

cmdVelPub = rospy.Publisher("RosAria/cmd_vel", Twist, queue_size=10)
currentGoalPub = rospy.Publisher("currentGoal", CurrentGoal, queue_size=10)

def gpsPosCallback(data):
    global currentGPSPos
    currentGPSPos = (data.latitude, data.longitude)

def gpsTravelSubCallback(data):
    global megaMindStarted, gps_travel_cmd_vel_msg
    gps_travel_cmd_vel_msg = data
    
    if (not megaMindStarted):
        megaMindStarted = True

def publisherCallback(event):
    global megaMindStarted, cmdVelPub, currentGPSPos, gps_travel_cmd_vel_msg
    
    goal = CurrentGoal()
    goal.currentGoal = 0
    currentGoalPub.publish(goal)
    if (megaMindStarted):

        msg = gps_travel_cmd_vel_msg
        
        cmdVelPub.publish(msg)

def main():
    global start
    rospy.init_node('GPSTravel', anonymous=True)
    fixSub = rospy.get_param('~topic', 'fix')
    gpsTravelSub = rospy.get_param('~topic', 'gps_travel_cmd_vel')
    rospy.Subscriber(fixSub, NavSatFix, gpsPosCallback)
    rospy.Subscriber(gpsTravelSub, Twist, gpsTravelSubCallback)
    timer = rospy.Timer(rospy.Duration(0.2), publisherCallback)
    start = time.perf_counter()
    rospy.spin()
    timer.shutdown()

if __name__ == '__main__':
    print("Running")
    main()
