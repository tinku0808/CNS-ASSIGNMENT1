import csv
csv.register_dialect('myDialect',delimiter=',',
                     quoting=csv.QUOTE ALL,skipinitialspace=True)
with open('quotes.csv','r')as file:
    fileReader=csv.reader(file,dialect='myDialect')
    for row in fileReader:
        print(row)
    file.close()
