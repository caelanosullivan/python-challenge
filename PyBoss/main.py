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

# Create empty lists for new columns:

DOB_formatted = None

Name_first = []
Name_last = []
DOB_reformat = []
SSN_hidden = []
State_abbrev = []

## Write 2 functions - one to clean data, one to append to lists and zip.
## DOB in plain text format: 1970-05-24

# Function to reformat per-row records

def 

# Function to add row stuff to lists
def reformat(employee_record_row):
    
    # Append employee ID to list
    EmpID_original.append(row[0])

    # Split name column into first and last; append to lists

    Name_original = row[1].split(" ")

    Name_first.append(Name_original[0])
    Name_last.append(Name_original[1])

    # Reformat DOB; append to list

    DOB_formatted = datetime.datetime.strptime(row[2],'%Y-%m-%d').strftime('%d/%m/%Y')
    DOB_reformat.append()

    # append appropriate cells to categorized lists
    Title.append(row[1])
    Price.append(row[4])
    Subscriber_Count.append(row[5])
    Number_of_Reviews.append(row[6])
    #Parse the course length column by splitting on space, 
    # then append the 0th item in THAT list(4.5, etc) to Course_Length list
    parsed_course_length = row[9].split(" ")
    #parsed_course_length = int(parsed_course_length[0])  Can I do this??
    Course_Length.append(parsed_course_length[0])


## Hard code opening CSVs and call functions

## Write first set of data, call fxn again, APPEND second set.
