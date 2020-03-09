#!/usr/bin/env python

import rospy
from std_msgs.msg import Float32

# used Float32 as datatype so that it can contain a fractional value for the dutycycle

# def callbackSteer(data):
#     rospy.loginfo(rospy.get_caller_id() + 'I heard steer %f', data.data)

# def callbackThrottle(data):
#     rospy.loginfo(rospy.get_caller_id() + 'I heard throttle %f', data.data)
def truncate(n, decimals=0):
    multiplier = 10 ** decimals
    return float(int(n * multiplier) / multiplier)

def callbackDrive(data):
    print('fuck you!')
    data = float(data.data)
    throt = float(truncate(data))/100
    steer = data-truncate(data)
    rospy.loginfo(rospy.get_caller_id() + 'I heard throttle %f, and steering %f', throt, steer)

def listener():
    print("fuck dis shit")
    rospy.init_node('listener', anonymous=True)

    # rospy.Subscriber('steer', Float32, callbackSteer)
    # rospy.Subscriber('throttle', Float32, callbackThrottle)
    rospy.Subscriber('drive', Float32, callbackDrive)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    listener()
