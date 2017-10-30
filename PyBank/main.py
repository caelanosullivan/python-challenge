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

#Import dependencies

import os
import csv
import datetime

# Create file paths and dictionaries to store data

csv1_path = os.path.join('raw_data','budget_data_1.csv')
csv2_path = os.path.join('raw_data','budget_data_2.csv')

csv1_dict = {}
csv2_dict = {}

# Open CSVs, read in contents, add to dictionaries

with open(csv1_path, newline='') as csvfile:
    
    # CSV reader specifies delimiter and variable to hold contents
        csvreader = csv.reader(csvfile, delimiter=',')
        next(csvreader, None)

        # Loop through rows, converting dates to YYMM format and adding {date:rev} to dictionary
        for row in csvreader:
            date = datetime.datetime.strptime(row[0],'%b-%y').strftime('%y%m')
            csv1_dict[date] = int(row[1])

with open(csv2_path, newline='') as csvfile:
    
    # CSV reader specifies delimiter and variable that holds contents
        csvreader = csv.reader(csvfile, delimiter=',')
        next(csvreader, None)

    # Loop through rows, converting dates to YYMM format and adding {date:rev} to dictionary    
        for row in csvreader:
            date = datetime.datetime.strptime(row[0],'%b-%Y').strftime('%y%m')
            csv2_dict[date] = int(row[1])
        
## Create summary Counter dictionary of unique keys

from collections import Counter
A = Counter(csv1_dict)
B = Counter(csv2_dict)
A.update(B)

aggregated_dict = dict(A)

# Initialize variables to hold calculations

total_months = None
total_revenue = None
avg_monthly_rev_delta = None
monthly_increase_max = None
monthly_increase_max_name = None
monthly_decrease_max = None
monthly_decrease_max_name = None

# Calculate total number of months included in the dataset

total_months = len(aggregated_dict)

# Calculate total amount of revenue gained over the entire period

total_revenue = sum(aggregated_dict.values())

# Calculate average change in revenue between months over the entire period

months_in_period = list(aggregated_dict.keys())
monthly_rev_delta_dict = {}
i=1

while i < len(months_in_period):
    difference = aggregated_dict.get(months_in_period[i]) - aggregated_dict.get(months_in_period[i-1])
    k = months_in_period[i]
    monthly_rev_delta_dict[k] = difference
    i += 1

avg_monthly_rev_delta = sum(monthly_rev_delta_dict.values())/len(monthly_rev_delta_dict)

# Calculate greatest increase in revenue (date and amount) over the entire period

monthly_increase_max = max(monthly_rev_delta_dict, key=monthly_rev_delta_dict.get)
monthly_increase_max_name = str(monthly_increase_max)
monthly_increase_max_name = datetime.datetime.strptime(monthly_increase_max_name, '%y%m').strftime('%b-%y')

# Calculate greatest decrease in revenue (date and amount) over the entire period

monthly_decrease_max = min(monthly_rev_delta_dict, key=monthly_rev_delta_dict.get)
monthly_decrease_max_name = str(monthly_decrease_max)
monthly_decrease_max_name = datetime.datetime.strptime(monthly_decrease_max_name, '%y%m').strftime('%b-%y')

# Create variables and store calculation result statements

a = "------------------------------------------------------------------\n"
b = "Financial Analysis\n"
c = "------------------------------------------------------------------\n"
d = (f'Total Months: {total_months}\n')
e = (f'Total Revenue: ${total_revenue}\n')
f = (f'Average Revenue Change: ${avg_monthly_rev_delta:.0f}\n')
g = (f'Greatest Increase in Revenue: {monthly_increase_max_name}, ${monthly_rev_delta_dict[monthly_increase_max]}\n')
h = (f'Greatest Decrease in Revenue: {monthly_decrease_max_name}, ${monthly_rev_delta_dict[monthly_decrease_max]}\n')

# Print results to terminal and write to text file

print (a,b,c,d,e,f,g,h)

output_path = 'revenue_analysis.txt'
output_file = open(output_path, 'w')

output_file.write(a)
output_file.write(b)
output_file.write(c)
output_file.write(d)
output_file.write(e)
output_file.write(f)
output_file.write(g)
output_file.write(h)

output_file.close()