#!/usr/bin/env python
import sys
sys.path.insert(0, "..")

import rospy
from std_msgs.msg import Int16
from opcua import Client
from opcua import ua

def talker():
    pub = rospy.Publisher('pilapub', Int16, queue_size=10)
    rospy.init_node('pila', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():
	var = client.get_node("ns=6;s=::Test_OPCUA:Pila")
	pilaValue = var.get_value() # get value of node as a python builtin
        #hello_str = "hello world %s" % rospy.get_time()
        rospy.loginfo(pilaValue)
        pub.publish(pilaValue)
        rate.sleep()





if __name__ == "__main__":

    client = Client("opc.tcp://192.168.1.4:4840/")
    # client = Client("opc.tcp://admin@localhost:4840/freeopcua/server/") #connect using a user
    try:
        client.connect()

        # Client has a few methods to get proxy to UA nodes that should always be in address space such as Root or Objects
        root = client.get_root_node()
        print("Objects node is: ", root)

        # Node objects have methods to read and write node attributes as well as browse or populate address space
        print("Children of root are: ", root.get_children())

        # get a specific node knowing its node id
        #var = client.get_node(ua.NodeId(1002, 2))
	#while(1):
	       # var = client.get_node("ns=6;s=::Test_OPCUA:Pila")
        	#var.get_data_value() # get value of node as a DataValue object
        	#var.get_value() # get value of node as a python builtin
	#print("vaaaar = " + str(var))
		#print("vaaaalluuuee = " + str(var.get_value()))

        #var2 = client.get_node("ns=6;s=::Test_OPCUA:AnalogOut1")
	#print("vaaaar222 = " + str(var2))
        #var2.set_value(ua.Variant([32000], ua.VariantType.Int16)) #set node value using explicit data type
        #var.set_value(3.9) # set node value using implicit data type

        # Now getting a variable node using its browse path
        #myvar = root.get_child(["6:Test_OPCUA:Pila"])
        #obj = root.get_child(["0:Objects", "2:MyObject"])
        #print("myvar is: ", myvar)
        #print("myobj is: ", obj)

        # Stacked myvar access
  #      print("myvar is: ", root.get_children()[0].get_children()[0].get_variables()[6].get_value())
	
	talker()
    except rospy.ROSInterruptException:
        pass
    finally:
        client.disconnect()

