NAME_FILE = "name.txt"
NUMBER_FILE = "numbers.txt"

out_file = open(NAME_FILE, "w")
name = input("Enter name: ")
print(name, file=out_file)
out_file.close()

in_file = open(NAME_FILE, "r")
print(f"Your name is {in_file.read()}")
in_file.close()

number_file = open(NUMBER_FILE, "r")
first_number = int(number_file.readline())
second_number = int(number_file.readline())
number_file.close()
total = 0
total = first_number + second_number
print(total)

number_file = open(NUMBER_FILE, "r")
lines = number_file.readlines()
number_file.close()
for line in lines:
    line = line.strip()
    print(line)

