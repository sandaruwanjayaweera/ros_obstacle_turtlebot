# Copyright 2016 Open Source Robotics Foundation, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import rclpy
from rclpy.node import Node

from std_msgs.msg import String
from tutorial_interfaces.msg import CAM
import math

def enu_to_gps(x, y, z, lat1, long1, alt1):
    print("Beginning data processing2...")
    r = 6378388                                         # earth radius in m (http://www.cs.jyu.fi/el/summerschool/materials/lbs/lbs_integration/tsld026.htm)
    long2   = x*360*10**7/(2*math.pi*r) + long1
    lat2    = y*360*10**7/(2*math.pi*r) + lat1
    alt2    = (z + alt1)*10				# m to cm
    print("Data processing finished2." + str(long2) + "," + str(lat2) + "," + str(alt2))
    print("Data processing finished2." + str(round(long2,1)) + "," + str(round(lat2,1)) + "," + str(round(alt2,1)))
    return lat2,long2,alt2

class MinimalPublisher(Node):
    x 		= 0
    y 		= 0
    z 		= 0
    lattitude 	= 0
    longitude  	= 0
    altitude  	= 0

    def __init__(self):
        super().__init__('minimal_publisher')
        self.publisher_ = self.create_publisher(CAM, 'CAM', 10)     # CHANGE
        timer_period = 0.0005
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.i = 0

    def timer_callback(self):
#        f = open("/home/san/python/fake_gps.txt", "w")
        self.x += 0.1
        self.y += 0.1
        self.z  += 0.1
        self.lattitude,self.longitude,self.altitude = enu_to_gps(self.x, self.y, self.z, 0, 0, 0)
#        f.write(str(self.lattitude) + "," + str(self.longitude) + "," + str(self.altitude))
#        f.close()

#        with open("/home/san/python/fake_gps.txt", "r") as file:
#                first_line = file.readline()
#                for last_line in file:
#                     pass
#        fake_gps = first_line.split(",")
#        print(first_line)

        msg = CAM()                                           # CHANGE
        msg.pdu_proto_version 		= 4                           			# CHANGE
        msg.pdu_message_id 		= 2                                      	# CAM 2, DENM 1
        msg.pdu_src_station_id 		= 101                                      	# srcStationID

        msg.bc_station_type 				= 1                           			# CHANGE
        msg.bc_ref_pos_lattitude 			= int(round(self.lattitude))                                      	# CHANGE
        msg.bc_ref_pos_longitude 			= int(round(self.longitude))                                      	# CHANGE
#        msg.bc_ref_pos_lattitude 			= int(fake_gps[0])                                      	# CHANGE
#        msg.bc_ref_pos_longitude 			= int(fake_gps[1])                                      	# CHANGE
        msg.bc_ref_pos_conf_ellipse_semi_major 		= 4                           			# CHANGE
        msg.bc_ref_pos_conf_ellipse_semi_minor 		= 5                                      	# CHANGE
        msg.bc_ref_pos_altitude_heading 		= 6                                      	# CHANGE
        msg.bc_ref_pos_altitude_val 			= int(round(self.altitude))                           			# CHANGE
