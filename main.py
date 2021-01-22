import os
import csv

#Create path for CSV

budget_path = os.path.join("Resources", "budget_data.csv")

totalmonths = 0
greatestinc = 0
greatestdec = 0
nettotal = 0
prevcol=867884
sumforavg=0

#Open and Read CSV File


with open(budget_path) as csvfile:
    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)

    # Read each row of data after the header

    for row in csvreader:
        totalmonths=totalmonths+1
        row[1]=int(row[1])
        nettotal=row[1] + nettotal
        change =  row[1]-prevcol
        prevcol = row[1]
        sumforavg = change + sumforavg
        if change > greatestinc:
            greatestinc = change
        if change < greatestdec:
            greatestdec = change

    avgchange= sumforavg / (totalmonths-1)
 
print("Financial Analysis\n")
print("------\n")
print("Total Months = ",totalmonths)
print("Total = ",nettotal)
print("Average change = ",avgchange)
print("Greatest Decrease = ",greatestdec) 
print("Greatest Increase = ",greatestinc) 

 
