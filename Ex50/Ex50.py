# Create a function that will receive n as argument and return an array of n
# random numbers from 1 to n


import itertools
import random


def random_gen(n):
    while True:
        yield random.randrange(n)


gen = random_gen(100)

items = set()
arr = []
for x in itertools.takewhile(lambda x: len(items) < 10, gen):
    items.add(x)
for i in items:
    arr.append(i)
print(arr)
