import csv

infile = open("EmployeePay.csv", "r")

contents = csv.reader(infile, delimiter=",")

for details in contents:
    print("EmployeeID :", details[0])
    print("FirstName :", details[1])
    print("LastName :", details[2])
    print("Salary :", details[3])
    print("Bonus :", details[4])
    print("                       ")
    print("                       ")

infile.close()
