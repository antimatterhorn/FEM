import sys
import importlib

from LinearAlgebra import *

if __name__ == "__main__":
    vec1 = Vector3d(1.0,2.0,3.0)
    vec2 = Vector3d(2.0,3.0,4.0)

    print("Vec1 =",vec1)
    print("Vec2 =",vec2)
    print("Vec1*Vec2 =",vec1*vec2)
    print("Vec1xVec2 =",vec1.cross(vec2))
    print("Vec1+Vec2 =",vec1+vec2)
    print("Vec2*2 = ",vec2*2.0)
    print("|Vec2| =",vec2.magnitude)
