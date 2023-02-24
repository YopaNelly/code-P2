# Create a function that will capitalize the first letter of each word in a text
me = "create a function that will capitalize the first letter of each word in a text"


def capitalizeFirst(string):
    return string.title()  # Or " ".join(word[0].upper()+word[1:] for word in string.split(" "))


print(capitalizeFirst(me))

