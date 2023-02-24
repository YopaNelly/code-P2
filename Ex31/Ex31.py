# Create a function that will return the number of words in a text
me = "Hello! I am Nelly Come join me let write codes"


def numberOfWords(string):
    arr = string.split()
    return len(arr)


print("Number of words in the text: ", numberOfWords(me))