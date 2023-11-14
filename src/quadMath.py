from LinearAlgebra import *

if __name__ == "__main__":
    p1 = Vector2d(0.1, 0.4)
    p2 = Vector2d(2.0, 0.1)
    p3 = Vector2d(2.4, 2.3)
    p4 = Vector2d(0.5, 2.0)

    area = quadArea(p1,p2,p3,p4)
    print("Area:", area)

    p3 = Vector2d(2.4, 5.3)

    area = quadArea(p1,p2,p3,p4)
    print("Area:", area)