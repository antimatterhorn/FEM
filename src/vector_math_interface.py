# vector_math_interface.py (Python interface for VectorMath namespace using cppyy)

import cppyy

# Load the vector_math.cpp file as a Python module using cppyy
cppyy.include("vector_math.cpp")

# Import the VectorMath namespace
VectorMath = cppyy.gbl.VectorMath

class Vector:
    def __init__(self,*args):
        if len(args) == 1:
            self.vector = VectorMath.Vector1D(*args)
        elif len(args) == 2:
            self.vector = VectorMath.Vector2D(*args)
        elif len(args) == 3:
            self.vector = VectorMath.Vector3D(*args)
        else:
            raise ValueError("invalid number of args for Vector")
    def crossProduct(self,other):
        crossP = self.vector.crossProduct(other.vector)
        if isinstance(self.vector, VectorMath.Vector3D):
            return Vector(crossP.x(), crossP.y(), crossP.z())
        elif isinstance(self.vector, VectorMath.Vector2D):
            return Vector(crossP.x(), crossP.y())
        elif isinstance(self.vector, VectorMath.Vector1D):
            return Vector(crossP.x())
        else:
            raise ValueError("Invalid vector type after cross product")
    
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
        return str(self.vector.toString())

# Example usage
if __name__ == "__main__":
    vec1 = Vector(1.0,2.0,3.0)
    vec2 = Vector(2.0,3.0,4.0)

    print(vec1,vec2)
    print(vec1.crossProduct(vec2))
