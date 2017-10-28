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

#Import dependencies

import os
import csv
import datetime

# Display initial instructions and collect .csv files from user

print("------------------------------------------------------------------")
print("Please enter two CSV files for revenue data analysis.")
budget1_csv = input("First CSV file: ")
budget2_csv = input("Second CSV file: ")

# 

csv_path1 = 
csv_path2 = 