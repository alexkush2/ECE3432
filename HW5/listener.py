#!/usr/bin/env python

## Simple talker demo that listens to std_msgs/Strings published 
## to the 'chatter' topic

import rospy
from std_msgs.msg import Float32

def callbackSteer(data):
    rospy.loginfo(rospy.get_caller_id() + 'I heard steer %f', data.data)

def callbackThrottle(data):
    rospy.loginfo(rospy.get_caller_id() + 'I heard throttle %f', data.data)

def listener():

    # In ROS, nodes are uniquely named. If two nodes with the same
    # name are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'listener' node so that multiple listeners can
    # run simultaneously.
    rospy.init_node('listener', anonymous=True)

    rospy.Subscriber('steer', Float32, callbackSteer)
    rospy.Subscriber('throttle', Float32, callbackThrottle)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    listener()
