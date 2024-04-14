import pandas as pd

def get_dupes_df(dataframe):
    df = dataframe
    duplicates_df = df[df.duplicated()]

    duplicates_df.to_csv('dupes.csv')