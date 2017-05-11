import json
import csv
import ast,json
from pprint import pprint
with open('report.json') as data_file:    
    data = json.load(data_file)
f = open('myfile.txt', 'w')
f.write(str(data["behavior"]["apistats"])) 
f.close()
with open('myfile.txt') as fp:
    k= fp.readline().split(':', 1 )
l=k[0].split('{',1)
k=ast.literal_eval(json.dumps(l[1]))
value= ast.literal_eval(k)
print value
no=len(data["behavior"]["apistats"][value])
count=0
print no
lists=(data["behavior"]["apistats"][value].keys())
jlist= ast.literal_eval(json.dumps(lists))
val= ast.literal_eval(str(jlist))
with open('apistats.csv', 'w') as csvfile:
    fieldnames = ['apistats']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    while (count < no):
  	writer.writerow({'apistats': val[count]})
	  count = count + 1




