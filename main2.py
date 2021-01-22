
import os
import csv


totals = {}
percentages = {}

csvpath = os.path.join(".", "Resources", "election_data.csv")  

totals["Khan"] = 0
totals["O'Tooley"] = 0
totals["Li"] = 0
totals["Correy"] = 0
total_vote = 0

with open(csvpath) as csvfile:
    csv_reader = csv.reader(csvfile, delimiter = ",")
    csv_header = next(csv_reader)

    for row in csv_reader:
        total_vote = total_vote + 1
        candidate = row[2]
        totals[candidate] += 1

    for candidate in totals:
        percentages[candidate] = totals[candidate] / total_vote * 100
        print(candidate, " Total = ", totals[candidate], " Percentage = ", percentages[candidate], "%")

    print("Winner = ", max(totals, key=totals.get))

    
