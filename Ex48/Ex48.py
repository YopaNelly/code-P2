# Create a function to return the longest word(s) in a string
text = "Create a function to return the longestn word(s) in a string"
text = text.split()
arr2 = []


def longustWord(text):
    longustWord = ""
    for word in text:
        if len(word) > len(longustWord):
            longustWord = word
    return longustWord


print(longustWord(text))
