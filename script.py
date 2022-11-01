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
