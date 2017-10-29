# -*- coding: UTF-8 -*-
"""PyBank

This module reads in two user-supplied revenue datasets (.csv) with columns Date and Revenue.

It normalizes and combines the data, then calculates:
- The total number of months included in the dataset
- The total amount of revenue gained over the entire period
- The average change in revenue between months over the entire period
- The greatest increase in revenue (date and amount) over the entire period
- The greatest decrease in revenue (date and amount) over the entire period

Finally, it returns the analysis to the terminal and exports a text file of the results.

Example:

  $ python main.py

"""

# datetime.datetime.strptime("2013-1-25", '%Y-%m-%d').strftime('%m/%d/%y')
# '01/25/13'

### IMPROVEMENTS:
## Intake any number of budget csvs (with a loop? function?)

#Import dependencies

import os
import csv
import datetime

# Display initial instructions and collect .csv files from user

# print("------------------------------------------------------------------")
# print("Please enter two CSV files for revenue data analysis.")
# budget1_csv = input("First CSV file: ")
# budget2_csv = input("Second CSV file: ")

# Create file paths and dictionaries to store data

# csv1_path = os.path.join('raw_data',budget1_csv)
# csv2_path = os.path.join('raw_data',budget2_csv)

csv1_path = os.path.join('raw_data','budget_data_1.csv')
csv2_path = os.path.join('raw_data','budget_data_2.csv')

csv1_dict = {}
csv2_dict = {}

# Block to open CSVs, read in contents, add to dictionaries
with open(csv1_path, newline='') as csvfile:
    
    # CSV reader specifies delimiter and variable that holds contents
        csvreader = csv.reader(csvfile, delimiter=',')
        next(csvreader, None)

        # Loop through rows, converting dates to YYMM format and adding {date:rev} to dictionary
        for row in csvreader:
            #date = row[0]
            date = datetime.datetime.strptime(row[0],'%b-%y').strftime('%y%m')
            #csv1_dict[(row[0])]=(row[1])
            csv1_dict[date] = int(row[1])
        
        #print(csv1_dict)

with open(csv2_path, newline='') as csvfile:
    # CSV reader specifies delimiter and variable that holds contents
        csvreader = csv.reader(csvfile, delimiter=',')
        next(csvreader, None)
        #print(f'Date is {date}')

        for row in csvreader:
            date = datetime.datetime.strptime(row[0],'%b-%Y').strftime('%y%m')
            csv2_dict[date] = int(row[1])
        
        #print(csv2_dict)

## Create summary dictionary of unique keys

from collections import Counter
A = Counter(csv1_dict)
B = Counter(csv2_dict)
A.update(B)

aggregated_dict = dict(A)
#Sprint("Summary dict: ",aggregated_dict)

# Initialize variables to hold calculations
total_months = None
total_revenue = None
avg_monthly_rev_delta = None
monthly_increase_max = None
monthly_decrease_max = None

# Calculate total number of months included in the dataset

total_months = len(aggregated_dict)
#print(f'Total months: {total_months}')

# Calculate total amount of revenue gained over the entire period

total_revenue = sum(aggregated_dict.values())
#print(f'Total: {total_revenue}')

# Calculate average change in revenue between months over the entire period

months_in_period = list(aggregated_dict.keys())
monthly_rev_delta_dict = {}
i=1

while i < len(months_in_period):
    difference = aggregated_dict.get(months_in_period[i]) - aggregated_dict.get(months_in_period[i-1])
    k = months_in_period[i]
    monthly_rev_delta_dict[k] = difference
    i += 1
#print(monthly_rev_delta_dict)

avg_monthly_rev_delta = sum(monthly_rev_delta_dict.values())/len(monthly_rev_delta_dict)
#print(avg_monthly_rev_delta)

##### TEST CODE
# print(months_in_period)
# months_in_period.sort()
# print('Months:',months_in_period)
# list.sort() # permanent
# print(months_in_period[2])
# month2 = aggregated_dict.get(months_in_period[2])
# month1 = aggregated_dict.get(months_in_period[1])
# # print(month2)
# # print(month1)
# # print(month2-month1)
# difference = aggregated_dict.get(months_in_period[2]) - aggregated_dict.get(months_in_period[1])
# print(difference)

# monthly_rev_delta_dict = {}
# for i in range(len(months_in_period)):

#     difference = aggregated_dict.get(months_in_period[i+1]) - aggregated_dict.get(months_in_period[i])
#     #monthly_rev_delta_dict[months_in_period(i+1)] = difference
#     print(difference)
#     i += 1

# Calculate greatest increase in revenue (date and amount) over the entire period

monthly_increase_max = max(monthly_rev_delta_dict, key=monthly_rev_delta_dict.get)

# print('greatest increase:', monthly_increase_max)
# print('val:', monthly_rev_delta_dict[monthly_increase_max])

    #print(monthly_increase_max, monthly_rev_delta_dict[monthly_increase_max])

# Calculate greatest decrease in revenue (date and amount) over the entire period
monthly_decrease_max = min(monthly_rev_delta_dict, key=monthly_rev_delta_dict.get)

# print('greatest decrease:', monthly_decrease_max)
# print('val:', monthly_rev_delta_dict[monthly_decrease_max])


## Open CSVs -- loop way, not finished.

#file_paths = []
#file_paths = [csv_path1, csv_path2]

# for path in file_paths:
#     with open(path, newline='') as csvfile:
#     # CSV reader specifies delimiter and variable that holds contents
#         csvreader = csv.reader(csvfile, delimiter=',')

#         for row in csvreader:
#             #Add cols, rows to dictionary...but how to create 2+ dicts?

# Output statements


# x = 3.14159265
# print(f'pi = {x:.2f}')

print("------------------------------------------------------------------")
print("Financial Analysis")
print("------------------------------------------------------------------")
print(f'Total Months: {total_months}')
print(f'Total Revenue: {total_revenue}')
print(f'Average Revenue Change: ${avg_monthly_rev_delta:.0f}')
print(f'Greatest Increase in Revenue: {monthly_increase_max}, ${monthly_rev_delta_dict[monthly_increase_max]})')
print(f'Greatest Decrease in Revenue: {monthly_decrease_max}, ${monthly_rev_delta_dict[monthly_decrease_max]}')