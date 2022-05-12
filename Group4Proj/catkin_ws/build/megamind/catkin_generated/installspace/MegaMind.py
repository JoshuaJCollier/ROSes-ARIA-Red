#!/usr/bin/env python3
import rospy
import sys
import time
import math

# Predefined message data
from geometry_msgs.msg import Twist
from megamind.msg import Decision
from sensor_msgs.msg import NavSatFix, Joy

currentGPSPos = (0, 0)
start = 0
gps_travel_cmd_vel_msg = Twist()
object_avoid_cmd_vel_msg = Twist()
controller_joy_in = Joy()
mindState = 0
decision = Decision()

firstPos = []
secondPos = []
startHeadingTime = 0
foundHeading = False

megaMindStarted = False

cmdVelPub = rospy.Publisher("RosAria/cmd_vel", Twist, queue_size=10)
megaPub = rospy.Publisher("decision", Decision, queue_size=10)

def medianFilter(gpsPoints):
    sumPoints = list()
    for i in range(10):
        pointSum = gpsPoints[i][0] + gpsPoints[i][1]
        # add sum to list, retaining their index in the gpsPoints list
        sumPoints.append((pointSum,i))
    
    # sort the list of sum in ascending order
    sumPoints.sort(key=lambda tup: tup[0])
    # get the index of the median sum (5th or 6th element)
    index = sumPoints[5][1]
    
    print("sorted list of sums is: " + str(sumPoints))
    print("middle index is: " + str(index))
    print("median gps point is: " + str(gpsPoints[index]))
    
    return gpsPoints[index]

def gpsPosCallback(data):
    global currentGPSPos, megaMindStarted
    currentGPSPos = (data.latitude, data.longitude)

    if (not megaMindStarted):
        megaMindStarted = True

def objectAvoidSubCallback(data):
    global object_avoid_cmd_vel_msg
    object_avoid_cmd_vel_msg = data
    
def controllerSubCallback(data):
    global controller_joy_in
    controller_joy_in = data
    
def gpsTravelSubCallback(data):
    global megaMindStarted, gps_travel_cmd_vel_msg
    gps_travel_cmd_vel_msg = data

def publisherCallback(event):
    global megaMindStarted, cmdVelPub, megaPub, currentGPSPos, gps_travel_cmd_vel_msg, object_avoid_cmd_vel_msg, controller_joy_in, mindState, decision, startHeadingTime, foundHeading
    # Mind State Definitions: 0 -> Goal Seeking, 1 -> Object Avoidance, 2 -> Cone Finding, 3 -> Cone Picture, 4 -> Bucket Picture
    
    msg = Twist()
    if (megaMindStarted):
        # 0 -> Goal Seeking
        #if (controller_joy_in.buttons[0] == 1):
        if (mindState == 0):
            if (len(firstPos) < 10):
                decision.gps_travel_on = 0
                firstPos.append(currentGPSPos)
                startHeadingTime = time.perf_counter()
            elif (len(firstPos) == 10) and (time.perf_counter() < (startHeadingTime+5)) and (not foundHeading):
                msg.linear.x = 1
            elif (time.perf_counter() > (startHeadingTime+2)) and (not foundHeading):
                if (len(secondPos) < 10):
                    secondPos.append(currentGPSPos)
                else:
                    # NOW YOU CAN CALCULATE HEADING
                    lat1, lon1 = medianFilter(firstPos)
                    lat2, lon2 = medianFilter(secondPos)
                    decision.startHeading = math.atan2(lon2-lon1,lat2-lat1)
                    decision.startTime = time.perf_counter()
                    foundHeading = True
                    decision.gps_travel_on = 1
            # do the find heading thing here, then set gps_travel to 1

            # if we see something 
            if decision.gps_travel_on == 1:
                msg = gps_travel_cmd_vel_msg

            # if distance to goal is small or we see the cone clearly or there is an obstacle, then 
            # decision.currentGoal = 1 or 2

        elif (mindState == 1):
            msg = object_avoid_cmd_vel_msg

        # if (goal has been reached):
        #     goal.currentGoal += 1

        cmdVelPub.publish(msg)
        #decision.startTime = time.perf_counter()
        megaPub.publish(decision)
        #else:
        #    print("Manual")
        #    # remap controller to direct cmd_vel controls
        #    msg.linear.x = controller_joy_in.axes[1]/2 # Up/Down of Left Stick
        #    msg.angular.z = controller_joy_in.axes[2] # Left/Right of Right Stick

def main():
    global start, mindState, goal
    rospy.init_node('GPSTravel', anonymous=True)
    fixSub = rospy.get_param('~topic', 'fix')
    gpsTravelSub = rospy.get_param('~topic', 'gps_travel_cmd_vel')
    objAvoidSub = rospy.get_param('~topic', 'object_avoid_cmd_vel')
    controllerSub = rospy.get_param('~topic', 'joy')
    rospy.Subscriber(fixSub, NavSatFix, gpsPosCallback)
    rospy.Subscriber(gpsTravelSub, Twist, gpsTravelSubCallback)
    rospy.Subscriber(objAvoidSub, Twist, objectAvoidSubCallback)
    rospy.Subscriber(controllerSub, Joy, controllerSubCallback)
    timer = rospy.Timer(rospy.Duration(0.2), publisherCallback)
    start = time.perf_counter()
    decision.currentGoal = 0
    mindState = 0
    
    rospy.spin()
    timer.shutdown()

if __name__ == '__main__':
    print("Running")
    main()
