"""
CP1404 Practical
Loops
"""

for i in range(1, 21, 2):
    print(i, end=" ")
print()

# a.
for i in range(0, 110, 10):
    print(i, end=" ")
print()

# b.
for i in range(20, 0, -1):
    print(i, end=" ")
print()

# c.
number_of_stars = int(input("Number of stars: "))
for i in range(number_of_stars):
    print("*", end="")
print()
print()

# d.
for row in range(number_of_stars):
    for column in range(row+1):
        print("*", end="")
    print()
print()
