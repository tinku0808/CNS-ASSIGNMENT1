import csv
info=[['SNO','NAME','AGE'],[1,'TINKU','20'],[2,'THARUN',20],[3,'TEJU',20],[4,'AVANTH',60]]
csv.register_dialect("mydialect",quoting=csv.QUOTE_ALL,delimiter=',')
file=open('age.csv','w')
filewriter=csv.writer(file,dialect="mydialect")
for row in info:
    filewriter.writerow(row)
file.close()
