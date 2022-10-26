import csv,operator
sortedlist=[]
csv.register_dialect("mydialect",delimiter=',',skipinitialspace=True)
file=open("CNS.csv",'r')
filereader=csv.reader(file,dialect="mydialect")
next(filereader)
sortedlist=sorted(filereader,key=operator.itemgetter(0))
for row in sortedlist:
    print(row)
file.close()
