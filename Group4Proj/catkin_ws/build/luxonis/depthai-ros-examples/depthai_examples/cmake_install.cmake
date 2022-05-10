# Install script for directory: /home/netipc/Desktop/Group4Proj/catkin_ws/src/luxonis/depthai-ros-examples/depthai_examples

# Set the install prefix
if(NOT DEFINED CMAKE_INSTALL_PREFIX)
  set(CMAKE_INSTALL_PREFIX "/home/netipc/Desktop/Group4Proj/catkin_ws/install")
endif()
string(REGEX REPLACE "/$" "" CMAKE_INSTALL_PREFIX "${CMAKE_INSTALL_PREFIX}")

# Set the install configuration name.
if(NOT DEFINED CMAKE_INSTALL_CONFIG_NAME)
  if(BUILD_TYPE)
    string(REGEX REPLACE "^[^A-Za-z0-9_]+" ""
           CMAKE_INSTALL_CONFIG_NAME "${BUILD_TYPE}")
  else()
    set(CMAKE_INSTALL_CONFIG_NAME "")
  endif()
  message(STATUS "Install configuration: \"${CMAKE_INSTALL_CONFIG_NAME}\"")
endif()

# Set the component getting installed.
if(NOT CMAKE_INSTALL_COMPONENT)
  if(COMPONENT)
    message(STATUS "Install component: \"${COMPONENT}\"")
    set(CMAKE_INSTALL_COMPONENT "${COMPONENT}")
  else()
    set(CMAKE_INSTALL_COMPONENT)
  endif()
endif()

# Install shared libraries without execute permission?
if(NOT DEFINED CMAKE_INSTALL_SO_NO_EXE)
  set(CMAKE_INSTALL_SO_NO_EXE "1")
endif()

