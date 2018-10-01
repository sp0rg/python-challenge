
import os
import csv

budget_data_csv = os.path.join("..","Resources", "budget_data.csv")

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

#increase/decreast most-est variables
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
#print(incMost,monthInc) #test results - rev is off
#print(decMost,monthDec) #test results - rev is off

#print(netPL)
#print(totalMonths)   #test the total - it works 
#header = next(budget_data_csv)
#Your task is to create a Python script that analyzes the records to calculate each of 
# the following:
#def getBankTotal(BankData):
  #* The total number of months included in the dataset
    #totalMonths = []#(BankData[0])
    #for x in(BankData[0]):
        #if x not in totalMonths:#.count(x):
            #totalMonths.append(x)
    #return totalMonths
    #print(len(totalMonths)-1)
    
    #for months in totalMonths:
     #   print(months)
    #print (x)
    #print totalMonths
    #totalMonths = (BankData[0])
 # * The total net amount of "Profit/Losses" over the entire period
    #netPL = []
    #for y in (BankData[1]):
        #netPL.append(y)
    #return netPL
    #print(int(netPL)
 
 # * The average change in "Profit/Losses" between months over the entire period
#avgChange = round(netPL/int(totalMonths), 2)
#maybe need to do something nested?
#like variance = value[r+1]-value[r]
#or take evens minus odds? and add the differences together?
#then take that and divide by months
#for r in range(len(bankRevenue)):
    #if bankRevenue[r] >= incMost:
        #incMost = bankRevenue[r]
        #monthInc = bankMonths[r]
    #elif bankRevenue[r] <= decMost:
        #decMost = bankRevenue[r]
        #monthDec = bankMonths[r]
#print(avgChange) #doesn't match given output
 
 # * The greatest increase in profits (date and amount) over the entire period

 # * The greatest decrease in losses (date and amount) over the entire period

#* As an example, your analysis should look similar to the one below:
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {totalMonths}")
print(f"Total: ${netPL}")
#print(f"Average Change: ${avgChange}")
print(f"Greatest Increase in Profits: {monthInc} (${incMost})")
print(f"Greatest Decrease in Profits: {monthDec} (${decMost})")
 # text
 # Financial Analysis
 # ----------------------------
 # Total Months: 86
 # Total: $38382578
 # Average  Change: $-2315.12
 # Greatest Increase in Profits: Feb-2012 ($1926159)
 # Greatest Decrease in Profits: Sep-2013 ($-2196167)


    #* In addition, your final script should both print the analysis to the terminal 
    ## and export a text file with the results.