# Create a function to calculate the sum of all the numbers in a jagged array
# (contains numbers or other arrays of numbers on an unlimited number of
# levels)


def sumjegged(arr):
    sum = 0
    for num in arr:
        if type(num) == list:
           num = sumjegged(num)
        sum += num
    return sum


print(sumjegged([[7, 2], [68, 45, [23]], [10, 45], 1, 4]))
