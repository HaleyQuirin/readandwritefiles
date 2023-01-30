import csv

infile = open("customers.csv", "r")
outfile = open("customer_country.csv", "w")

read = csv.reader(infile, delimiter=",")

outfile.write("Name, Country\n")

for line in read:
    FirstName = line[1]
    LastName = line[2]
    Country = line[4]
    newfile = FirstName + " " + LastName + ", " + Country
    outfile.write(newfile + "\n")

infile.close()
outfile.close()
