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
        # for i in range(len(goals)):
            # relative goals
            # relativeGoals.append((goals[i][0] - currentGPSPos[0], goals[i][1] - currentGPSPos[1]))
        
        goal = goals[currentGoal]
        # write some code to get heading from current position to current goal
        # and set the speeds accordingly, also pass them to a topic that isnt
        # cmd_vel so that another node can do the final publishing to cmd_vel
        msg = Twist()
        alpha = math.atan2(goal[1],goal[0])
        dist = math.sqrt(math.pow(goal[1], 2) + math.pow(goal[0],2))
        if (time.perf_counter() < (start+alpha*2)):
            msg.angular.z = -0.5
        if (time.perf_counter() < (start+dist*2+alpha*2)) and (time.perf_counter() > (start+alpha*2)):
            msg.linear.x = 0.5
        elif (time.perf_counter() > (start+dist*2)):
            msg.linear.x = 0
        
        # msg.linear.x = 0 # forward is forward idk (meters per second)
        # msg.angular.z = -0.5 # positive angular z is turning counter clockwise (radians per second)
        
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

'''
def navSat(data):
    rospy.loginfo(rospy.get_caller_id() + "NavSatFix: %s", data.data)
    currentGPSPos = (data.data.lattitude, data.data.longitude)

def currGoal(data):
    rospy.loginfo(rospy.get_caller_id() + "Current Goal: %s", data.data)
    currentGoal = data.data

def GPSTravel():
    curentGPSPos = (0, 0)
    currentGoal = 0
    # pubTopic = rospy.get_param('~topic', 'RosAria/cmd_vel')
    subTopic = rospy.get_param('~topic', 'fix')
    sub2Topic = rospy.get_param('~topic', 'currentGoal')
    rospy.loginfo('topic = %s', "gpsTravel_cmd_vel")

    pub = rospy.Publisher("gpsTravel_cmd_vel", Twist, queue_size=10)
    sub = rospy.Subscriber(subTopic, NavSatFix, navSat)
    sub2 = rospy.Subscriber(sub2Topic, int, currGoal)
    
    rospy.init_node('GPSTravel', anonymous=True)
    
    msg = Twist()
    rate = rospy.Rate(10) # 10hz
    
    # these are relative positions
    goals = [(0, 5), (1, 5), (1, 4)]
    
    while not rospy.is_shutdown():
        relativeGoals = []
        for i in range(len(goals)):
            # relative goals
            relativeGoals.append((goals[i][0] - curentGPSPos[0], goals[i][1] - curentGPSPos[1]))
        
        goal = goals[currentGoal]
        
        # write some code to get heading from current position to current goal
        # and set the speeds accordingly, also pass them to a topic that isnt
        # cmd_vel so that another node can do the final publishing to cmd_vel
        msg.linear.x = 0
        msg.linear.y = 0
        msg.linear.z = 0
        msg.angular.x = 0
        msg.angular.y = 0
        msg.angular.z = 0
        
        pub.publish(msg)
        rate.sleep()

if __name__ == '__main__':
    try:
        GPSTravel()
    except rospy.ROSInterruptException:
        pass
'''

'''
# Node example class.
class GPSTravel():
    # Must have __init__(self) function for a class, similar to a C++ class constructor.
    def __init__(self):
        # Get the ~private namespace parameters from command line or launch file.
        topic = rospy.get_param('~topic', 'RosAria/cmd_vel')
        rospy.loginfo('topic = %s', topic)
        # Create a dynamic reconfigure server.
        # Create a publisher for our custom message.
        pub = rospy.Publisher(topic, Twist, queue_size=10)
        # Set the message to publish as our custom message.
        msg = Twist()
        # Initialize message variables.
        msg.linear.x = 1
        msg.linear.y = 0
        msg.linear.z = 0
        msg.angular.x = 0
        msg.angular.y = 0
        msg.angular.z = 0

        # Main while loop.
        while not rospy.is_shutdown():
            # Fill in custom message variables with values from dynamic reconfigure server.
#            msg.linear = self.linear
#            msg.angular = self.angular
            # Publish our custom message.
            pub.publish(msg)
            # Sleep for a while before publishing new messages. Division is so rate != period.

            rospy.sleep(1.0)

#    # Create a callback function for the dynamic reconfigure server.
#    def reconfigure(self, config, level):
#        # Fill in local variables with values received from dynamic reconfigure clients (typically the GUI).
#        self.linear = config["linear"]
#        self.angular = config["angular"]
#        # Return the new variables.
#        return config

# Main function.
if __name__ == '__main__':
    # Initialize the node and name it.
    rospy.init_node('GPSTravel')
    # Go to class functions that do all the heavy lifting. Do error checking.
    try:
        ne = GPSTravel()
    except rospy.ROSInterruptException: pass
'''

