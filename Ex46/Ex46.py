# Find the maximum number in a jagged array of numbers or array of numbers
def function(arr):
    max = arr[0]
    for num in arr:
        if type(num) == list:
           num = function(num)
        if max < num:
            max = num
    return max


print(function([2, 4, 10, [12, 4, [100, 99], 4], [3, 2, 99], 0]))
