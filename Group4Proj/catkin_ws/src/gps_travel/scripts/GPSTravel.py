#!/usr/bin/env python
import rospy
import sys
import time
import math

# Predefined message data
from geometry_msgs.msg import Twist
from megamind.msg import Decision
from sensor_msgs.msg import NavSatFix

currentGPSPos = (0, 0)
currentGoal = 0
startHeading = 0
gps_travel_on = 0
startTime = 0

facing = False
start = 0

gpsStarted = False
# "gpstravel_cmd_vel"
pub = rospy.Publisher("gps_travel_cmd_vel", Twist, queue_size=10)

def decisionCallback(data):
    global gpsStarted, currentGoal, startHeading, gps_travel_on, startTime
    currentGoal = data.currentGoal
    startHeading = data.startHeading
    gps_travel_on = data.gps_travel_on
    startTime = data.startTime

def gpsPosCallback(data):
    global gpsStarted, currentGPSPos
    currentGPSPos = (data.latitude, data.longitude)
    if (not gpsStarted):
        gpsStarted = True
    
def publisherCallback(event):
    global gpsStarted, pub, currentGPSPos, facing, start, currentGoal, startHeading, gps_travel_on, startTime
    if (not gpsStarted):
        start = time.perf_counter()
    if (gpsStarted and gps_travel_on):
        goals = [(-31.980868452462268, 115.81715590281765), (-31.98075832251854, 115.81715710980328), (-31.980743349384806, 115.81712532559989)]
        relativeGoals = []
        for i in range(len(goals)):
            # relative goals
            relativeGoals.append((goals[i][0] - currentGPSPos[0], goals[i][1] - currentGPSPos[1]))
        
        goal = relativeGoals[currentGoal]
        msg = Twist()
        
        # calculate heading and distance
        alpha = startHeading - math.atan2(goal[1],goal[0])
        dist = math.sqrt(math.pow(goal[1], 2) + math.pow(goal[0],2))
        
        # make this based on the heading thing instead, and then the other is an elif
        if (time.perf_counter() < (startTime+alpha*2)):
            if alpha > 180:
                msg.angular.z = -0.5
            else:
                msg.angular.z = 0.5
        # time.perf_counter() < (start+dist*2+alpha*2)) and (time.perf_counter() > (start+alpha*2) 
        if (dist > 2):
            msg.linear.x = 0.5
        # Make this the else
        elif (dist < 2):
            msg.linear.x = 0
                
        pub.publish(msg)

def main():
    global start
    rospy.init_node('GPSTravel', anonymous=True)
    gpsTopic = rospy.get_param('~topic', 'fix')
    megaTopic = rospy.get_param('~topic', 'currentGoal')
    rospy.Subscriber(gpsTopic, NavSatFix, gpsPosCallback)
    rospy.Subscriber(megaTopic, Decision, decisionCallback)
    timer = rospy.Timer(rospy.Duration(0.2), publisherCallback)
    start = time.perf_counter()
    rospy.spin()
    timer.shutdown()

if __name__ == '__main__':
    print("Running")
    main()
