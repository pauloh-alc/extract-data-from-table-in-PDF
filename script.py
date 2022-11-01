#!/usr/bin/env python

import tabula as tb
import zipfile as zf
import csv

# Used libs:
"""
    *tabula : tabula-py enables you to extract tables from a PDF into a DataFrame, or a JSON.
    *csv    : the csv library provides functionality to both read from and write to CSV files.
    *zipfile: the ZIP file format is a common archive and compression standar.
"""

# csv file name
FILE_NAME_CSV = 'file'
# pdf file name
FILE_NAME_PDF = 'anexo1'

# First page of the pdf and last page of the pdf that contains tables.
FIRST_PAGE = 3
LAST_PAGE = 180

# number of tables in pdf
QTD_TABLES = LAST_PAGE - FIRST_PAGE + 1

# Read PDF into list of DataFrames
list_dfs = tb.read_pdf(FILE_NAME_PDF+'.pdf', pages=str(FIRST_PAGE) + '-' + str(LAST_PAGE), lattice=True)

# dictionary to handle subtitles
dic = {'OD': 'Seg. Odontológica', 'AMB': 'Seg. Ambulatorial'}

# function: Replaces the short data in the OD and AMB columns with their descriptions
def replace_column_data(row, i, j):
    for key in dic.keys():
        if key in list_dfs[i].iloc[j]:
            try:
                idx = list(list_dfs[i].iloc[j]).index(key)
            except ValueError:
                idx = -1;

            if idx != -1:
                row[idx] = dic[key]

# function: turn to zip
def to_zip_file():
    z = zf.ZipFile('Teste_'+FILE_NAME_CSV+'_.zip', 'w', zf.ZIP_DEFLATED)
    z.write(FILE_NAME_CSV+'.csv')
    z.close()


# Manipulating the .csv file
def write_to_csv_file():
    with open('./'+FILE_NAME_CSV+'.csv', 'w') as csvfile:
        # Write the columns name
        csv.writer(csvfile, delimiter=',').writerow(list(list_dfs[0].columns))
        # Stores each table row in a list
        row = []

        # Scroll through pdf tables
        for i in range(0,QTD_TABLES):
            qtd_rows = len(list_dfs[i].index)
            
            # Traverse the table rows
            for j in range(0,qtd_rows):
                list_dfs[i].fillna(value='', inplace = True)        # replace nan values with blank values.
                row = list(list_dfs[i].iloc[j])                     # selecting line from DataFrame.
                replace_column_data(row, i, j)                      # replaces the short data in the OD and AMB columns with their descriptions.
                csv.writer(csvfile, delimiter=',').writerow(row)    # write to csv file