# Is this installation the result of a crosscompile?
if(NOT DEFINED CMAKE_CROSSCOMPILING)
  set(CMAKE_CROSSCOMPILING "FALSE")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/pkgconfig" TYPE FILE FILES "/home/netipc/Desktop/Group4Proj/catkin_ws/build/luxonis/depthai-ros-examples/depthai_examples/catkin_generated/installspace/depthai_examples.pc")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/depthai_examples/cmake" TYPE FILE FILES
    "/home/netipc/Desktop/Group4Proj/catkin_ws/build/luxonis/depthai-ros-examples/depthai_examples/catkin_generated/installspace/depthai_examplesConfig.cmake"
    "/home/netipc/Desktop/Group4Proj/catkin_ws/build/luxonis/depthai-ros-examples/depthai_examples/catkin_generated/installspace/depthai_examplesConfig-version.cmake"
    )
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/depthai_examples" TYPE FILE FILES "/home/netipc/Desktop/Group4Proj/catkin_ws/src/luxonis/depthai-ros-examples/depthai_examples/package.xml")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  if(EXISTS "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/depthai_examples/crop_control_service" AND
     NOT IS_SYMLINK "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/depthai_examples/crop_control_service")
    file(RPATH_CHECK
         FILE "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/depthai_examples/crop_control_service"
         RPATH "/home/netipc/Desktop/Group4Proj/catkin_ws/devel/lib:/opt/ros/noetic/lib:/usr/local/lib")
  endif()
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/depthai_examples" TYPE EXECUTABLE FILES "/home/netipc/Desktop/Group4Proj/catkin_ws/devel/lib/depthai_examples/crop_control_service")
  if(EXISTS "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/depthai_examples/crop_control_service" AND
     NOT IS_SYMLINK "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/depthai_examples/crop_control_service")
    file(RPATH_CHANGE
         FILE "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/depthai_examples/crop_control_service"
         OLD_RPATH "/home/netipc/Desktop/Group4Proj/catkin_ws/devel/lib:/opt/ros/noetic/lib:/usr/local/lib:"
         NEW_RPATH "/home/netipc/Desktop/Group4Proj/catkin_ws/devel/lib:/opt/ros/noetic/lib:/usr/local/lib")
    if(CMAKE_INSTALL_DO_STRIP)
      execute_process(COMMAND "/usr/bin/strip" "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/depthai_examples/crop_control_service")
    endif()
  endif()
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  if(EXISTS "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/depthai_examples/mobilenet_node" AND
     NOT IS_SYMLINK "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/depthai_examples/mobilenet_node")
    file(RPATH_CHECK
         FILE "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/depthai_examples/mobilenet_node"
         RPATH "/home/netipc/Desktop/Group4Proj/catkin_ws/devel/lib:/opt/ros/noetic/lib:/usr/local/lib")
  endif()
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/depthai_examples" TYPE EXECUTABLE FILES "/home/netipc/Desktop/Group4Proj/catkin_ws/devel/lib/depthai_examples/mobilenet_node")
  if(EXISTS "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/depthai_examples/mobilenet_node" AND
     NOT IS_SYMLINK "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/depthai_examples/mobilenet_node")
    file(RPATH_CHANGE
         FILE "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/depthai_examples/mobilenet_node"
         OLD_RPATH "/home/netipc/Desktop/Group4Proj/catkin_ws/devel/lib:/opt/ros/noetic/lib:/usr/local/lib:"
         NEW_RPATH "/home/netipc/Desktop/Group4Proj/catkin_ws/devel/lib:/opt/ros/noetic/lib:/usr/local/lib")
    if(CMAKE_INSTALL_DO_STRIP)
      execute_process(COMMAND "/usr/bin/strip" "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/depthai_examples/mobilenet_node")
    endif()
  endif()
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  if(EXISTS "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/depthai_examples/rgb_node" AND
     NOT IS_SYMLINK "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/depthai_examples/rgb_node")
    file(RPATH_CHECK
         FILE "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/depthai_examples/rgb_node"
         RPATH "/home/netipc/Desktop/Group4Proj/catkin_ws/devel/lib:/opt/ros/noetic/lib:/usr/local/lib")
  endif()
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/depthai_examples" TYPE EXECUTABLE FILES "/home/netipc/Desktop/Group4Proj/catkin_ws/devel/lib/depthai_examples/rgb_node")
  if(EXISTS "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/depthai_examples/rgb_node" AND
     NOT IS_SYMLINK "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/depthai_examples/rgb_node")
    file(RPATH_CHANGE
         FILE "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/depthai_examples/rgb_node"
         OLD_RPATH "/home/netipc/Desktop/Group4Proj/catkin_ws/devel/lib:/opt/ros/noetic/lib:/usr/local/lib:"
         NEW_RPATH "/home/netipc/Desktop/Group4Proj/catkin_ws/devel/lib:/opt/ros/noetic/lib:/usr/local/lib")
    if(CMAKE_INSTALL_DO_STRIP)
      execute_process(COMMAND "/usr/bin/strip" "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/depthai_examples/rgb_node")
    endif()
  endif()
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  if(EXISTS "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/depthai_examples/rgb_stereo_node" AND
     NOT IS_SYMLINK "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/depthai_examples/rgb_stereo_node")
    file(RPATH_CHECK
         FILE "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/depthai_examples/rgb_stereo_node"
         RPATH "/home/netipc/Desktop/Group4Proj/catkin_ws/devel/lib:/opt/ros/noetic/lib:/usr/local/lib")
  endif()
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/depthai_examples" TYPE EXECUTABLE FILES "/home/netipc/Desktop/Group4Proj/catkin_ws/devel/lib/depthai_examples/rgb_stereo_node")
  if(EXISTS "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/depthai_examples/rgb_stereo_node" AND
     NOT IS_SYMLINK "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/depthai_examples/rgb_stereo_node")
    file(RPATH_CHANGE
         FILE "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/depthai_examples/rgb_stereo_node"
         OLD_RPATH "/home/netipc/Desktop/Group4Proj/catkin_ws/devel/lib:/opt/ros/noetic/lib:/usr/local/lib:"
         NEW_RPATH "/home/netipc/Desktop/Group4Proj/catkin_ws/devel/lib:/opt/ros/noetic/lib:/usr/local/lib")
    if(CMAKE_INSTALL_DO_STRIP)
      execute_process(COMMAND "/usr/bin/strip" "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/depthai_examples/rgb_stereo_node")
    endif()
  endif()
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  if(EXISTS "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/depthai_examples/rgb_subscriber_node" AND
     NOT IS_SYMLINK "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/depthai_examples/rgb_subscriber_node")
    file(RPATH_CHECK
         FILE "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/depthai_examples/rgb_subscriber_node"
         RPATH "/home/netipc/Desktop/Group4Proj/catkin_ws/devel/lib:/opt/ros/noetic/lib:/usr/local/lib")
  endif()
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/depthai_examples" TYPE EXECUTABLE FILES "/home/netipc/Desktop/Group4Proj/catkin_ws/devel/lib/depthai_examples/rgb_subscriber_node")
  if(EXISTS "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/depthai_examples/rgb_subscriber_node" AND
     NOT IS_SYMLINK "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/depthai_examples/rgb_subscriber_node")
    file(RPATH_CHANGE
         FILE "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/depthai_examples/rgb_subscriber_node"
         OLD_RPATH "/home/netipc/Desktop/Group4Proj/catkin_ws/devel/lib:/opt/ros/noetic/lib:/usr/local/lib:"
         NEW_RPATH "/home/netipc/Desktop/Group4Proj/catkin_ws/devel/lib:/opt/ros/noetic/lib:/usr/local/lib")
    if(CMAKE_INSTALL_DO_STRIP)
      execute_process(COMMAND "/usr/bin/strip" "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/depthai_examples/rgb_subscriber_node")
    endif()
  endif()
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  if(EXISTS "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/depthai_examples/stereo_inertial_node" AND
     NOT IS_SYMLINK "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/depthai_examples/stereo_inertial_node")
    file(RPATH_CHECK
         FILE "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/depthai_examples/stereo_inertial_node"
         RPATH "/home/netipc/Desktop/Group4Proj/catkin_ws/devel/lib:/opt/ros/noetic/lib:/usr/local/lib")
  endif()
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/depthai_examples" TYPE EXECUTABLE FILES "/home/netipc/Desktop/Group4Proj/catkin_ws/devel/lib/depthai_examples/stereo_inertial_node")
  if(EXISTS "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/depthai_examples/stereo_inertial_node" AND
     NOT IS_SYMLINK "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/depthai_examples/stereo_inertial_node")
    file(RPATH_CHANGE
         FILE "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/depthai_examples/stereo_inertial_node"
         OLD_RPATH "/home/netipc/Desktop/Group4Proj/catkin_ws/devel/lib:/opt/ros/noetic/lib:/usr/local/lib:"
         NEW_RPATH "/home/netipc/Desktop/Group4Proj/catkin_ws/devel/lib:/opt/ros/noetic/lib:/usr/local/lib")
    if(CMAKE_INSTALL_DO_STRIP)
      execute_process(COMMAND "/usr/bin/strip" "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/depthai_examples/stereo_inertial_node")
    endif()
  endif()
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  if(EXISTS "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/depthai_examples/stereo_node" AND
     NOT IS_SYMLINK "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/depthai_examples/stereo_node")
    file(RPATH_CHECK
         FILE "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/depthai_examples/stereo_node"
         RPATH "/home/netipc/Desktop/Group4Proj/catkin_ws/devel/lib:/opt/ros/noetic/lib:/usr/local/lib")
  endif()
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/depthai_examples" TYPE EXECUTABLE FILES "/home/netipc/Desktop/Group4Proj/catkin_ws/devel/lib/depthai_examples/stereo_node")
  if(EXISTS "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/depthai_examples/stereo_node" AND
     NOT IS_SYMLINK "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/depthai_examples/stereo_node")
    file(RPATH_CHANGE
         FILE "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/depthai_examples/stereo_node"
         OLD_RPATH "/home/netipc/Desktop/Group4Proj/catkin_ws/devel/lib:/opt/ros/noetic/lib:/usr/local/lib:"
         NEW_RPATH "/home/netipc/Desktop/Group4Proj/catkin_ws/devel/lib:/opt/ros/noetic/lib:/usr/local/lib")
    if(CMAKE_INSTALL_DO_STRIP)
      execute_process(COMMAND "/usr/bin/strip" "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/depthai_examples/stereo_node")
    endif()
  endif()
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  if(EXISTS "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/depthai_examples/yolov4_spatial_node" AND
     NOT IS_SYMLINK "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/depthai_examples/yolov4_spatial_node")
    file(RPATH_CHECK
         FILE "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/depthai_examples/yolov4_spatial_node"
         RPATH "/home/netipc/Desktop/Group4Proj/catkin_ws/devel/lib:/opt/ros/noetic/lib:/usr/local/lib")
  endif()
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/depthai_examples" TYPE EXECUTABLE FILES "/home/netipc/Desktop/Group4Proj/catkin_ws/devel/lib/depthai_examples/yolov4_spatial_node")
  if(EXISTS "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/depthai_examples/yolov4_spatial_node" AND
     NOT IS_SYMLINK "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/depthai_examples/yolov4_spatial_node")
    file(RPATH_CHANGE
         FILE "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/depthai_examples/yolov4_spatial_node"
         OLD_RPATH "/home/netipc/Desktop/Group4Proj/catkin_ws/devel/lib:/opt/ros/noetic/lib:/usr/local/lib:"
         NEW_RPATH "/home/netipc/Desktop/Group4Proj/catkin_ws/devel/lib:/opt/ros/noetic/lib:/usr/local/lib")
    if(CMAKE_INSTALL_DO_STRIP)
      execute_process(COMMAND "/usr/bin/strip" "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/depthai_examples/yolov4_spatial_node")
    endif()
  endif()
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/depthai_examples/launch" TYPE DIRECTORY FILES "/home/netipc/Desktop/Group4Proj/catkin_ws/src/luxonis/depthai-ros-examples/depthai_examples/launch/" REGEX "/\\.svn$" EXCLUDE)
endif()

