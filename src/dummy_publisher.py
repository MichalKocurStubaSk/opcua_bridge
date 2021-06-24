#!/usr/bin/env python
# license removed for brevity
import rospy
from std_msgs.msg import Int16


def talker(): 
    A1= 10000
    pub = rospy.Publisher('dummypub', Int16, queue_size=10)
    rospy.init_node('dummy', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():
	A1 = A1 + 1000
	if A1 > 20000:
		A1 = -32000
        rospy.loginfo(int(A1))
        pub.publish(int(A1))
        rate.sleep()

if __name__ == '__main__':
    
    try:
        talker()
    except rospy.ROSInterruptException:
        pass

