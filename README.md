# AUTO4508-Project
Github repo for code compilation to operate Pioneer Robot. 

To connect to bot:
Join Wi-Fi
- name: Stealth-2g
- pass: Magic2010

SSH into robot
```
ssh netipc@192.168.2.** (156 for R5 currently)
```
- use password netipc

Set up catkin in folder you are working in
Follow steps on this http://old.roblab.org/courses/mobrob/project/general/Pioneer-Project-Powerpoint.pdf

For Camera: ROSDepthAI
- https://github.com/luxonis/depthai-ros follow guides online
- pip uninstall PyQt5
- if pip uninstall doesnt work, pip install PyQt5 and then uninstall (it tells you how to do it somewhere)

For Motors & Battery: ROSAria
- http://wiki.ros.org/ROSARIA/Tutorials/How%20to%20use%20ROSARIA
```
git clone https://github.com/reedhedges/AriaCoda
cd AriaCoda
make
```
- follow guides online

For GPS: ROS GPS
```
sudo apt-get install ros-noetic-nmea-navsat-driver
```

For Controller: ps3joy
- http://wiki.ros.org/ps3joy
- follow guide

After installing nodes
```
catkin_make
```

Code bits (to run all the nodes from install, these will be combined in a launch file)
```
rosrun rosaria RosAria _port:=/dev/ttyS1
rosrun rosaria_client interface
roslaunch depthai_examples stereo_node.launch
rosrun nmea_navsat_driver nmea_serial_driver
_port:=/dev/ttyACM0 _baud:=9600
```
