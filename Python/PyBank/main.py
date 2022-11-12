import os
import csv

date = []
profitloss = []
csvData = []
plChange = []

csvpath = os.path.join("Resources", "budget_data.csv")

with open(csvpath, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    # print(csvreader)

    csvheader = next(csvreader)
    # print(f"CSV Header: {csvheader}")

    for row in csvreader:
        date.append(row[0])
        profitloss.append(int(row[1]))
        csvData.append(row[:])

for x in range(1,len(profitloss)):
    plChange.append(int(profitloss[x])-int(profitloss[x-1]))

ttl = sum(profitloss)
avg = round((sum(plChange))/(len(date)),2)

increaseCalc = int(max(plChange))
decreaseCalc = int(min(plChange))

increaseRow = int(plChange.index(increaseCalc))
decreaseRow = int(plChange.index(decreaseCalc))


print("""Financial Analysis
--------------------------""")
print("Total Months: " + str((len(date))))
print(f"Total: ${ttl}")
print(f"Average: ${avg}")
print("Greatest Increase in Profits: " + str(csvData[increaseRow+1]))
print("Greatest Decrease in Profits: " + str(csvData[decreaseRow+1]))

output_path = os.path.join("Analysis", "PyBank.txt")
with open(output_path, 'w') as txt_file:
        txt_file.write("Financial Analysis")
        txt_file.write('\n')
        txt_file.write("--------------------------")
        txt_file.write('\n')
        txt_file.write("Total Months: " + str((len(date))))
        txt_file.write('\n')
        txt_file.write(f"Total: ${ttl}")
        txt_file.write('\n')
        txt_file.write(f"Average: ${avg}")
        txt_file.write('\n')
        txt_file.write("Greatest Increase in Profits: " + str(csvData[increaseRow+1]))
        txt_file.write('\n')
        txt_file.write("Greatest Decrease in Profits: " + str(csvData[decreaseRow+1]))
