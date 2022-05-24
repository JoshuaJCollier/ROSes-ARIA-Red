#!/usr/bin/env python
import rospy
import sys
import time
import math

# Predefined message data
from geometry_msgs.msg import Twist
from megamind.msg import Decision
from object_detect.msg import Objects
from sensor_msgs.msg import NavSatFix, Joy

currentGPSPos = (0, 0)
start = 0
gps_travel_cmd_vel_msg = Twist()
object_detect = Objects()
controller_joy_in = Joy()
mindState = 0
decision = Decision()
#msg = Twist()

firstPos = []
secondPos = []
startHeadingTime = 0
foundHeading = False

megaMindStarted = False
goalIncreased = False

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
    
    return gpsPoints[index]

def gpsPosCallback(data):
    global currentGPSPos
    currentGPSPos = (data.latitude, data.longitude)

def objectDetectSubCallback(data):
    global object_detect
    object_detect = data
    
def controllerSubCallback(data):
    global controller_joy_in, megaMindStarted
    controller_joy_in = data
    if (not megaMindStarted):
        megaMindStarted = True
    
def gpsTravelSubCallback(data):
    global megaMindStarted, gps_travel_cmd_vel_msg
    gps_travel_cmd_vel_msg = data

def publisherCallback(event):
    global megaMindStarted, goalIncreased, cmdVelPub, megaPub, currentGPSPos, gps_travel_cmd_vel_msg, object_detect, controller_joy_in, mindState, decision, startHeadingTime, foundHeading, firstPos, secondPos
    # Mind State Definitions: 0 -> Goal Seeking, 1 -> Object Avoidance, 2 -> Cone Finding, 3 -> Cone Picture, 4 -> Bucket Picture
    #goals = [(-31.9805773505506, 115.8171660979887), (-31.98038731577529, 115.8171782781675), (-31.98017884452402, 115.8171702857572), (-31.98082891705035, 115.8171314540043), (-31.98081842250873, 115.8174656945906), (-31.98081842250873, 115.8174656945906), (-31.98041252344407, 115.8175647311226), (-31.98052211397503, 115.8197862220968)]
    goals = [(-31.9808289171, 115.817131454), (-31.9803873158, 115.817178278), (-31.9804125234, 115.817564731), (-31.9801788445, 115.817170286), (-31.9808289171, 115.817131454)]
    relativeGoals = []
    for i in range(len(goals)):
        # relative goals
        relativeGoals.append((goals[i][0] - currentGPSPos[0], goals[i][1] - currentGPSPos[1]))
    
    goal = relativeGoals[decision.currentGoal]
    
    msg = Twist()
    if (megaMindStarted):
        # 0 -> Goal Seeking
        if (controller_joy_in.buttons[0] == 1):
            if (mindState == 0): # ------------- GOAL SEEKING -------------
                # FIRST CALCULATE THE HEADING
                goalIncreased = False
                if (len(firstPos) < 10):
                    decision.gps_travel_on = 0
                    firstPos.append(currentGPSPos)
                    startHeadingTime = time.perf_counter()
                elif (len(firstPos) == 10) and (time.perf_counter() < (startHeadingTime+4)) and (not foundHeading):
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
                
                # HEADING IS SET, USE GPS TRAVEL TO MOVE
                if decision.gps_travel_on == 1:
                    msg = gps_travel_cmd_vel_msg

                    if math.sqrt(math.pow(goal[1], 2) + math.pow(goal[0],2)) < 0.00002 and msg.linear.x == 0:
                        mindState = 2
		# if distance to goal is small or we see the cone clearly or there is an obstacle, then 
                # decision.currentGoal = 1 or 2

            elif (mindState == 1): # ------------- OBJECT AVOIDANCE -------------
                # HARD CODED OBSTACLE AVOIDANCE
                if object_detect.obstacle == 0 and object_detect.obstacleDist < 1:
                    if (object_detect.time + math.pi*0.5 > time.perf_counter()):
                        msg.linear.x = 0
                        msg.angular.z = 0.5
                    elif (object_detect.time + math.pi*0.5 + 1.41 > time.perf_counter()):
                        msg.linear.x = 1
                        msg.angular.z = 0
                    elif (object_detect.time + math.pi*1.5 + 1.41 > time.perf_counter()):
                        msg.linear.x = 0
                        msg.angular.z = -0.5
                    elif (object_detect.time + math.pi*1.5 + 2.82 > time.perf_counter()):
                        msg.linear.x = 1
                        msg.angular.z = 0
                    elif (object_detect.time + math.pi*2 + 2.82 > time.perf_counter()):
                        msg.linear.x = 0
                        msg.angular.z = 0.5
                    else:
                        msg.linear.x = 0
                        msg.angular.z = 0
                        mindState = 0
                # MOVING OBSTACLE SHOULD BE AVOIDED

                # ONCE OBSTACLE IS GONE RETURN TO GOAL SEEKING
                if object_avoid_cmd_vel_msg.cone:
                    mindState = 2
                    
            elif (mindState == 2): # ------------- CONE FINDING -------------
                # RESETTING SUCH THAT WE CAN GOAL SEEK FOR THE NEXT GOAL AFTER PICTURE AND STUFF
                if not goalIncreased:
                    goalIncreased = True
                    decision.currentGoal += 1
                    mindState = 3
                decision.gps_travel_on = 0
                firstPos = []
                secondPos = []
            
            elif (mindState == 3): # ------------- CONE PICTURE -------------
                # take picture somehow
                mindState = 4
            
            elif (mindState == 4): # ------------- BUCKET PICTURE -------------
                # take picture again but bucket this time
                if (object_detect.bucket == 1):
                    mindState = 0
            
            # read from megaPub, might be best to publish mindState and stuff
            # can also at some point use a matplotlib program to plot path
            # for distance need to use depth cloud, for picture need to use OAK
            # for objects we need distance and if its moving, aside from all
            # this its looking good I think
            decision.mindState = mindState
            megaPub.publish(decision)
        elif (controller_joy_in.buttons[1] == 1):
            print("Manual")
            # remap controller to direct cmd_vel controls
            msg.linear.x = controller_joy_in.buttons[13] - controller_joy_in.buttons[14] #controller_joy_in.axes[1] # Up/Down of Left Stick
            msg.angular.z = controller_joy_in.buttons[15] - controller_joy_in.buttons[16] #controller_joy_in.axes[3] # Left/Right of Right Stick
            dec2 = Decision()
            dec2.mindState = 5
            megaPub.publish(dec2)
        else:
            msg.linear.x = 0
            msg.angular.z = 0
        cmdVelPub.publish(msg)

def main():
    global start, mindState, goal
    rospy.init_node('GPSTravel', anonymous=True)
    fixSub = rospy.get_param('~topic', 'fix')
    gpsTravelSub = rospy.get_param('~topic', 'gps_travel_cmd_vel')
    objDetectSub = rospy.get_param('~topic', 'object_detect')
    controllerSub = rospy.get_param('~topic', 'joy')
    rospy.Subscriber(fixSub, NavSatFix, gpsPosCallback)
    rospy.Subscriber(gpsTravelSub, Twist, gpsTravelSubCallback)
    rospy.Subscriber(objDetectSub, Objects, objectDetectSubCallback)
    rospy.Subscriber(controllerSub, Joy, controllerSubCallback)
    timer = rospy.Timer(rospy.Duration(0.2), publisherCallback)
    start = time.perf_counter()
    decision.currentGoal = 0
    # IN ORDER TO START PROGRAM, MIND STATE MUST BE SET TO 0
    mindState = 0
    
    rospy.spin()
    timer.shutdown()

if __name__ == '__main__':
    print("Running")
    main()



