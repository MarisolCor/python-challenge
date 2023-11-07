#Challenge 3 python Election Result 
#Marisol Cornejo
# Import os and csv module
import os
import csv
#File path
absolute_path = os.path.dirname(__file__)
csvpath = os.path.join(absolute_path,'Resources', 'election_data.csv')
output_path = os.path.join(absolute_path, "analysis", "analysis_election.csv")
# variables
total_votes=0
total_votes_charles=0
total_votes_diana=0
total_votes_raymon=0
total_votes_charles_pct=0
total_votes_diana_pct=0
total_votes_raymon_pct=0
winner=""
#Read csv file
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
#loop through the rows
    for row in csvreader:
       total_votes=total_votes+1
       if  row[2]=="Charles Casper Stockham":
           total_votes_charles+=1
       elif row[2]=="Diana DeGette":
           total_votes_diana+=1
       elif row[2]=="Raymon Anthony Doane":
           total_votes_raymon+=1

#Loop Ends 
#Calculations
    total_votes_charles_pct=(total_votes_charles*100)/total_votes
    total_votes_diana_pct=(total_votes_diana*100)/total_votes
    total_votes_raymon_pct=(total_votes_raymon*100)/total_votes
    if total_votes_charles_pct>total_votes_diana_pct and  total_votes_charles_pct>total_votes_raymon_pct:
        winner="Charles Casper Stockham"
    if total_votes_diana_pct>total_votes_charles_pct and  total_votes_diana_pct>total_votes_raymon_pct:
        winner="Diana DeGette"
    if total_votes_raymon_pct>total_votes_diana_pct and  total_votes_charles_pct<total_votes_raymon_pct:
        winner="Raymon Anthony Doane"   

#Print results
    print("--------------------")
    print("Election Results")
    print("--------------------")
    print(f"Total Votes: {total_votes}")
    print(f"Charles Casper Stockham: {total_votes_charles_pct}%  ({str(total_votes_charles)})")
    print(f"Diana DeGette: {total_votes_diana_pct}%   ({str(total_votes_diana)})")
    print(f"Raymon Anthony Doane:{total_votes_raymon_pct}%   ({str(total_votes_raymon)})")
    print(f"Winner: {winner}")
    print("--------------------------------------------------------------") 

# Write the output to as csv
with open(output_path, 'w') as csvfile:
    csvwriter = csv.writer(csvfile, delimiter=',')
    csvwriter.writerow(['Election Results'])
    csvwriter.writerow(['Total Votes: ',total_votes])
    csvwriter.writerow(['Charles Casper Stockham:',str(total_votes_charles_pct)+"%("+ str(total_votes_charles)+")"])
    csvwriter.writerow(['Diana DeGette: ',str(total_votes_diana_pct)+"%("+ str(total_votes_diana)+")"])
    csvwriter.writerow(['Raymon Anthony Doane',str(total_votes_raymon_pct)+"% ("+ str(total_votes_raymon)+")"])
    csvwriter.writerow(['Winner:',winner])
   
