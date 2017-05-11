import csv
file=open( "file_name.csv", "r")      #change filename
reader = csv.reader(file)
arr=[]
for line in reader:
    t=line[0]
    arr.append(t)
k=len(arr)
if k:
    file=open( "file_name.csv", "r")  #change filename
    reader = csv.reader(file)
    for line in reader:
        t=line[0]
        arr.append(t)
tk=len(arr)
count=0
with open('outmerge.csv', 'w') as csvfile:
    fieldnames = ['list']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    while (count < tk):
	writer.writerow({'list': arr[count]})
	count = count + 1
