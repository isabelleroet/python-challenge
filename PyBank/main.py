#import os allows user to interact with current os of user 
#import csv (comma separated values), most common import and export for spreadsheets and databases
import os
import csv
from statistics import mean 

#import cvs file 
#os.path.join combines path names into one complete path 
#create a place to hold your variables 
csvpath = os.path.join("Resources", "budget_data.csv")
MonthList = []
ProfitMargin = []

#skipping header in csv and formatting with empty lists from above
#next skips header row 
#row 0 is month and row 1 is profit 
#.append adds an item to the end of the list 
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    header = next(csvreader)
    for row in csvreader:
        MonthList.append(row[0])
        ProfitMargin.append(int(row[1]))

#read for loop and place monthly change in profit to empty list 
ProfitChange = []

#subtracting profit a from b and c from b and so on...'i' is for every iteration
for i in range (1,len(ProfitMargin)):
    ProfitChange.append(ProfitMargin[i]-ProfitMargin[i-1])

#Total Months
#len function returns number of items in an object 
TotalMonths = len(MonthList)

#Total
#sum function sums numbers in a list 
TotalProfitLoss = sum(ProfitMargin)

#Average Change
#mean function calculates mean/average of a given list  
AverageChange = mean(ProfitChange)

#Greatest Increase in Profits
#max function finds maximum value 
MaxProfit = max(ProfitChange)

#Greatest Decrease in Profits
#min function finds minimum value 
MinProfit = min(ProfitChange)

#month with greatest profit change
#index returns index of given element in list  
MaxMonth = MonthList[ProfitChange.index(MaxProfit) +1]

#month with most profit lost
#index returns index of given element in list  
MinMonth = MonthList[ProfitChange.index(MinProfit) +1]

#print results
#n is for spaces
print(f"Finacial Analysis \n------------------------\nTotal Months: {TotalMonths} \n\
Total: ${TotalProfitLoss} \nAverage Change: ${round(AverageChange, ndigits=2)} \n\
Greatest Profit Increase: {MaxMonth} $({MaxProfit}) \n\
Greatest Profit Decrease: {MinMonth} $({MinProfit})")

#with open command opens a file 
#write method writes a specified text to the file
with open("PyBank.txt", "w", newline="") as textfile:
    textfile.write(f"Finacial Analysis \n------------------------\nTotal Months: {TotalMonths} \n\
Total: ${TotalProfitLoss} \nAverage Change: ${round(AverageChange, ndigits=2)} \n\
Greatest Profit Increase: {MaxMonth} $({MaxProfit}) \n\
Greatest Profit Decrease: {MinMonth} $({MinProfit})")