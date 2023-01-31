import csv

infile = open("sales.csv", "r")  # open file sales.csv to read
write = open("salesreport.csv", "w")  # open file sales.csv to write
outfile = csv.writer(write)

next(infile)

read = csv.reader(infile, delimiter=",")  # "," will be seen as the delimiter

outfile.writerow(["Customer ID, Total"])  # title at teh top of the "sales report"

CustomerID = "250"  # starting point
CustomerTotal = 0  # starting point


for line in read:
    if CustomerID != line[0]:
        outfile.writerow([CustomerID] + [str(CustomerTotal)])
        Total = 0
        CustomerTotal = 0
        CustomerID = line[0]
        Total = float(line[3]) + float(line[4]) + float(line[5])
        CustomerTotal += Total
    else:
        Total = float(line[3]) + float(line[4]) + float(line[5])
        CustomerTotal += Total
outfile.writerow([CustomerID] + [str(CustomerTotal)])


infile.close()
write.close()
