"""
Guitar Exercise
Guitars file

Estimate and actual in guitar file
"""

from prac_06.guitar import Guitar

print("My guitars!")
guitars = []
name = input("Name: ")
while name != "":
    year = int(input("Year: "))
    cost = float(input("Cost: $"))
    guitar_details = Guitar(name, year, cost)
    guitars.append(guitar_details)
    print(guitar_details, " added")
    print()
    name = input("Name: ")

# Find the longest name length
length = len(guitars[0].name)
for guitar in guitars:
    if len(guitar.name) > length:
        length = len(guitar.name)

print()
# List all the guitars that is inputted
print("These are my guitars:")
for i, guitar in enumerate(guitars, 1):
    vintage_string = ""
    if guitar.is_vintage():
        vintage_string = "(vintage)"
    print(f"Guitar {i}: {guitar.name:>{length}} ({guitar.year}), worth ${guitar.cost:10,.2f} {vintage_string}")
