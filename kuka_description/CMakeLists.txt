cmake_minimum_required(VERSION 3.0.2)
project(kuka_description)


add_compile_options(-std=c++11)

find_package(catkin REQUIRED COMPONENTS
    # kuka_gazebo
    # kuka_kr4_moveit
    kuka_kr4_support
)

catkin_package()

include_directories(
  ${catkin_INCLUDE_DIRS}
)