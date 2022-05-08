#!/usr/bin/env python

# Import required Python code.
import rospy
import sys

# Import custom message data and dynamic reconfigure variables.
from geometry_msgs.msg import Twist

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
