# Import libraries
import pandas as pd
from typing import Any, Dict

# Write helper functions

# def clean_data(df):

#     df['Amount'] = df['Amount'].astype(int)

#     return df

class DataPreparation:

    def __init__(self, config: Dict[str, Any]):

        self.config = config

    @staticmethod
    def _clean_merchant_name(name: str) -> str:

        name = name.capitalize()
        name = name.replace('2','&')
        
        return name

    def clean_data(self, df):

        df['Amount'] = df['Amount'].astype(int)
        df['Merchant'] = df['Merchant'].apply(self._clean_merchant_name)

        return df
