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

from tutorial_interfaces.msg import DENMCW

class MinimalSubscriber(Node):

    def __init__(self):
        super().__init__('minimal_subscriber')
        self.subscription = self.create_subscription(DENMCW, 'topic', self.listener_callback, 10)	 	#CHANGE
        self.subscription

    def listener_callback(self, msg):
            self.get_logger().info('I heard: \
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
							) ) # CHANGE


def main(args=None):
    rclpy.init(args=args)

    minimal_subscriber = MinimalSubscriber()

    rclpy.spin(minimal_subscriber)

    minimal_subscriber.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
