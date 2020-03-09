#!/usr/bin/env python

import rospy
from sensor_msgs.msg import Joy
from rpiHAT import ServoNT
import time

s=ServoNT(channel=1, freq=94.5)
t=ServoNT(channel=2, freq=94.5)

def callback(data):
    rospy.loginfo(rospy.get_caller_id() + ' I heard %s', data.axes)
    # duty cycle in range [0.10, 0.20]

    steer = (data.axes[1]*.05)+.15
    s.pulse(steer)
    rospy.loginfo(rospy.get_caller_id() + ' steering: %s, duty cycle %f', data.axes[0], steer)

    throttle = (data.axes[0]*.05)+.15
    t.pulse(throttle)
    rospy.loginfo(rospy.get_caller_id() + ' throttle: %s, duty cycle %f', data.axes[1], throttle)

def listener():
    rospy.init_node('listener', anonymous=True)

    rospy.Subscriber('joy', Joy, callback)

    s.pulse(0.15)
    t.pulse(0.15)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    listener()