#        msg.bc_ref_pos_altitude_val 			= int(fake_gps[2])                           			# CHANGE
        msg.bc_ref_pos_altitude_conf 			= 8                                      	# CHANGE

        msg.hf_heading_val 				= 1                           			# CHANGE
        msg.hf_heading_conf 				= 2                                      	# CHANGE
        msg.hf_vertical_heading 			= 3                                      	# CHANGE
        msg.hf_speed_val		 		= 4                           			# CHANGE
        msg.hf_speed_conf		 		= 5                                      	# CHANGE
        msg.hf_drive_dir_heading_val	 		= 6                                      	# CHANGE
        msg.hf_drive_dir_heading_conf 			= 7                           			# CHANGE
        msg.hf_drive_dir_vertical_heading 		= 8                                      	# CHANGE
        msg.hf_v_len_val 				= 9                           			# CHANGE
        msg.hf_v_len_conf	 			= 10                                      	# CHANGE
        msg.hf_v_width		 			= 11                                      	# CHANGE
        msg.hf_v_height			 		= 12                           			# CHANGE
        msg.hf_long_acc_val		 		= 13                                      	# CHANGE
        msg.hf_long_acc_conf		 		= 14                                      	# CHANGE
        msg.hf_curv_val		 			= 15                           			# CHANGE
        msg.hf_curv_conf	 			= 16                                      	# CHANGE
        msg.hf_curv_cal_mod 				= 17                           			# CHANGE
        msg.hf_yaw_r_val	 			= 18                                      	# CHANGE
        msg.hf_yaw_r_conf	 			= 19                                      	# CHANGE
        msg.hf_lat_acc_val		 		= 20                           			# CHANGE
        msg.hf_lat_acc_conf		 		= 21                                      	# CHANGE
        msg.hf_vertical_acc_val		 		= 22                                      	# CHANGE
        msg.hf_vertical_acc_conf 			= 23                           			# CHANGE

        self.publisher_.publish(msg)
        print('Publishing: \
					\n x - "%f",\
					\n y - "%f",\
					\n z - "%f",\
					' 
					% (	self.x, 
						self.y, 
						self.z
						) )  # CHANGE
