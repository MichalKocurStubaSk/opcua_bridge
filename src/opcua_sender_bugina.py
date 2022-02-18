#!/usr/bin/env python
#from pandas import Int64Dtype
import rospy
import numpy as np
from std_msgs.msg import Int16
from std_msgs.msg import Int32
from std_msgs.msg import Int64
from std_msgs.msg import Float64MultiArray
from opcua import Client
from opcua import ua
import math


def callback(data):
    #rospy.loginfo(rospy.get_caller_id() + "I heard %d", data.data)
    #print ("uhol rad: "+str(data.data[0])+" rychlost:"+str(data.data[1]))
    speedClient = client.get_node("ns=6;s=::AsGlobalPV:Speed_Car_ref")
    speedClient.set_value(ua.Variant([float(data.data[1])], ua.VariantType.Float))
    
    
    brakeClient = client.get_node("ns=6;s=::AsGlobalPV:BrakeLevel")
    brakeClient.set_value(ua.Variant([np.int16(0)], ua.VariantType.Int16))

    fiClient = client.get_node("ns=6;s=::AsGlobalPV:Fi_Volant_ref")
    fiClient.set_value(ua.Variant([float((data.data[0]))], ua.VariantType.Float))

    timeClient = client.get_node("ns=6;s=::AsGlobalPV:Cas_ROS")
    timeClient.set_value(ua.Variant([np.int32(rospy.get_rostime().nsecs)], ua.VariantType.Int32))

    
def listener():

    # In ROS, nodes are uniquely named. If two nodes with the same
    # name are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'listener' node so that multiple listeners can
    # run simultaneously.
    rospy.init_node('listener', anonymous=True)

    rospy.Subscriber("ref_speed_steer", Float64MultiArray, callback)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    client = Client("opc.tcp://192.168.1.2:4840/")
    try:
        client.connect()
        root = client.get_root_node()
        print("Objects node is: ", root)


        listener()
    except rospy.ROSInterruptException:
        pass
    finally:
        client.disconnect()
