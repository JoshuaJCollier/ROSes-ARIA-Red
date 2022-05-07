# AUTO4508-Project
Github repo for code compilation to operate Pioneer Robot. 

To connect to bot:
Join Wi-Fi
- name: Stealth-2g
- pass: Magic2010

SSH into robot
- ssh netipc@192.168.2.**
- use password netipc

Set up catkin in folder you are working in

For ROSDepthAI
- follow guides online
- pip uninstall PyQt5
- if pip uninstall doesnt work, pip install PyQt5 and then uninstall (it tells you how to do it somewhere)

For ROSAria
- git clone https://github.com/reedhedges/AriaCoda
- cd AriaCoda
- make
- follow guides online

For ROS GPS
- sudo apt-get install ros-noetic-nmea-navsat-driver

After installing nodes
- catkin_make
