import pandas as pd

# Create new csv with only the duplicated rows
def get_dupes_df(dataframe):
    df = dataframe
    duplicates_df = df[df.duplicated()]

    # Can also pass in specific cols to check for dupes
    # duplicates_df = df[df/duplicated(cols)]

    duplicates_df.to_csv('dupes.csv')