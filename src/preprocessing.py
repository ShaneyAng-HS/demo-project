# Import libraries
import pandas as pd

# Write helper functions

def clean_data(df):
    
    df['Amount'] = df['Amount'].astype(int)

    return df


