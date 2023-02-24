# Find the frequency of characters inside a string. Return the result as an
# array of objects.


def getcharfreq(string):
    arr1 = []
    arr2 = []
    string = list(string)
    for letter in string:
        if ord(letter) not in range(65, 91) and ord(letter) not in range(97, 123):
            continue
        if letter not in arr2:
            arr1.append([letter, string.count(letter)])
        arr2.append(letter)

    return arr1


print(getcharfreq("Hello I will like to work harder"))