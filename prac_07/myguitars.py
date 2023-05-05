import csv
from prac_06.guitar import Guitar

def main():
    guitars = []
    in_file = open('guitars.csv', 'r', newline='')
    guitar_data = csv.reader(in_file)
    for row in guitar_data:
        guitars.append(row)
    in_file.close()


main()