#Challenge 3 python Bank Analysis 
#Marisol Cornejo
# Import the datetime, os,and csv module
import datetime
import os
import csv
#File path
absolute_path = os.path.dirname(__file__)
csvpath = os.path.join(absolute_path,'Resources', 'budget_data.csv')
output_path = os.path.join(absolute_path, "analysis", "analysis_bank.csv")
# variables
total_months=0
net_total=0
initial_value=0
final_value=0
calculations=[]
dates=[]
average_change=0 
increse=0
decrease=0
increse_date=0
decrease_date=0
#Read csv file
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
#loop through the rows
    for row in csvreader:
       total_months=total_months+1 
       net_total=net_total+int(row[1])
       final_value=int(row[1])
       calculations.append(final_value-initial_value)
       initial_value=final_value
       dates.append(row[0])
#Loop Ends 
#Calculations
    dates=dates[1::]
    less1=calculations[1::]
    average_change=sum(less1)/len(less1)
    increse=max(less1)
    decrease=min(less1)
    increse_date=dates[less1.index(increse)]
    decrease_date=dates[less1.index(decrease)]
#Print results
    print("--------------------")
    print("Financial Analysis")
    print("--------------------")
    print(f"Total months: {total_months}")
    print(f"Total: ${net_total}")
    print(f"Average change: ${average_change}")
    print(f"Greatest Increase in Profits:{increse_date} ${increse}")
    print(f"Greatest Decrease in Profits:{decrease_date} ${decrease}")
    print("--------------------------------------------------------------")
# Write the output to as csv
with open(output_path, 'w') as csvfile:
    csvwriter = csv.writer(csvfile, delimiter=',')
    csvwriter.writerow(['Financial Analysis'])
    csvwriter.writerow(['Total months: ',total_months])
    csvwriter.writerow(['Total: $',net_total])
    csvwriter.writerow(['Average change: $ ',average_change])
    csvwriter.writerow(['Greatest Increase in Profits:',increse_date ,'$'+str(increse)])
    csvwriter.writerow(['Greatest Increase in Profits:',decrease_date ,'$'+str(decrease)])
   
