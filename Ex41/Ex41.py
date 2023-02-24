# Create a function to calculate the distance between two points defined by their x, y
# coordinates
import math


def Distance(P1, P2):
    distance = math.sqrt(((p1[0] - p2[0]) ** 2) + ((p1[1] - p2[1]) ** 2))
    return distance


p1 = [4, 6]
p2 = [5, 5]
print("Distance between the two point is: ", Distance(p1, p2))
