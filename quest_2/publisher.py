#!/usr/bin/env python3
import rospy
from std_msgs.msg import String
import datetime

def talker():
    pub = rospy.Publisher('/datetime', String, queue_size=10)
    rospy.init_node('time_publisher', anonymous=True)
    rate = rospy.Rate(1) # 1Hz

    while not rospy.is_shutdown():
        now = datetime.datetime.now()
        time_str = now.strftime("%Y.%m.%d_%H:%M:%S")
        rospy.loginfo(time_str)
        pub.publish(time_str)
        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
