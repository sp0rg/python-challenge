import os
import csv

election_data_csv = os.path.join("..","Resources", "election_data.csv")

#define two empty lists for the months and revenue
#bankMonths - list for each month/year combo
#bankRevenue - list for rev each month
voterList = []
countyList = []
candidateList = []

#read and break up
#didn't do this initially and realized I wasn't
#able to populate my lists
#https://docs.python.org/3/library/csv.html
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

print("Election Results")
print("-------------------------")

#Calculate and print total votes
totalVotes = len(voterList)
print(f"Total Votes: {totalVotes}")
print("-------------------------")

#Grabbed unique candidates - not sure that this adds any value
#originally wanted to bounce against the candidate list and count only values that matched 0,1,2,3
candidateUnique = []
for r in range(len(candidateList)):
        
    if candidateList[r] not in candidateUnique:
        candidateUnique.append(candidateList[r])
                
#print(candidateUnique)

khanList = []
for r in range(len(candidateList)):
        
    if 'Khan' in candidateList[r]:
        khanList.append(candidateList[r])
                
khanListLEN = int(len(khanList))
#print(khanListLEN)

khanPercent = (khanListLEN / totalVotes) * 100
khanPercent = str(round(khanPercent,3))
#print(khanPercent)
print(f"Khan: {khanPercent}% ({khanListLEN})")

correyList = []
for r in range(len(candidateList)):
        
    if 'Correy' in candidateList[r]:
        correyList.append(candidateList[r])
                
correyListLEN = int(len(correyList))
#print(correyListLEN)

correyPercent = (correyListLEN / totalVotes) * 100
correyPercent = str(round(correyPercent,3))
print(f"Correy: {correyPercent}% ({correyListLEN})")

liList = []
for r in range(len(candidateList)):
        
    if 'Li' in candidateList[r]:
        liList.append(candidateList[r])
                
liListLEN = int(len(liList))
#print(liListLEN)

liPercent = (liListLEN / totalVotes) * 100
liPercent = str(round(liPercent,3))
#print(liPercent)
print(f"Li: {liPercent}% ({liListLEN})")


otooleyList = []
for r in range(len(candidateList)):
        
    if "O'Tooley" in candidateList[r]:
        otooleyList.append(candidateList[r])
                
otooleyListLEN = int(len(otooleyList))
#print(otooleyListLEN)

otooleyPercent = (otooleyListLEN / totalVotes) * 100
otooleyPercent = str(round(otooleyPercent,3))
#print(otooleyPercent)
print(f"O'Tooley: {otooleyPercent}% ({otooleyListLEN})")
print("-------------------------")



#print("Election Results")
#print("-------------------------")
#print("Total Votes: {totalVotes}")
#print("-------------------------")
#
 #Election Results
#  -------------------------
 # Total Votes: 3521001
#  -------------------------
# Khan: 63.000% (2218231)
 # Correy: 20.000% (704200)
 # Li: 14.000% (492940)
 # O'Tooley: 3.000% (105630)
 # -------------------------
#  Winner: Khan
#  -------------------------