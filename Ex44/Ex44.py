# Create a function that will convert a string containing a binary number into a
# number


from math import pow
arr = []


def function(string):
    for i in string:
        arr.append(i)
    n = len(arr)
    sum = 0
    for num in arr:
        sum += int(num)*pow(2, n-1)
        n -= 1
    return round(sum)


print(function("111"))
