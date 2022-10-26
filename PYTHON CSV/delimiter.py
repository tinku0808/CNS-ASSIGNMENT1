import csv
file=open("CNS.csv",'r')
fileReader=csv.reader(file,)
for row in fileReader:
    print(row[0])
file.close()
