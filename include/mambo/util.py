import random
def getName():
    return "​your_name​"
def getStatus():
    return random.choice(["happy","awesome"])

# import rospy
# from std_msgs.msg import String
#
#
# def talker():
#     # Publishers
#     pub_mambo_01 = rospy.Publisher('/mambo_01/odom', String, queue_size=1)
#     pub_mambo_02 = rospy.Publisher('/mambo_02/odom', String, queue_size=1)
#
#     # Start node
#     rospy.init_node('mambo_central', anonymous=True)
#
#     # 20Hz
#     rate = rospy.Rate(20)
#
#     # Main loop
#     while not rospy.is_shutdown() :
#         str = "string de teste"
#         rospy.loginfo(str)
#         pub_mambo_01.publish(str)
#         pub_mambo_02.publish(str)
#         rate.sleep()
#
# if __name__ == '__main__':
#     try:
#         talker()
#     except rospy.ROSInterruptException:
#         pass