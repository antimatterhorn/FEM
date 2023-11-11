# pybind11gen.py

import sys
from PYB11Generator import *

PYB11namespaces = ["VectorMath"]


# Include the C++ header
cppCode = """
#include "vector_math.cpp"
"""

# Create a PYB11 module
m = PYB11module(cppCode,
                 )

# Expose Vector classes to Python
PYB11generateModule(m, targets=[VectorMath.Vector1D, VectorMath.Vector2D, VectorMath.Vector3D])
