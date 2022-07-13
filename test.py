import pandas as pd
import csv
from csv import writer
from csv import reader
import numpy as np
import uuid

keywords = "001|Pimville"

unique_filename = str(uuid.uuid4())

df = pd.read_csv('Python CSV.csv')

#print(df.loc[df['Reference'].str.contains(keywords)])

def add_column_in_csv(input_file, output_file, transform_row):
    """ Append a column in existing csv using csv.reader / csv.writer classes"""
    # Open the input_file in read mode and output_file in write mode
    with open(input_file, 'r') as read_obj, \
            open(output_file, 'w', newline='') as write_obj:
        # Create a csv.reader object from the input file object
        csv_reader = reader(read_obj)
        # Create a csv.writer object from the output file object
        csv_writer = writer(write_obj)
        # Read each row of the input csv file as list
        for row in csv_reader:
            # Pass the list / row in the transform function to add column text for this row
            transform_row(row, csv_reader.line_num)
            # Write the updated row / list to the output file
            csv_writer.writerow(row)

default_text = "Pimville"

reference_column = df.loc[df['Reference'].str.contains(keywords)]

number = 1
increment = number+1

file_name = "output_${increment}"


#writes output of csv only containing keywords 
with open('output.txt', 'a') as f:
    print(reference_column, file=f)

#ensure that there are no exsting csv files with the same name

read_file = pd.read_csv (r'output.txt')
read_file.to_csv (r'pimville.csv', index=None)

for df.loc[df['Reference'].str.contains(keywords)] in df: 
    add_column_in_csv('pimville.csv', unique_filename.csv', lambda row, line_num: row.append(default_text))


# output = pd.read_csv('output_3.csv')
# print(output)

#print(df.loc[df['Reference'].str.contains(keyword)])