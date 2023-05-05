import csv
from prac_06.guitar import Guitar

def main():
    guitars = []
    in_file = open('guitars.csv', 'r', newline='')
    guitar_data = csv.reader(in_file)
    for name, year, cost in guitar_data:
        guitars.append(Guitar(name, int(year), float(cost)))
    in_file.close()
    
    for guitar in guitars:
        print(guitar)



main()