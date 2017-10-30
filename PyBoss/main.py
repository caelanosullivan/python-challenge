# -*- coding: UTF-8 -*-
"""PyBoss

This module reads in two CSVs of employee records and converts them to the required format.

Conversions include:
- The Name column should be split into separate First Name and Last Name columns.
- The DOB data should be re-written into DD/MM/YYYY format.
- The SSN data should be re-written such that the first five numbers are hidden from view.
- The State data should be re-written as simple two-letter abbreviations.

Finally, it exports a CSV file of the results.

Example:

  $ python main.py

"""

#Import dependencies

import os
import csv
import datetime

# Create file paths

csv1_path = os.path.join('raw_data','employee_data1.csv')
csv2_path = os.path.join('raw_data','employee_data2.csv')

# Create empty lists for original column data:
EmpID_original = []
Name_original =[]
DOB_original = []
SSN_original = []
State_original = []

SSN_orig = None

# Create empty lists for new columns:

DOB_formatted = None
SSN_formatted = None

Name_first = []
Name_last = []
DOB_reformat = []
SSN_hidden = []
State_abbrev = []

## Write 2 functions - one to clean data, one to append to lists and zip.
## DOB in plain text format: 1970-05-24

# Function to reformat per-row records


# Function to add row stuff to lists
def reformat_employee_record(employee_record_row):
    
    # Append employee ID to list
    EmpID_original.append(row[0])

    # Split name column into first and last; append to lists

    Name_original = row[1].split(" ")

    Name_first.append(Name_original[0])
    Name_last.append(Name_original[1])

    # Reformat DOB; append to list

    DOB_formatted = datetime.datetime.strptime(row[2],'%Y-%m-%d').strftime('%d/%m/%Y')
    DOB_reformat.append(DOB_formatted)

    # Create new SSN strings using last 4 digits preceded by ***-**-; append to list
    
    SSN_orig = row[3]
    SSN_formatted = (f'***-**-{SSN_orig[7:]}')
    SSN_hidden.append(SSN_formatted)

# Open CSVs, read in contents

with open(csv1_path, newline='') as csvfile:
    
    # CSV reader specifies delimiter and variable to hold contents
        csvreader = csv.reader(csvfile, delimiter=',')
        next(csvreader, None)

        # Loop through rows, converting dates to YYMM format and adding {date:rev} to dictionary
        for row in csvreader:
            reformat_employee_record(row)

## Zip lists into tuples
employee_tuples = zip(EmpID_original,Name_first, Name_last, DOB_reformat, SSN_hidden)

# Set variable for output file
output_file = os.path.join("employees_cleaned.csv")

#opens it
with open(output_file, "w", newline="") as datafile:
    csvwriter = csv.writer(datafile)
    
    #Write header row
    csvwriter.writerow(['Emp ID', 'First Name', 'Last Name','DOB','SSN','State'])

    #Write following rows
    csvwriter.writerows(employee_tuples)

##change open("learner.csv", "w") to open("learner.csv", "a")


### Need code for second CSV

## Write first set of data, call fxn again, APPEND second set.


