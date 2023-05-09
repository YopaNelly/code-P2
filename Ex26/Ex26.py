# Create a function that will receive two arrays and will return an array with elements that are in the first array but not in the second
first_array = [1, 2, 3, 10, 5, 3, 14]
second_array = [-1, 4, 5, 6, 14]


def function(arr1, arr2):
    for i in arr1:
        for j in arr2:
            if i == j:
                arr1.remove(i)
    return arr1


print(function(first_array, second_array))
