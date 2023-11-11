cmake_minimum_required(VERSION 3.12)
project(FEM)

# Set the path to the pyb11 executable
set(PYB11_EXECUTABLE "extern/pybind11/")  # Replace with the actual path

# Add the subdirectory containing the VectorMath module
add_subdirectory(src)