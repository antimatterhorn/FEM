# Example usage
import sys
# caution: path[0] is reserved for script path (or '' in REPL)
sys.path.insert(1, '../src')

import vector_math_interface.py as VectorMath

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
