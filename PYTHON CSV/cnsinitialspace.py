import csv
csv.register_dialect('mydialect',delimiter=',',skipinitialspace=True)
file= open("CNS.csv",'r')
fileReader=csv.reader(file,dialect='mydialect')
for row in fileReader:
    print(row)
file.close()
    
