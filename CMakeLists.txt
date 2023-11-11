cmake_minimum_required(VERSION 3.12)
project(FEM)

# Set the path to the pyb11 executable
set(PYB11GENERATOR_ROOT_DIR ${CMAKE_SOURCE_DIR}/extern/PYB11Generator)
include(${PYB11GENERATOR_ROOT_DIR}/cmake/PYB11Generator.cmake)

# Add the subdirectory containing the VectorMath module
add_subdirectory(src)