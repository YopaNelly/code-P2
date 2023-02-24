#  Calculate 70! with high precision (all digits)

n = 70
factorial = 1
for i in range(1, (n+1)):
    factorial *= i
print(round(factorial))
