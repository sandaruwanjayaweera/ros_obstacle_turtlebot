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
from tutorial_interfaces.msg import DENMCW

class MinimalPublisher(Node):

    def __init__(self):
        super().__init__('minimal_publisher')
        self.publisher_ = self.create_publisher(DENMCW, 'topic', 10)     # CHANGE
        timer_period = 0.001
        self.timer = self.create_timer(timer_period, self.timer_callback)

    def timer_callback(self):
        msg = DENMCW()                                           # CHANGE
        msg.pdu_proto_version 		= 4                           			# CHANGE
        msg.pdu_message_id 		= 1                                      	# CAM 2, DENM 1
        msg.pdu_src_station_id 		= 101                                      	# srcStationID

        msg.mc_action_id_origin_station_id 			= 1                           			# CHANGE
        msg.mc_action_id_seq_no 				= 2                                      	# CHANGE
        msg.mc_det_time 					= 3                                      	# CHANGE
        msg.mc_ref_time 					= 4                           			# CHANGE
        msg.mc_ref_pos_lattitude 				= 5                                      	# CHANGE
        msg.mc_ref_pos_longitude 				= 6                                      	# CHANGE
        msg.mc_ref_pos_conf_ellipse_semi_major 			= 7                           			# CHANGE
        msg.mc_ref_pos_conf_ellipse_semi_minor 			= 8                                      	# CHANGE
        msg.mc_ref_pos_altitude_heading 			= 1                           			# CHANGE
        msg.mc_ref_pos_altitude_val 				= 2                                      	# CHANGE
        msg.mc_ref_pos_altitude_conf 				= 3                                      	# CHANGE
        msg.mc_validity_duration		 		= 4                           			# CHANGE
        msg.mc_station_type		 			= 5                                      	# CHANGE

        msg.al_carte_type 					= 1                           			# CHANGE
        msg.al_des_station_id 					= 2                                      	# CHANGE
        msg.al_uc_collision_severity 				= 3                                      	# CHANGE
        msg.al_uc_collision_time		 		= 4                           			# CHANGE
        msg.al_uc_collision_dist		 		= 5                                      	# CHANGE
        msg.al_uc_action_action_type	 			= 6                                      	# CHANGE
        msg.al_uc_action_speed_val 				= 7                           			# CHANGE
        msg.al_uc_action_speed_conf 				= 8                                      	# CHANGE
        msg.al_uc_action_drive_dir_heading_val 			= 9                           			# CHANGE
        msg.al_uc_action_drive_dir_heading_conf	 		= 10                                      	# CHANGE
        msg.al_uc_action_drive_dir_vertical_heading		= 11                                      	# CHANGE
        msg.al_uc_action_long_acc_val			 	= 12                           			# CHANGE
        msg.al_uc_action_long_acc_conf		 		= 13                                      	# CHANGE
        msg.al_uc_action_curv_val		 		= 14                                      	# CHANGE
        msg.al_uc_action_curv_conf		 		= 15                           			# CHANGE
        msg.al_uc_action_curv_cal_mod	 			= 16                                      	# CHANGE
        msg.al_uc_action_yaw_r_val 				= 17                           			# CHANGE
        msg.al_uc_action_yaw_r_conf	 			= 18                                      	# CHANGE
        msg.al_uc_action_lat_acc_val	 			= 19                                      	# CHANGE
        msg.al_uc_action_lat_acc_conf		 		= 20                           			# CHANGE
        msg.al_uc_action_vertical_acc_val		 	= 21                                      	# CHANGE
        msg.al_uc_action_vertical_acc_conf		 	= 22                                      	# CHANGE

        self.publisher_.publish(msg)
        self.get_logger().info('Publishing: \
					\n proto_version - "%d",\
					\n message_id - "%d",\
					\n src_station_id - "%d",\
					\n \
					\n mc_action_id_origin_station_id - "%d",\
					\n mc_action_id_seq_no - "%d",\
					\n mc_det_time - "%d",\
					\n mc_ref_time - "%d",\
					\n mc_ref_pos_lattitude - "%d",\
					\n mc_ref_pos_longitude - "%d",\
					\n mc_ref_pos_conf_ellipse_semi_major - "%d",\
					\n mc_ref_pos_conf_ellipse_semi_minor - "%d",\
					\n mc_ref_pos_altitude_heading - "%d",\
					\n mc_ref_pos_altitude_val - "%d",\
					\n mc_ref_pos_altitude_conf - "%d",\
					\n mc_validity_duration - "%d",\
					\n mc_station_type - "%d",\
					\n \
					\n al_carte_type - "%d",\
					\n al_des_station_id - "%d",\
					\n al_uc_collision_severity - "%d",\
					\n al_uc_collision_time - "%d",\
					\n al_uc_collision_dist - "%d",\
					\n al_uc_action_action_type - "%d",\
					\n al_uc_action_speed_val - "%d",\
					\n al_uc_action_speed_conf - "%d",\
					\n al_uc_action_drive_dir_heading_val - "%d",\
					\n al_uc_action_drive_dir_heading_conf - "%d",\
					\n al_uc_action_drive_dir_vertical_heading - "%d",\
					\n al_uc_action_long_acc_val - "%d",\
					\n al_uc_action_long_acc_conf - "%d",\
					\n al_uc_action_curv_val - "%d",\
					\n al_uc_action_curv_conf - "%d",\
					\n al_uc_action_curv_cal_mod - "%d",\
					\n al_uc_action_yaw_r_val - "%d",\
					\n al_uc_action_yaw_r_conf - "%d",\
					\n al_uc_action_lat_acc_val - "%d",\
					\n al_uc_action_lat_acc_conf - "%d",\
					\n al_uc_action_vertical_acc_val - "%d",\
					\n al_uc_action_vertical_acc_conf - "%d",\
					\n ----------------------------------------------------- \
					' 
					% (	msg.pdu_proto_version, 
						msg.pdu_message_id, 
						msg.pdu_src_station_id,

        					msg.mc_action_id_origin_station_id,
        					msg.mc_action_id_seq_no,
        					msg.mc_det_time,
        					msg.mc_ref_time,
        					msg.mc_ref_pos_lattitude,
        					msg.mc_ref_pos_longitude,
        					msg.mc_ref_pos_conf_ellipse_semi_major,
        					msg.mc_ref_pos_conf_ellipse_semi_minor,
        					msg.mc_ref_pos_altitude_heading,
        					msg.mc_ref_pos_altitude_val,
        					msg.mc_ref_pos_altitude_conf,
        					msg.mc_validity_duration,
        					msg.mc_station_type,

        					msg.al_carte_type,
        					msg.al_des_station_id,
        					msg.al_uc_collision_severity,
        					msg.al_uc_collision_time,
        					msg.al_uc_collision_dist,
        					msg.al_uc_action_action_type,
        					msg.al_uc_action_speed_val,
        					msg.al_uc_action_speed_conf,
        					msg.al_uc_action_drive_dir_heading_val,
        					msg.al_uc_action_drive_dir_heading_conf,
        					msg.al_uc_action_drive_dir_vertical_heading,
        					msg.al_uc_action_long_acc_val,
        					msg.al_uc_action_long_acc_conf,
        					msg.al_uc_action_curv_val,
        					msg.al_uc_action_curv_conf,
        					msg.al_uc_action_curv_cal_mod,
        					msg.al_uc_action_yaw_r_val,
        					msg.al_uc_action_yaw_r_conf,
        					msg.al_uc_action_lat_acc_val,
        					msg.al_uc_action_lat_acc_conf,
        					msg.al_uc_action_vertical_acc_val,
        					msg.al_uc_action_vertical_acc_conf
						) )  # CHANGE


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
