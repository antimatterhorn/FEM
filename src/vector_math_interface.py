# vector_math_interface.py (Python interface for vector math operations using cppyy)

import cppyy

# Load the updated C++ functions as a Python module using cppyy
cppyy.include("vector_math.cpp")

# Import the VectorMath namespace
VectorMath = cppyy.gbl.VectorMath

class Vector:
    @staticmethod
    def create_vector(*args):
        return VectorMath.Vector(args)

# Example usage
if __name__ == "__main__":
    vector_a = Vector.create_vector(1.0, 2.0, 3.0)
    vector_b = Vector.create_vector(4.0, 5.0, 6.0)
    scalar = 2.0

    # Vector addition
    result_addition = vector_a.add(vector_b)

    # Dot product
    result_dot_product = vector_a.dotProduct(vector_b)

    # Cross product
    result_cross_product = vector_a.crossProduct(vector_b)

    # Scalar product
    result_scalar_product = vector_a.scalarProduct(scalar)

    print("Vector Addition Result:", result_addition.values)
    print("Dot Product Result:", result_dot_product)
    print("Cross Product Result:", result_cross_product.values)
    print("Scalar Product Result:", result_scalar_product.values)
