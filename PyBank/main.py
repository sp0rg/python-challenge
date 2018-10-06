
import os
import csv

#defines input path
budget_data_csv = os.path.join("..","Resources", "budget_data.csv")
#defines output path
output_data_csv = os.path.join("pyBank_output.csv")

#define two empty lists for the months and revenue
#bankMonths - list for each month/year combo
#bankRevenue - list for rev each month
bankMonths = []
bankRevenue = []

#read and break up
#didn't do this initially and realized I wasn't
#able to populate my lists
#https://docs.python.org/3/library/csv.html
with open(budget_data_csv,'r') as budgetCSV:
    
    budgetRead = csv.reader(budgetCSV, delimiter=',')

    header = next(budgetRead)

    for row in budgetRead:
        #appends each month from first column
        bankMonths.append(row[0])
        #appends each rev amt from second column as integer
        bankRevenue.append(int(row[1]))

#
totalMonths = len(bankMonths)
#print(bankMonths,bankRevenue) #just to validate that
#this hot mess is actually kind of working

##### Finding the Net revenue
netPL = 0
#for y in range(len(bankRevenue)):
#    netPL.append(y)
#return netPL
#print(int(netPL)
#insted of r had rev, shortened for simplification
#used the length of bankRevenue list to make range for
#number of times to cycle through
for r in range(len(bankRevenue)):
    netPL += bankRevenue[r]

###### Finding increase/decreast most-est
incMost = bankRevenue[0]
decMost = bankRevenue[0]
monthInc = bankMonths[0]
monthDec = bankMonths[0]

#used same mechanism as calculating net prof/loss
#could possible include netPL at the end of the statement
#did not have the subtraction in there at first
#for decrease had to add the subtraction to the elif
#not sure why!!!
for r in range(len(bankRevenue)):
    if bankRevenue[r] >= incMost:
        incMost = bankRevenue[r] - bankRevenue[r - 1]
        monthInc = bankMonths[r]
    elif bankRevenue[r]  - bankRevenue[r - 1] <= decMost:
        decMost = bankRevenue[r] - bankRevenue[r - 1]
        monthDec = bankMonths[r]

###### AVERAGE SECTION
avgrevChange = []
moreAvg = 0
somewhatAvg = 0
bobeatsBroccoli = 0 #there are only so many ways to say average
removeCarrots = 0 #tired of broccoli? bring on the carrots!

#calculation to add each iteration of difference
for r in range(len(bankRevenue)): 
    if avgrevChange != 0:
        bobeatsBroccoli =  bankRevenue[r] - bankRevenue[r - 1]
        avgrevChange.append(bobeatsBroccoli)

#kept coming up with zero
#assumed that subtracting first row from last row it would throw the sum off later
#dug around on the interwebs a bit, but it makes sense
#zero indexed takes the first row minus the very last row (-1)
removeCarrots = bankRevenue[0] - bankRevenue[-1]

#This gets our net - still need to remove those carrots
for r in range(len(avgrevChange)):
    moreAvg += avgrevChange[r]

#takes removes the carrots to get a proper net value
evenmoreAvg = moreAvg - removeCarrots

#divide for average, then round and all that jazz
#had to account that there really should only be 85 pairs of differences
#when we removed carrots we took the list from 86 to 85 :)
somewhatAvg = evenmoreAvg / (totalMonths - 1)
somewhatRnd = str(round(somewhatAvg,2))

###### Print Section
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {totalMonths}")
print(f"Total: ${netPL}")
print(f"Average Change: ${somewhatRnd}")
print(f"Greatest Increase in Profits: {monthInc} (${incMost})")
print(f"Greatest Decrease in Profits: {monthDec} (${decMost})")
 
with open(output_data_csv, mode='w', newline='') as summary_txt:
    writer = csv.writer(summary_txt)

    writer.writerows([
        ["Financial Analysis"],
        ['-' * 28],
        [f"Total Months: {totalMonths}"],
        [f"Total: ${netPL}"],
        [f"Average Change: ${somewhatRnd}"],
        [f"Greatest Increase in Profits: {monthInc} (${incMost})"],
        [f"Greatest Decrease in Profits: {monthDec} (${decMost})"]
    ])

    #* In addition, your final script should both print the analysis to the terminal 
    ## and export a text file with the results.