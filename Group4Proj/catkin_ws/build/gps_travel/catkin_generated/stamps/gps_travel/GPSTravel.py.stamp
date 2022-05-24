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
        goals = [(-31.9805773505506, 115.8171660979887), (-31.98038731577529, 115.8171782781675), (-31.98017884452402, 115.8171702857572), (-31.98082891705035, 115.8171314540043), (-31.98081842250873, 115.8174656945906), (-31.98081842250873, 115.8174656945906), (-31.98041252344407, 115.8175647311226), (-31.98052211397503, 115.8197862220968)]
        #goals = [(-31.9808289171, 115.817131454), (-31.9803873158, 115.817178278), (-31.9804125234, 115.817564731), (-31.9801788445, 115.817170286), (-31.9808289171, 115.817131454)]
        relativeGoals = []
        for i in range(len(goals)):
            # relative goals
            relativeGoals.append((goals[i][0] - currentGPSPos[0], goals[i][1] - currentGPSPos[1]))
        
        goal = relativeGoals[currentGoal]
        msg = Twist()
        
        # calculate heading and distance
        alpha = startHeading - math.atan2(goal[1],goal[0])
        dist = math.sqrt(math.pow(goal[1], 2) + math.pow(goal[0],2))
        if alpha > math.pi:
            alpha -= 2*math.pi
        elif alpha < -math.pi:
            alpha += 2*math.pi

        # make this based on the heading thing instead, and then the other is an elif
        # we are turning at 0.5 radians per second for the radian difference times by 2
        if (time.perf_counter() < (startTime+alpha*2)):
            if alpha > 0:
                msg.angular.z = 0.5
            else:
                msg.angular.z = -0.5
        
        # some math gave the following result:
        # (31.98109143766833-31.98052883658287)/62 ~= 0.00001, which is the difference between
        # two GPS coordinates 62 meters away, thus 0.00001 is equivilent to 1m, below 2m distance
        # is used as the distance from the goal
        elif (dist > 0.00002):
            msg.linear.x = 0.5
        # Make this the else
        else:
            msg.linear.x = 0
                
        pub.publish(msg)

def main():
    global start
    rospy.init_node('GPSTravel', anonymous=True)
    gpsTopic = rospy.get_param('~topic', 'fix')
    megaTopic = rospy.get_param('~topic', 'decision')
    rospy.Subscriber(gpsTopic, NavSatFix, gpsPosCallback)
    rospy.Subscriber(megaTopic, Decision, decisionCallback)
    timer = rospy.Timer(rospy.Duration(0.2), publisherCallback)
    start = time.perf_counter()
    rospy.spin()
    timer.shutdown()

if __name__ == '__main__':
    print("Running")
    main()

