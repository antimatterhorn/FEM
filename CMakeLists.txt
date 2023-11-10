cmake_minimum_required(VERSION 3.12)
project(VectorMathProject)

include(FetchContent)

# Fetch pybind11
FetchContent_Declare(
    pybind11
    GIT_REPOSITORY https://github.com/pybind/pybind11.git
    GIT_TAG v2.7.1  # Use the specific version you need
)
FetchContent_MakeAvailable(pybind11)

add_library(VectorMath MODULE src/vector_math.cpp src/vector_math_interface.cpp)
target_link_libraries(VectorMath PRIVATE pybind11::module python3.8)