import csv

infile = open("sales.csv", "r")  # open file sales.csv to read
outfile = open("salesreport.csv", "w")  # open file sales.csv to write
next(infile)

read = csv.reader(infile, delimiter=",")

outfile.write("Customer ID          Total\n")

CustomerID = "249"
CustomerTotal = 0

for line in read:
    if CustomerID != line[0]:
        print(CustomerTotal)
        CustomerID = [0]
        CustomerTotal = 0
        CustomerID = line[0]
        Total = line[3] + line[4] + line[5]
        newfile = CustomerID + "                  " + Total
        outfile.write(newfile + "\n")

    Total = float(line[3]) + float(line[4]) + float(line[5])
    CustomerTotal += Total

infile.close()
outfile.close()
