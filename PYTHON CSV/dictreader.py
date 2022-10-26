import csv
#csv.register_dialect("myDialect",delimiter=',',skipinitialspace=True)
file=open("CNS.csv",'r')
fileReader=csv.DictReader(file)
for row in fileReader:
    print(row)
file.close()
