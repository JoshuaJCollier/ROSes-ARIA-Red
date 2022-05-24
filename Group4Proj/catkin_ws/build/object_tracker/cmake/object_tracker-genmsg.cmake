# generated from genmsg/cmake/pkg-genmsg.cmake.em

message(STATUS "object_tracker: 1 messages, 0 services")

set(MSG_I_FLAGS "-Iobject_tracker:/home/netipc/Desktop/Group4Proj/catkin_ws/src/object_tracker/msg;-Istd_msgs:/opt/ros/noetic/share/std_msgs/cmake/../msg")

# Find all generators

add_custom_target(object_tracker_generate_messages ALL)

# verify that message/service dependencies have not changed since configure



get_filename_component(_filename "/home/netipc/Desktop/Group4Proj/catkin_ws/src/object_tracker/msg/Objects.msg" NAME_WE)
add_custom_target(_object_tracker_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "object_tracker" "/home/netipc/Desktop/Group4Proj/catkin_ws/src/object_tracker/msg/Objects.msg" ""
)

#
#  langs = 
#


