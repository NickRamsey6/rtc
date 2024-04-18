import pandas as pd
from openpyxl import Workbook, load_workbook

# Load workbook
wb = load_workbook('path')
ws = wb.active

# Access specific cells
print(ws['A1'].value)

# Modify specific cells
ws['A1'] = 'Test'
wb.save(path)

# Access specific sheets
print(wb.sheetnames)
print(wb['Sheet1'])
ws = wb['Sheet1']

# Create new csv with only the duplicated rows
def get_dupes_df(dataframe):
    df = dataframe
    duplicates_df = df[df.duplicated()]

    # Can also pass in specific cols to check for dupes
    # duplicates_df = df[df/duplicated(cols)]

    duplicates_df.to_csv('dupes.csv')