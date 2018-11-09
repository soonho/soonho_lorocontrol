#!/usr/bin/env python
import rospy
from nav_msgs.msg import Odometry
from pyparrot.Minidrone import Mambo



def talker():
    # Start node
    rospy.init_node('mambo_central', anonymous=True)

    # Publishers
    pub_mambo_01 = rospy.Publisher('/mambo_01/odom', Odometry, queue_size=1)
    pub_mambo_02 = rospy.Publisher('/mambo_02/odom', Odometry, queue_size=1)

    # 20Hz
    rate = rospy.Rate(20)

    # Endereços MAC dos Mambos
    bt_mac_01 = "d0:3a:de:8a:e6:37"
    bt_mac_02 = "d0:3a:82:0a:e6:21"

    # Objetos dos drones
    drone_01 = Mambo(address=bt_mac_01, use_wifi=False)
    drone_02 = Mambo(address=bt_mac_02, use_wifi=False)

    # Conectar aos drones
    success_01 = drone_01.connect(num_retries=3)
    success_02 = drone_02.connect(num_retries=3)

    if success_01 & success_02:
        # Objetos para publicar nos topicos
        data_mano_01 = Odometry()
        data_mano_02 = Odometry()

        # Main loop
        while not rospy.is_shutdown() :
            # data_mano_01.pose.pose.position.x =
            data_mano_01.twist.twist.linear.x = drone_01.sensors.speed_x
            data_mano_01.twist.twist.linear.y = drone_01.sensors.speed_y
            data_mano_01.twist.twist.linear.z = drone_01.sensors.speed_z
            data_mano_01.pose.pose.orientation.w = drone_01.sensors.get_estimated_z_orientation()
            data_mano_01.pose.pose.position.z = drone_01.sensors.altitude
            str = "string de teste"
            rospy.loginfo(str)
            pub_mambo_01.publish(str)
            pub_mambo_02.publish(str)
            rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass