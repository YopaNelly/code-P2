import math
# Create a function that will return a Boolean value indicating if two circles
# defined by center coordinates and radius are intersecting
import math


# Function to check if two circles touch each other
def function(x1, y1, x2, y2, r1, r2):
    d = math.sqrt((x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2))
    return d <= r1+r2


print(function(200, 200, 100, 300, 300, 50))
