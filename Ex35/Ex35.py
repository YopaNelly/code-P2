# Create a function to convert a CSV text to a “bi-dimensional” array
def function(string):
    arr = []
    n = 0
    string = string.split()
    for i in string:
        arr.insert(n, list(i))
        n += 1
    return arr


print(function("Hello convert csv to array"))
