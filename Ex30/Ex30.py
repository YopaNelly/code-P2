# Create a function that will add two positive numbers of indefinite size. The numbers
# are received as strings and the result should be also provided as string.
num1 = input("enter your number: ")
num2 = input("enter an other number: ")


def function(a, b):
    if int(a) >= 0 and int(b) >= 0:
        sum = int(a) + int(b)
        return str(sum)
    else:
        return "invalid numbers"


print(function(num1, num2))
