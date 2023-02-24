# Print the distance between the first 100 prime numbers


def isprime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    for i in range(2, (n - 1)):
        if n % i == 0:
            return False
    return True


arr = []
arr1 = []
for i in range(1, 101):
    if isprime(i):
        arr.append(i)
print("The prime numbers are: ", arr)
for i in range(0, len(arr)-1):
    arr1.append(arr[i+1] - arr[i])
print("The distance between the prime numbers are: ", arr1)
