import csv
#file=open('CNS.csv','r')
with open('CNS.csv','r') as file:
    fileReader=csv.reader(file)
    print(fileReader)
    for row in fileReader:
        print(row)
file.close()

