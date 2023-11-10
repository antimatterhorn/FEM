import sys
import importlib

sys.path.insert(1, '/home/cody/codes/FEM/build')
print(sys.path)

try:
    VectorMath = importlib.import_module('VectorMath')
except ImportError as e:
    print(e)

if __name__ == "__main__":
    vec1 = Vector(1.0,2.0,3.0)
    vec2 = Vector(2.0,3.0,4.0)

    print("Vec1 =",vec1)
    print("Vec2 =",vec2)
    print("Vec1*Vec2 =",vec1*vec2)
    print("Vec1xVec2 =",vec1.crossProduct(vec2))
    print("Vec1+Vec2 =",vec1+vec2)
    print("Vec2*2 = ",vec2*2.0)
    print("|Vec2| =",vec2.magnitude)
