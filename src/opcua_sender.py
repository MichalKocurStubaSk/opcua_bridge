#!/usr/bin/env python
import rospy
from std_msgs.msg import Int16
from opcua import Client
from opcua import ua

def callback(data):
    rospy.loginfo(rospy.get_caller_id() + "I heard %d", data.data)
    var2 = client.get_node("ns=6;s=::Test_OPCUA:AnalogOut1")
    var2.set_value(ua.Variant([int(data.data)], ua.VariantType.Int16))

    
def listener():

    # In ROS, nodes are uniquely named. If two nodes with the same
    # name are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'listener' node so that multiple listeners can
    # run simultaneously.
    rospy.init_node('listener', anonymous=True)

    rospy.Subscriber("dummypub", Int16, callback)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    client = Client("opc.tcp://192.168.1.4:4840/")
    try:
        client.connect()
        root = client.get_root_node()
        print("Objects node is: ", root)


        listener()
    except rospy.ROSInterruptException:
        pass
    finally:
        client.disconnect()
