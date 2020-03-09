#!/usr/bin/env python

import rospy
from sensor_msgs.msg import Joy
from rpiHAT import ServoNT
import time

# setup servos
s=ServoNT(channel=1, freq=94.5)
t=ServoNT(channel=2, freq=94.5)

def callback(data):
    # log entire thing heard
    rospy.loginfo(rospy.get_caller_id() + ' I heard %s', data.axes)
    
    # duty cycle in range [0.10, 0.20]
    # scale steering value to dutycycle, then set and log it
    steer = (data.axes[0]*.05)+.15
    s.pulse(steer)
    rospy.loginfo(rospy.get_caller_id() + ' steering: %s, duty cycle %f', data.axes[0], steer)

    # scale throttle value to dutycycle, then set and log it
    throttle = (data.axes[4]*.05)+.15
    t.pulse(throttle)
    rospy.loginfo(rospy.get_caller_id() + ' throttle: %s, duty cycle %f', data.axes[1], throttle)

def listener():
    # start node and subscribe to joy
    rospy.init_node('listener', anonymous=True)
    rospy.Subscriber('joy', Joy, callback)

    # zero servo positions
    s.pulse(0.15)
    t.pulse(0.15)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    listener()
