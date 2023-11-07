# vector_math_interface.py (Python interface for VectorMath namespace using cppyy)

import cppyy

# Load the vector_math.cpp file as a Python module using cppyy
cppyy.include("vector_math.cpp")

# Import the VectorMath namespace
VectorMath = cppyy.gbl.VectorMath

class Vector:
    def __init__(self,*args):
        self.vector = VectorMath.Vector(args)
    def cross(self,other):
        crossP = self.vector.cross(other.vector)
        return Vector(crossP.x(),crossP.y(),crossP.z())
    
    @property
    def x(self):
        return self.vector.x()

    @property
    def y(self):
        return self.vector.y()

    @property
    def z(self):
        return self.vector.z()

    def __str__(self):
        return f"({self.x}, {self.y}, {self.z})"

# Example usage
if __name__ == "__main__":
    vec1 = Vector(1.0,2.0,3.0)
    vec2 = Vector(2.0,3.0,4.0)

    print(vec1.cross(vec2))
