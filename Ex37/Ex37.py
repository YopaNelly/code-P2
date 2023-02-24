# Create a function that will convert a string in an array containing the ASCII codes of
# each character
arr = []


def function(string):
    string = list(string)
    for i in string:
        arr.append(ord(i))
    return arr


string = "Yo guys have fun :)"
print(function(string))
