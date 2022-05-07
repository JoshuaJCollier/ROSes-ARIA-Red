# AUTO4508-Project Group 4
Github repo for code compilation to operate Pioneer Robot. Below are instructions for connecting to the bot and installing nodes, as well as compiling and running.

# To connect to bot
Join Wi-Fi
- Name: Stealth-2G
- Pass: Magic2010

SSH into robot
```
ssh netipc@192.168.2.** (156 for R5 currently)
```
- Pass: netipc

# To install nodes
Set up catkin in folder you are working in
- Follow steps on this http://old.roblab.org/courses/mobrob/project/general/Pioneer-Project-Powerpoint.pdf

For Camera: ROSDepthAI
- https://github.com/luxonis/depthai-ros follow guides online
- pip uninstall PyQt5
- If pip uninstall doesnt work, pip install PyQt5 and then uninstall (it tells you how to do it somewhere)

For Motors & Battery: ROSAria
- http://wiki.ros.org/ROSARIA/Tutorials/How%20to%20use%20ROSARIA
```
git clone https://github.com/reedhedges/AriaCoda
cd AriaCoda
make
```
- Follow guides online

For GPS: ROS GPS
```
sudo apt-get install ros-noetic-nmea-navsat-driver
```

For Controller: ps3joy
- http://wiki.ros.org/ps3joy
- follow guide (have not tried yet)

# 
After installing new nodes
```
catkin_make
```

Code bits (to run all the nodes from install, these will be combined in a launch file)
```
roslaunch depthai_examples stereo_node.launch (not working so far I think)
```

Working with ROS
```
rosnode list
rostopic list
```

ROS GPS 
- You will need a master node
```
. devel/setup.bash
roscore 

.devel/setup.bash
rosrun nmea_navsat_driver nmea_serial_driver _port:=/dev/ttyACM0 _baud:=9600

rostopic echo fix (for output)
```
- rostopic echo fix gives data

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

Things to look at
- http://wiki.ros.org/Robots/AMR_Pioneer_Compatible possible embedded connection between GPS and ARIA
- https://answers.ros.org/question/266857/using-roslaunch-to-launch-ros-nodes/ launch file written in python
- https://automaticaddison.com/how-to-create-and-execute-ros-launch-files/ create launch file
