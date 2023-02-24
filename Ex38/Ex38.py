# Create a function that will
# convert an array containing ASCII codes in a string

def function(arr):
    n = 0
    for i in arr:
        arr[n] = chr(i)
        n += 1
    arr = ''.join(arr)
    return arr


code = [73, 32, 108, 111, 118, 101, 32, 109, 121, 32, 115, 101, 108, 102]
print(function(code))
