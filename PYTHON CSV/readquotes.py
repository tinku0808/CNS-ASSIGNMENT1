import csv
csv.register_dialect('myDialect',delimiter=',',quoting=csv.QUOTE_ALL,
                     skipinitialspace=True)
file=open("quotes.csv",'r')
fileReader=csv.reader(file,dialect='myDialect')
for row in fileReader:
    print(row)
file.close()
