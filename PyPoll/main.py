import os
import csv

csvpath = os.path.join("Resources", "election_data.csv")

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    header = next(csvreader)
    
    # prepare variables
    ballotids = []  # generate list named "ballotid" for "ballotid" column
    counties = []  # generate list named "county" for "county" column
    candidates = []  # generate list named "candidates" for "candidate" column
    candidatenames = []  # generate list for candidate names
    total = []  # generate list for total votes found for each candidate
    resultprint = []  # generate list for result printout of each found candidate
    percentage = []  # generate list for percentage of votes found for each candidate
    
    # set start conditions
    line_count = 0
    winnervotes = 0
    loop1 = 0
    loop2 = 0
    loop3 = 0
    loop4 = 0
    
    # Read in each row of data after the header and write data into assigned lists
    for row in csvreader:
        ballotid = row[0]  # assign column 0 as ballot id
        county = row[1]  # assign column 1 as county
        candidate = row[2]  # assign column 2 as candidate
        ballotids.append(ballotid)  # add next line to list ballotids
        counties.append(county)  # add next line to list counties
        candidates.append(candidate)  # add next line to list candidates
    
    line_count = len(ballotids)  # count the total number of votes cast in the "ballot id" column
    
    # begin data analysis
    candidatenames.append(candidates[0])  # pre-load candidate names for comparison
    
    # first loop runs through list of candidates to determine candidates voted for
    for loop1 in range(line_count - 1):
        if candidates[loop1 + 1] != candidates[loop1] and candidates[loop1 + 1] not in candidatenames:
            candidatenames.append(candidates[loop1 + 1])
    
    n = len(candidatenames)
    
    # second loop runs through total votes of candidates and adds to list total
    for loop2 in range(n):  # range of loop depending on how many candidates found
        total.append(candidates.count(candidatenames[loop2]))
    
    for loop3 in range(n):  # range of loop depending on how many candidates found
        percentage.append(f"{round((total[loop3]/line_count*100), 3)}%")  # Calculate % per candidate found
        if total[loop3] > winnervotes:  # find candidate with highest vote count
            winner = candidatenames[loop3]
            winnervotes = total[loop3]
    
    # Fourth loop variable loop4 as loop index counter
    for loop4 in range(n):
        resultprint.append(f"{candidatenames[loop4]}: {percentage[loop4]} ({total[loop4]})")  # format list resultprint
    
    resultlines = "\n".join(resultprint)  # prepare new combined list of results for printout

#print results, n is for spaces
analysis=f'\
Election Results\n\
----------------------------\n\
Total Votes: {line_count}\n\
----------------------------\n\
{resultlines}\n\
----------------------------\n\
Winner: {winner} :)\n\
----------------------------\n'

print(analysis) #output results on screen

#write into text file named pypoll.txt
file1=open("pypoll.txt", "w") #open or if file does not exist then create a file named pypoll.txt
file1.writelines(analysis) #write analysis into pypoll.txt
file1.close() #close pypoll.txt write mode