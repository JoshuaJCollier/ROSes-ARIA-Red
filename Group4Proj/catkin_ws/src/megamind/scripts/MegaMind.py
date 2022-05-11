#!/usr/bin/env python
import rospy
import sys
import time
import math

# Predefined message data
from geometry_msgs.msg import Twist
from megamind.msg import CurrentGoal
from sensor_msgs.msg import NavSatFix, Joy

currentGPSPos = (0, 0)
currentGoal = 0
start = 0
gps_travel_cmd_vel_msg = Twist()
object_avoid_cmd_vel_msg = Twist()
controller_joy_in = Joy()
mindState = 0
goal = CurrentGoal()

megaMindStarted = False

cmdVelPub = rospy.Publisher("RosAria/cmd_vel", Twist, queue_size=10)
currentGoalPub = rospy.Publisher("currentGoal", CurrentGoal, queue_size=10)

def gpsPosCallback(data):
    global currentGPSPos
    currentGPSPos = (data.latitude, data.longitude)

def objectAvoidSubCallback(data):
    global object_avoid_cmd_vel_msg
    object_avoid_cmd_vel_msg = data
    
def controllerSubCallback(data):
    global controller_joy_in
    controller_joy_in = data
    
def gpsTravelSubCallback(data):
    global megaMindStarted, gps_travel_cmd_vel_msg
    gps_travel_cmd_vel_msg = data
    
    if (not megaMindStarted):
        megaMindStarted = True

def publisherCallback(event):
    global megaMindStarted, cmdVelPub, currentGPSPos, gps_travel_cmd_vel_msg, object_avoid_cmd_vel_msg, controller_joy_in, mindState, goal
    # Mind State Definitions: 0 -> Goal Seeking, 1 -> Object Avoidance, 2 -> Cone Finding, 3 -> Cone Picture, 4 -> Bucket Picture
    
    msg = Twist()
    if (megaMindStarted):
        # 0 -> Goal Seeking
        if (controller_joy_in.buttons[0] == 1):
            if (mindState == 0):
                msg = gps_travel_cmd_vel_msg
            elif (mindState == 1):
                msg = object_avoid_cmd_vel_msg
            
            # if (goal has been reached):
            #     goal.currentGoal += 1
            
            cmdVelPub.publish(msg)
            currentGoalPub.publish(goal)
        else:
            print("Manual")
            # remap controller to direct cmd_vel controls
            msg.linear.x = controller_joy_in.axes[1]/2 # Up/Down of Left Stick
            msg.angular.z = controller_joy_in.axes[2] # Left/Right of Right Stick

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
    goal.currentGoal = 0
    
    rospy.spin()
    timer.shutdown()

if __name__ == '__main__':
    print("Running")
    main()
