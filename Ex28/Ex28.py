# Calculate the sum of first 100 prime numbers and return them in an array
def isprime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    for p in range(2, (n - 1)):
        if n % p == 0:
            return False
    return True


arr2 = []
for i in range(2, 101):
    if isprime(i):
        arr2.append(i)
print("The prime numbers are: ", arr2)
sum = 0
for i in range(2, 101):
    if isprime(i):
        sum += i
print("The sum of the prime numbers is: ", sum)
