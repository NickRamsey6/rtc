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

# Create new sheet
wb.create_sheet('New_Sheet')
wb.save(path)

# Create new workbook
wb = Workbook()
ws = wb.active
ws.title = 'Data'
ws.append(['Col1', 'Col2', 'Col3'])
wb.save(path)

# Create new csv with only the duplicated rows
def get_dupes_df(dataframe):
    df = dataframe
    duplicates_df = df[df.duplicated()]

    # Can also pass in specific cols to check for dupes
    # duplicates_df = df[df/duplicated(cols)]

    duplicates_df.to_csv('dupes.csv')