#!/bin/zsh

cd ~/
source /opt/ros/melodic/setup.zsh
mkdir -p ~/catkin_ws/src
cd ~/catkin_ws/
catkin_make
source devel/setup.bash
cd ~/catkin_ws/src
catkin_create_pkg racecar std_msgs rospy roscpp
cd ~/catkin_ws
catkin_make
. ~/catkin_ws/devel/setup.zsh
roscd racecar
mkdir scripts
cd scripts
cp ~/ECE3432/HW5/talker.py ~/catkin_ws/src/racecar/scripts
#wget https://raw.github.com/ros/ros_tutorials/kinetic-devel/rospy_tutorials/001_talker_listener/talker.py
chmod +x talker.py
roscd racecar/scripts/
#wget https://raw.github.com/ros/ros_tutorials/kinetic-devel/rospy_tutorials/001_talker_listener/listener.py
cp ~/ECE3432/HW5/listener.py ~/catkin_ws/src/racecar/scripts
chmod +x listener.py
cd ~/catkin_ws
catkin_make
