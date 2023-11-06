# vector_math_interface.py (Python interface for VectorMath namespace using cppyy)

import cppyy

# Load the vector_math.cpp file as a Python module using cppyy
cppyy.include("vector_math.cpp")

# Import the VectorMath namespace
VectorMath = cppyy.gbl.VectorMath

class VectorMathWrapper:
    @staticmethod
    def create_vector(*args):
        return VectorMath.Vector(args)
