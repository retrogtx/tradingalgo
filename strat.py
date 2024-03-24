import csv

with open('nifty50.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)