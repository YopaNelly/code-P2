# Create a function that will receive a bi-dimensional array as argument and a
# number and will extract as a unidimensional array the column specified by the
# number
from array import array


def function(arr, n):
    arr = [[0] * 10] * 8
    arr[0][2] = 1
    return arr[n]


arr = []
print(function(arr, 1))
