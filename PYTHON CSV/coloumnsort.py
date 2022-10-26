import csv,operator
sortedlist=[]
csv.register_dialect("myDialect",delimiter=',',skipinitialspace=True)
file=open("CNS.csv",'r')
fileReader=csv.reader(file,'myDialect')
next(fileReader)
for col in fileReader:
    sortedlist.append(col[0])#=sorted(fileReader,key=operator.itemgetter(0))
sortedlist.sort()
for row in sortedlist:
    print("itEm",row)
file.close()
