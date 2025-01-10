# Prompt for a number.
n = int(input("Give me a number: "))

# Create an array.
array = []
import random
for i in range(n):
    array.append(random.randrange(0, n * 10))

# This is the algorithm.
c = 0
found = False
for index_1 in range(n):
    for index_2 in range(index_1 + 1, n):
        c += 1
        if array[index_1] == array[index_2]:
            found = True

print("n =", n, "    c =", c)

# Return and report.
if found:
    print("There was a duplicate in", array)
else:
    print("There was not a duplicate in", array)