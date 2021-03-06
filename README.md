# AUTO4508-Project Group 4
Github repo for code compilation to operate Pioneer Robot. Below are instructions for connecting to the bot and installing nodes, as well as compiling and running.

To Start Code:
- Download Group4Proj code onto robot
- "cd /path/to/catkin_ws" 
- "find ./ -type f -exec touch {} +" in terminal
- "catkin_make" in terminal
- "roslaunch group4.launch" to run

Tasks to Complete:
1. ~~Drive the robot along a path, specified through a number of given GPS waypoints. The robot has to visit each waypoint before returning to its starting position.~~
2. ~~Each waypoint is marked by a cone. Whenever a waypoint has been reached (with reasonable accuracy), the robot must take a photo of the cone and head towards the next waypoint.~~
3. ~~At each waypoint, a bucket will be in the vicinity. Identify it and take a picture and record its distance.~~
4. After finishing the course, print cone and bucket pictures and bucket distances to screen.
5. ~~Record the path and display it graphically.~~
6. ~~Implement UI with graphic and text to display internal state and intended actions (print mindState and explain what it does).~~
7. ~~Avoid collision with cones and obstacles including moving and stationary.~~
8. ~~For safety reasons, implement bluetooth with auto and manual~~

#
Code that written exclusively by us is found at the following paths and is attatched in a seperate file:
- AUTO4508-Project\Group4Proj\catkin_ws\src\megamind\scripts\MegaMind.py
- AUTO4508-Project\Group4Proj\catkin_ws\src\megamind\msg\Decision.msg
- AUTO4508-Project\Group4Proj\catkin_ws\src\gps_travel\scripts\GPSTravel.py
- AUTO4508-Project\Group4Proj\catkin_ws\src\take_photo\scripts\TakePhoto.py
- AUTO4508-Project\Group4Proj\catkin_ws\src\take_photo\scripts\ImagePublisher.py
- AUTO4508-Project\Group4Proj\catkin_ws\src\object_tracker\scripts\ObjectTracker.py
- AUTO4508-Project\Group4Proj\catkin_ws\src\object_tracker\msg\Objects.msg
- AUTO4508-Project\Group4Proj\catkin_ws\src\gui\scripts\GUI.py
- AUTO4508-Project\Group4Proj\catkin_ws\group4.launch

#
Code editted by us:
- AUTO4508-Project\Group4Proj\catkin_ws\src\megamind\CMakeLists.txt
- AUTO4508-Project\Group4Proj\catkin_ws\src\megamind\package.xml
- AUTO4508-Project\Group4Proj\catkin_ws\src\gps_travel\CMakeLists.txt
- AUTO4508-Project\Group4Proj\catkin_ws\src\take_photo\CMakeLists.txt
- AUTO4508-Project\Group4Proj\catkin_ws\src\object_tracker\CMakeLists.txt
- AUTO4508-Project\Group4Proj\catkin_ws\src\object_tracker\package.xml
- AUTO4508-Project\Group4Proj\catkin_ws\src\gui\CMakeLists.txt

#
Submodules imported from other gits:
- AUTO4508-Project\Group4Proj\catkin_ws\src\rosaria
- AUTO4508-Project\Group4Proj\catkin_ws\src\joystick_drivers
- AUTO4508-Project\Group4Proj\catkin_ws\src\luxonis\depthai-ros
- AUTO4508-Project\Group4Proj\catkin_ws\src\luxonis\depthai-ros-examples
- AUTO4508-Project\Group4Proj\catkin_ws\AriaCoda

#
Working out for GPS Stuff:
https://boulter.com/gps/distance/?from=-31.98052883658287+115.81716552265434&to=-31.98109143766833+115.81716552265429&units=k
https://www.gps-coordinates.net/
Calcs: (31.98109143766833-31.98052883658287)/62


# To connect to bot
Join Wi-Fi
- Name: Stealth-2G
- Pass: Magic2010
#

SSH into robot
```
ssh netipc@192.168.2.** (156 for R5 currently, pass: netipc)
cd Desktop/Group4Proj/catkin
```

# To install nodes
Set up catkin in folder you are working in
- Follow steps on this http://old.roblab.org/courses/mobrob/project/general/Pioneer-Project-Powerpoint.pdf
#

For Camera: ROSDepthAI
- https://github.com/luxonis/depthai-ros follow guides online
```
pip uninstall PyQt5
```
- If pip uninstall doesnt work, pip install PyQt5 and then uninstall (it tells you how to do it somewhere)
#

For Motors & Battery: ROSAria
- http://wiki.ros.org/ROSARIA/Tutorials/How%20to%20use%20ROSARIA
```
git clone https://github.com/reedhedges/AriaCoda
cd AriaCoda
make
```
- Follow guides online
#

For GPS: ROS GPS
```
sudo apt-get install ros-noetic-nmea-navsat-driver
```
#

For Controller: ps3joy
- http://wiki.ros.org/ps3joy
- Follow guide (have not tried yet)
#

After installing new nodes
```
catkin_make
```

# To Program
This will launch ROS Master node, ROSAria node, ROS GPS node and gps_travel node
```
roslaunch group4.launch
```
#

Working with ROS
```
rosnode list
rostopic list
```
#

Things to look at
- http://wiki.ros.org/Robots/AMR_Pioneer_Compatible possible embedded connection between GPS and ARIA
- https://answers.ros.org/question/266857/using-roslaunch-to-launch-ros-nodes/ launch file written in python
- https://automaticaddison.com/how-to-create-and-execute-ros-launch-files/ create launch file
- https://github.com/rnitin/pioneer-ros/blob/master/p3dx-mobilesim/waypoint_pioneer.cpp this is the coolest
- http://library.isr.ist.utl.pt/docs/roswiki/ROSARIA(2f)Tutorials(2f)How(20)to(20)use(20)ROSARIA.html this is cool
- https://github.com/tdenewiler/node_example/blob/main/src/pytalker.py 
- http://wiki.ros.org/ROSARIA useful
- http://wiki.ros.org/ROSNodeTutorialPython
- https://stackoverflow.com/questions/40508651/writing-a-ros-node-with-both-a-publisher-and-subscriber
#

Goals for 08/05/22
- Create node to publish to /RosAria/cmd_vel topic with geometry_msgs/Twist msg -> something like this (rostopic pub -1 /RosAria/cmd_vel geometry_msgs/Twist '[0.1, 0.0, 0.0]' '[0.0, 0.0, 0.0]')
- 
# Depricated

ROS GPS 
- You will need a master node
```
. devel/setup.bash
roscore 

. devel/setup.bash
rosrun nmea_navsat_driver nmea_serial_driver _port:=/dev/ttyACM0 _baud:=9600

rostopic echo fix (for output)
```
- rostopic echo fix gives data
#

ROSAria Working
- You need 3 terminals, on each of them, run one of the following sets of code (in order)
```
. devel/setup.bash
roscore

sudo bash
. devel/setup.bash
export ROS_IP=192.168.2.156
rosrun rosaria RosAria _port:=/dev/ttyS1

. devel/setup.bash
rosrun rosaria_client interface (press 4 for teleop)
```
- These will give control over the teleop
