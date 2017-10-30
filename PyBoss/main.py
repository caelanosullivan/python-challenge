# -*- coding: UTF-8 -*-
"""PyBoss

This module reads in two CSVs of employee records and converts them to the required format.

Conversions include:
- The Name column split into separate First Name and Last Name columns.
- The DOB data re-written into DD/MM/YYYY format.
- The SSN data re-written such that the first five numbers are hidden from view.
- The State data re-written as simple two-letter abbreviations.

Finally, it creates a CSV file of the results.

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

# Create needed variables and empty lists for original column data:
EmpID_original = []
Name_original =[]

SSN_orig = None

# Create needed variables and empty lists for new columns:

Name_first = []
Name_last = []
DOB_reformat = []
SSN_hidden = []
State_abbrev = []

DOB_formatted = None
SSN_formatted = None
State_formatted = None

# Dictionary of state names for conversions

us_state_abbrev = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY',
}

# Function to add employee row data to lists
def reformat_employee_record(employee_record_row):
    
    # Append employee ID to list

    EmpID_original.append(row[0])

    # Split name column into first and last; append to respective lists

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

    # Convert state names to two-letter abbrevations; append to list

    State_formatted = us_state_abbrev.get(row[4])
    State_abbrev.append(State_formatted)

# Open first CSV, read in contents

with open(csv1_path, newline='') as csvfile:
    
    # CSV reader specifies delimiter and variable to hold contents
        csvreader = csv.reader(csvfile, delimiter=',')
        next(csvreader, None)

        # Loop through rows, running function on each row to convert and append
        for row in csvreader:
            reformat_employee_record(row)

# Zip lists into tuples
employee_tuples = zip(EmpID_original,Name_first, Name_last, DOB_reformat, SSN_hidden, State_abbrev)

# Set variable for output file
output_file = os.path.join("employees_cleaned.csv")

# Open output file in write mode for population of first CSV cleaned data
with open(output_file, "w", newline="") as datafile:
    csvwriter = csv.writer(datafile)
    
    #Write header row
    csvwriter.writerow(['Emp ID', 'First Name', 'Last Name','DOB','SSN','State'])

    #Write employee data rows
    csvwriter.writerows(employee_tuples)

# Reset lists to empty in preparation for second CSV content

EmpID_original = []
Name_original =[]
Name_first = []
Name_last = []
DOB_reformat = []
SSN_hidden = []
State_abbrev = []

# Open second CSV, read in contents
with open(csv2_path, newline='') as csvfile:
    
    # CSV reader specifies delimiter and variable to hold contents
        csvreader = csv.reader(csvfile, delimiter=',')
        next(csvreader, None)

        # Loop through rows, running function on each row to convert and append
        for row in csvreader:
            reformat_employee_record(row)

# Zip lists into tuples
employee_tuples = zip(EmpID_original,Name_first, Name_last, DOB_reformat, SSN_hidden, State_abbrev)

# Open output file in append mode for population of second CSV cleaned data
with open(output_file, "a", newline="") as datafile:
    csvwriter = csv.writer(datafile)
    
    #Write employee data rows
    csvwriter.writerows(employee_tuples)