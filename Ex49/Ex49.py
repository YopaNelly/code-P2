#  Shuffle an array of strings
import random


def function(string):
    arr = list(string)
    random.shuffle(arr)
    result = ''.join(arr)
    return result


string = "Shuffle an array of strings"
print(function(string))

