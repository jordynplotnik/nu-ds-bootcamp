import os
import csv

canidates = {}

totalVotes = 0
mostVotesCount = 0
mostVotesCanidate = ""

csvpath = os.path.join("Resources", "election_data.csv")

with open(csvpath, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    
    for row in csvreader:
        canidateName = row[2]
        totalVotes = totalVotes + 1

        if canidateName in canidates:
            canidates[canidateName] = canidates[canidateName] + 1
        else: 
            canidates[canidateName] = 1


# Text Print
output_path = os.path.join("Analysis", "PyPoll.csv")
with open(output_path, 'w') as txt_file:
        txt_file.write("Election Results")
        txt_file.write('\n')
        txt_file.write("--------------------------")
        txt_file.write('\n')
        txt_file.write("Total Votes: "+ str(totalVotes))
        txt_file.write('\n')
        txt_file.write("--------------------------")
        txt_file.write('\n')
        
        for key, value in canidates.items():

            if value > mostVotesCount:
                mostVotesCanidate = key
                mostVotesCount = value
            
            output = key + ": " + str(round(((value/totalVotes)*100),2)) + "% " + str(value)
            txt_file.write(output+ '\n')
        
        txt_file.write("--------------------------")
        txt_file.write('\n')
        txt_file.write("Winner: " + str(mostVotesCanidate))
        txt_file.write('\n')
        txt_file.write("--------------------------")

# Terminal Print

print("""Election Results
---------------------------""")
print("Total Votes: "+ str(totalVotes))
print("---------------------------")
for key, value in canidates.items():

    if value > mostVotesCount:
        mostVotesCanidate = key
        mostVotesCount = value
    
    output = key + ": " + str(round(((value/totalVotes)*100),2)) + "% " + str(value)
    print(output)
print("---------------------------")
print("Winner: " + str(mostVotesCanidate))
print("---------------------------")