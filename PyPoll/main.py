import os
import csv

#defines input file and path
election_data_csv = os.path.join("..","Resources", "election_data.csv")

#defines output path and file name
output_data_csv = os.path.join("pyPoll_output.csv")

#set up lists
voterList = []
countyList = []
candidateList = []

#Open file, identify header, create lists
with open(election_data_csv,'r') as electionCSV:
    
    electionRead = csv.reader(electionCSV, delimiter=',')

    header = next(electionRead)

    for row in electionRead:
        #appends each voterID from first column
        voterList.append(row[0])
        #appends each county from 2nd column
        countyList.append(row[1])
        #appends each candidate from 3rd column
        candidateList.append(row[2])

#Calculate total # of votes
totalVotes = len(voterList)

### CANDIDATE LISTS
#Creating a list for each candidate - will use len later to perform calculations
khanList = []
correyList = []
liList = []
otooleyList = []

for r in range(len(candidateList)):
        
    if 'Khan' in candidateList[r]:
        khanList.append(candidateList[r])
    elif 'Correy' in candidateList[r]:
        correyList.append(candidateList[r])
    elif 'Li' in candidateList[r]:
        liList.append(candidateList[r])
    elif "O'Tooley" in candidateList[r]:
        otooleyList.append(candidateList[r])

### CANDIDATE RESULTS
#create LENs for each candidate and perform calculations
khanListLEN = int(len(khanList))
correyListLEN = int(len(correyList))
liListLEN = int(len(liList))
otooleyListLEN = int(len(otooleyList))

khanPercent = (khanListLEN / totalVotes) * 100
khanPercent = str(round(khanPercent,3))

correyPercent = (correyListLEN / totalVotes) * 100
correyPercent = str(round(correyPercent,3))

liPercent = (liListLEN / totalVotes) * 100
liPercent = str(round(liPercent,3))

otooleyPercent = (otooleyListLEN / totalVotes) * 100
otooleyPercent = str(round(otooleyPercent,3))

### WINNER - PART 1
#Grabbed unique candidates 
#originally wanted to bounce against the candidate list and count only values that matched 0,1,2,3
#Ended up using below to call
candidateUnique = []
for r in range(len(candidateList)):
        
    if candidateList[r] not in candidateUnique:
        candidateUnique.append(candidateList[r])

#checked the print order to coordinate 'resultCounts' 
#print(candidateUnique)

resultCounts = [khanListLEN,correyListLEN,liListLEN,otooleyListLEN]

### WINNER - PART 2
#probably a cleaner way to pull all of this, but kind of built things in chunks 
#and then mooshed them together
#Setting a new variable winnerCount up to determine the highest count from resultCounts
#Since results and unique candidates are in sync it picks the correct candidate as it loops through
winnerCount = 0
for r in range(len(resultCounts)):
    if resultCounts[r] > winnerCount:
        winnerCount = resultCounts[r]
        winner = candidateUnique[r]
#print(winnerCount,winner)

### PRINT
print("Election Results")
print('-' * 26)
print(f"Total Votes: {totalVotes}")
print('-' * 26)
print(f"Khan: {khanPercent}% ({khanListLEN})")
print(f"Correy: {correyPercent}% ({correyListLEN})")
print(f"Li: {liPercent}% ({liListLEN})")
print(f"O'Tooley: {otooleyPercent}% ({otooleyListLEN})")
print('-' * 26)
print(f"Winner: {winner}")
print('-' * 26)

### Setting up outputs
with open(output_data_csv, mode='w', newline='') as summary_txt:
    writer = csv.writer(summary_txt)

    writer.writerows([
        ["Election Results"],
        ['-' * 26],
        [f"Total Votes: {totalVotes}"],
        ['-' * 26],
        [f"Khan: {khanPercent}% ({khanListLEN})"],
        [f"Correy: {correyPercent}% ({correyListLEN})"],
        [f"Li: {liPercent}% ({liListLEN})"],
        [f"O'Tooley: {otooleyPercent}% ({otooleyListLEN})"],
        ['-' * 26],
        [f"Winner: {winner}"],
        ['-' * 26],
    ])