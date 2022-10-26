import csv,operator
csv.register_dialect("mydialect",delimiter=',',skipinitialspace=True)
file=open("CNS.csv",'r')
filereader=csv.DictReader(file,dialect="mydialect")
for row in filereader:
    print(row)
file.close()
