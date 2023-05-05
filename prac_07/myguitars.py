import csv
from prac_06.guitar import Guitar

def main():
    in_file = open('guitars.csv', 'r', newline='')
    guitars = csv.reader(in_file)
    for row in guitars:
        print(row)
    in_file.close()

main()