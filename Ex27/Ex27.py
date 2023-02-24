# Create a function that will receive an array of numbers as argument and will return a
# new array with distinct elements


def printDistinct(arr):
    for i in arr:
        if i not in arr1:
            arr1.append(i)
    return arr1


arr = [6, 10, 5, 4, 9, 120, 4, 6, 10]
arr1 = []
print(printDistinct(arr))


