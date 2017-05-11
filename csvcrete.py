import csv
with open('names.csv', 'w') as csvfile:
    fieldnames = ['strings']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerow({'strings': 'Baked'})
 
