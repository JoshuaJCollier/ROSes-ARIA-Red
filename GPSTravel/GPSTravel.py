#!/usr/bin/env python

# Import required Python code.
import roslib
roslib.load_manifest('traveller')
import rospy
import sys


# Import custom message data and dynamic reconfigure variables.
from geometry_msgs.Twist import travel

# Node example class.
class GPSTravel():
    # Must have __init__(self) function for a class, similar to a C++ class constructor.
    def __init__(self):
        # Get the ~private namespace parameters from command line or launch file.
        topic = rospy.get_param('~topic', 'chatter')
        rospy.loginfo('topic = %s', topic)
        # Create a dynamic reconfigure server.
        # Create a publisher for our custom message.
        pub = rospy.Publisher(topic, travel)
        # Set the message to publish as our custom message.
        msg = travel()
        # Initialize message variables.
        msg.a = 1
        msg.b = 2
        msg.message = 'joe biden'
        # Main while loop.
        while not rospy.is_shutdown():
            # Fill in custom message variables with values from dynamic reconfigure server.
            msg.message = self.message
            msg.a = self.a
            msg.b = self.b
            # Publish our custom message.
            pub.publish(msg)
            # Sleep for a while before publishing new messages. Division is so rate != period.

            rospy.sleep(1.0)

    # Create a callback function for the dynamic reconfigure server.
    def reconfigure(self, config, level):
        # Fill in local variables with values received from dynamic reconfigure clients (typically the GUI).
        self.message = config["message"]
        self.a = config["a"]
        self.b = config["b"]
        # Return the new variables.
        return config

# Main function.
if __name__ == '__main__':
    # Initialize the node and name it.
    rospy.init_node('pytalker')
    # Go to class functions that do all the heavy lifting. Do error checking.
    try:
        ne = GPSTravel()
    except rospy.ROSInterruptException: pass
