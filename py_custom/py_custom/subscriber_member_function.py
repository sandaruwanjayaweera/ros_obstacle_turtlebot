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

from tutorial_interfaces.msg import CAM

class MinimalSubscriber(Node):

    def __init__(self):
        super().__init__('minimal_subscriber')
        self.subscription = self.create_subscription(CAM, 'CAM', self.listener_callback, 10)	 	#CHANGE
        self.subscription

    def listener_callback(self, msg):
            self.get_logger().info('I heard: \
						\n proto_version - "%d",\
						\n message_id - "%d",\
						\n src_station_id - "%d"\
						\n \
						\n bc_station_type - "%d",\
						\n bc_ref_pos_lattitude - "%d",\
						\n bc_ref_pos_longitude - "%d",\
						\n bc_ref_pos_conf_ellipse_semi_major - "%d",\
						\n bc_ref_pos_conf_ellipse_semi_minor - "%d",\
						\n bc_ref_pos_altitude_heading - "%d",\
						\n bc_ref_pos_altitude_val - "%d",\
						\n bc_ref_pos_altitude_conf - "%d",\
						\n \
						\n hf_heading_val - "%d",\
						\n hf_heading_conf - "%d",\
						\n hf_vertical_heading - "%d",\
						\n hf_speed_val - "%d",\
						\n hf_speed_conf - "%d",\
						\n hf_drive_dir_heading_val - "%d",\
						\n hf_drive_dir_heading_conf - "%d",\
						\n hf_drive_dir_vertical_heading - "%d",\
						\n hf_v_len_val - "%d",\
						\n hf_v_len_conf - "%d",\
						\n hf_v_width - "%d",\
						\n hf_v_height - "%d",\
						\n hf_long_acc_val - "%d",\
						\n hf_long_acc_conf - "%d",\
						\n hf_curv_val - "%d",\
						\n hf_curv_conf - "%d",\
						\n hf_curv_cal_mod - "%d",\
						\n hf_yaw_r_val - "%d",\
						\n hf_yaw_r_conf - "%d",\
						\n hf_lat_acc_val - "%d",\
						\n hf_lat_acc_conf - "%d",\
						\n hf_vertical_acc_val - "%d",\
						\n hf_vertical_acc_conf - "%d",\
						\n ----------------------------------------------------- \
						' 
						% (	msg.pdu_proto_version, 
							msg.pdu_message_id, 
							msg.pdu_src_station_id,

							msg.bc_station_type, 
							msg.bc_ref_pos_lattitude,
							msg.bc_ref_pos_longitude, 
							msg.bc_ref_pos_conf_ellipse_semi_major,
							msg.bc_ref_pos_conf_ellipse_semi_minor, 
							msg.bc_ref_pos_altitude_heading,
							msg.bc_ref_pos_altitude_val, 
							msg.bc_ref_pos_altitude_conf,

							msg.hf_heading_val, 
							msg.hf_heading_conf,
							msg.hf_vertical_heading, 
							msg.hf_speed_val,
							msg.hf_speed_conf, 
							msg.hf_drive_dir_heading_val,
							msg.hf_drive_dir_heading_conf, 
							msg.hf_drive_dir_vertical_heading,
							msg.hf_v_len_val, 
							msg.hf_v_len_conf,
							msg.hf_v_width, 
							msg.hf_v_height,
							msg.hf_long_acc_val, 
							msg.hf_long_acc_conf,
							msg.hf_curv_val, 
							msg.hf_curv_conf,
							msg.hf_curv_cal_mod, 
							msg.hf_yaw_r_val,
							msg.hf_yaw_r_conf, 
							msg.hf_lat_acc_val,
							msg.hf_lat_acc_conf, 
							msg.hf_vertical_acc_val,
							msg.hf_vertical_acc_conf
							) ) # CHANGE


def main(args=None):
    rclpy.init(args=args)

    minimal_subscriber = MinimalSubscriber()

    rclpy.spin(minimal_subscriber)

    minimal_subscriber.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
