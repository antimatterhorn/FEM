from LinearAlgebra import *
import math

def computeQuadArea(p1, p2, p3, p4):
    # Calculate centroid
    centroid = (p1+p2+p3+p4)/4.0

    # Sort points based on angle with respect to the centroid
    sorted_points = [p1, p2, p3, p4]
    sorted_points.sort(key=lambda p: math.atan2(p.y - centroid.y, p.x - centroid.x))

    # Calculate signed area using the sorted points
    area = 0.0
    for i in range(4):
        next_index = (i + 1) % 4
        area += (sorted_points[i].x * sorted_points[next_index].y - sorted_points[next_index].x * sorted_points[i].y)

    return 0.5 * area

if __name__ == "__main__":
    p1 = Vector2d(0.1, 0.4)
    p2 = Vector2d(2.0, 0.1)
    p3 = Vector2d(2.4, 2.3)
    p4 = Vector2d(0.5, 2.0)

    area = computeQuadArea(p1, p2, p3, p4)
    print("Area:", area)