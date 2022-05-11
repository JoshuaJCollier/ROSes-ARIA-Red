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
facing = False
start = 0

gpsStarted = False
# "gpstravel_cmd_vel"
pub = rospy.Publisher("gps_travel_cmd_vel", Twist, queue_size=10)

def currentGoalCallback(data):
    global gpsStarted, currentGoal
    currentGoal = data.currentGoal

def gpsPosCallback(data):
    global gpsStarted, currentGPSPos
    currentGPSPos = (data.latitude, data.longitude)
    if (not gpsStarted):
        gpsStarted = True
    
def publisherCallback(event):
    global gpsStarted, pub, currentGPSPos, facing, start
    if (not gpsStarted):
        start = time.perf_counter()
    if (gpsStarted):
        goals = [(2, 2), (1, 5), (1, 4)]
        relativeGoals = []
        for i in range(len(goals)):
            # relative goals
            relativeGoals.append((goals[i][0] - currentGPSPos[0], goals[i][1] - currentGPSPos[1]))
        
        goal = goals[currentGoal]
        msg = Twist()
        
        # calculate heading and distance
        alpha = math.atan2(goal[1],goal[0])
        dist = math.sqrt(math.pow(goal[1], 2) + math.pow(goal[0],2))
        
        # make this based on the heading thing instead, and then the other is an elif
        if (time.perf_counter() < (start+alpha*2)):
            msg.angular.z = -0.5
        # CHange this to dist > 1  
        if (time.perf_counter() < (start+dist*2+alpha*2)) and (time.perf_counter() > (start+alpha*2)):
            msg.linear.x = 0.5
        # Make this the else
        elif (time.perf_counter() > (start+dist*2)):
            msg.linear.x = 0
                
        pub.publish(msg)

def main():
    global start
    rospy.init_node('GPSTravel', anonymous=True)
    subTopic = rospy.get_param('~topic', 'fix')
    goalTopic = rospy.get_param('~topic', 'currentGoal')
    rospy.Subscriber(subTopic, NavSatFix, gpsPosCallback)
    rospy.Subscriber(goalTopic, CurrentGoal, currentGoalCallback)
    timer = rospy.Timer(rospy.Duration(0.2), publisherCallback)
    start = time.perf_counter()
    rospy.spin()
    timer.shutdown()

if __name__ == '__main__':
    print("Running")
    main()