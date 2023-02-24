#  Deep copy a jagged array
# with numbers or other arrays in a new array
arr1 = [2, 4, 10, [12, 4, [100, 99], 4], [3, 2, 99], 0]
# arr2 = arr1.copy()
# print(arr2)


def copyArray(arr):
    arr2 = []
    for num in arr1:
        if num == list:
            num = copyArray(num)
        arr2.append(num)
    return arr2


print(copyArray(arr1))