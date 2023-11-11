cmake_minimum_required(VERSION 3.12)
project(VectorMathProject)

# Add the pybind11 submodule
add_subdirectory(extern/pybind11)

# Include the pybind11 headers
include_directories(extern/pybind11/include)

add_library(VectorMath MODULE src/vector_math.cpp src/vector_math_interface.cpp)
target_link_libraries(VectorMath PRIVATE pybind11::module)