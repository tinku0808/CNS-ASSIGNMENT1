import csv
info=[['sno','name','dob'],[1,INKU,8/8/2002],[2,AVANTH,2/4/2002],[3,TEJU,4/3/2002]]

csv.register_dialect("mydialect",quoting=csv.QUOTE_ALL,delimiter='$')
with open("dob1.csv",'w') as file:
    filewriter=csv.writer(file,dialect="mydialect")
    for row in info:
        filewriter.writerow(row)
file.close()