#        print('Publishing: \
#					\n proto_version - "%d",\
#					\n message_id - "%d",\
#					\n src_station_id - "%d",\
#					\n \
#					\n bc_station_type - "%d",\
#					\n bc_ref_pos_lattitude - "%d",\
#					\n bc_ref_pos_longitude - "%d",\
#					\n bc_ref_pos_conf_ellipse_semi_major - "%d",\
#					\n bc_ref_pos_conf_ellipse_semi_minor - "%d",\
#					\n bc_ref_pos_altitude_heading - "%d",\
#					\n bc_ref_pos_altitude_val - "%d",\
#					\n bc_ref_pos_altitude_conf - "%d",\
#					\n \
#					\n hf_heading_val - "%d",\
#					\n hf_heading_conf - "%d",\
#					\n hf_vertical_heading - "%d",\
#					\n hf_speed_val - "%d",\
#					\n hf_speed_conf - "%d",\
#					\n hf_drive_dir_heading_val - "%d",\
#					\n hf_drive_dir_heading_conf - "%d",\
#					\n hf_drive_dir_vertical_heading - "%d",\
#					\n hf_v_len_val - "%d",\
#					\n hf_v_len_conf - "%d",\
#					\n hf_v_width - "%d",\
#					\n hf_v_height - "%d",\
#					\n hf_long_acc_val - "%d",\
#					\n hf_long_acc_conf - "%d",\
#					\n hf_curv_val - "%d",\
#					\n hf_curv_conf - "%d",\
#					\n hf_curv_cal_mod - "%d",\
#					\n hf_yaw_r_val - "%d",\
#					\n hf_yaw_r_conf - "%d",\
#					\n hf_lat_acc_val - "%d",\
#					\n hf_lat_acc_conf - "%d",\
#					\n hf_vertical_acc_val - "%d",\
#					\n hf_vertical_acc_conf - "%d",\
#					\n ----------------------------------------------------- \
#					' 
#					% (	msg.pdu_proto_version, 
#						msg.pdu_message_id, 
#						msg.pdu_src_station_id,
#
#						msg.bc_station_type, 
#						msg.bc_ref_pos_lattitude,
#						msg.bc_ref_pos_longitude, 
#						msg.bc_ref_pos_conf_ellipse_semi_major,
#						msg.bc_ref_pos_conf_ellipse_semi_minor, 
#						msg.bc_ref_pos_altitude_heading,
#						msg.bc_ref_pos_altitude_val, 
#						msg.bc_ref_pos_altitude_conf,
#
#						msg.hf_heading_val, 
#						msg.hf_heading_conf,
#						msg.hf_vertical_heading, 
#						msg.hf_speed_val,
#						msg.hf_speed_conf, 
#						msg.hf_drive_dir_heading_val,
#						msg.hf_drive_dir_heading_conf, 
#						msg.hf_drive_dir_vertical_heading,
#						msg.hf_v_len_val, 
#						msg.hf_v_len_conf,
#						msg.hf_v_width, 
#						msg.hf_v_height,
#						msg.hf_long_acc_val, 
#						msg.hf_long_acc_conf,
#						msg.hf_curv_val, 
#						msg.hf_curv_conf,
#						msg.hf_curv_cal_mod, 
#						msg.hf_yaw_r_val,
#						msg.hf_yaw_r_conf, 
#						msg.hf_lat_acc_val,
#						msg.hf_lat_acc_conf, 
#						msg.hf_vertical_acc_val,
#						msg.hf_vertical_acc_conf
#						) )  # CHANGE
#        self.get_logger().info('Publishing: \
#					\n proto_version - "%d",\
#					\n message_id - "%d",\
#					\n src_station_id - "%d",\
#					\n \
#					\n bc_station_type - "%d",\
#					\n bc_ref_pos_lattitude - "%d",\
#					\n bc_ref_pos_longitude - "%d",\
#					\n bc_ref_pos_conf_ellipse_semi_major - "%d",\
#					\n bc_ref_pos_conf_ellipse_semi_minor - "%d",\
#					\n bc_ref_pos_altitude_heading - "%d",\
#					\n bc_ref_pos_altitude_val - "%d",\
#					\n bc_ref_pos_altitude_conf - "%d",\
#					\n \
#					\n hf_heading_val - "%d",\
#					\n hf_heading_conf - "%d",\
#					\n hf_vertical_heading - "%d",\
#					\n hf_speed_val - "%d",\
#					\n hf_speed_conf - "%d",\
#					\n hf_drive_dir_heading_val - "%d",\
#					\n hf_drive_dir_heading_conf - "%d",\
#					\n hf_drive_dir_vertical_heading - "%d",\
#					\n hf_v_len_val - "%d",\
#					\n hf_v_len_conf - "%d",\
#					\n hf_v_width - "%d",\
#					\n hf_v_height - "%d",\
#					\n hf_long_acc_val - "%d",\
#					\n hf_long_acc_conf - "%d",\
#					\n hf_curv_val - "%d",\
#					\n hf_curv_conf - "%d",\
#					\n hf_curv_cal_mod - "%d",\
#					\n hf_yaw_r_val - "%d",\
#					\n hf_yaw_r_conf - "%d",\
#					\n hf_lat_acc_val - "%d",\
#					\n hf_lat_acc_conf - "%d",\
#					\n hf_vertical_acc_val - "%d",\
#					\n hf_vertical_acc_conf - "%d",\
#					\n ----------------------------------------------------- \
#					' 
#					% (	msg.pdu_proto_version, 
#						msg.pdu_message_id, 
#						msg.pdu_src_station_id,
#
#						msg.bc_station_type, 
#						msg.bc_ref_pos_lattitude,
#						msg.bc_ref_pos_longitude, 
#						msg.bc_ref_pos_conf_ellipse_semi_major,
#						msg.bc_ref_pos_conf_ellipse_semi_minor, 
#						msg.bc_ref_pos_altitude_heading,
#						msg.bc_ref_pos_altitude_val, 
#						msg.bc_ref_pos_altitude_conf,
#
#						msg.hf_heading_val, 
#						msg.hf_heading_conf,
#						msg.hf_vertical_heading, 
#						msg.hf_speed_val,
#						msg.hf_speed_conf, 
#						msg.hf_drive_dir_heading_val,
#						msg.hf_drive_dir_heading_conf, 
#						msg.hf_drive_dir_vertical_heading,
#						msg.hf_v_len_val, 
#						msg.hf_v_len_conf,
#						msg.hf_v_width, 
#						msg.hf_v_height,
#						msg.hf_long_acc_val, 
#						msg.hf_long_acc_conf,
#						msg.hf_curv_val, 
#						msg.hf_curv_conf,
#						msg.hf_curv_cal_mod, 
#						msg.hf_yaw_r_val,
#						msg.hf_yaw_r_conf, 
#						msg.hf_lat_acc_val,
#						msg.hf_lat_acc_conf, 
#						msg.hf_vertical_acc_val,
#						msg.hf_vertical_acc_conf
#						) )  # CHANGE


def main(args=None):
    rclpy.init(args=args)

    minimal_publisher = MinimalPublisher()

    rclpy.spin(minimal_publisher)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    minimal_publisher.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
