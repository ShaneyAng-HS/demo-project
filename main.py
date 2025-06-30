# Import libraries
import pandas as pd
from src.preprocessing import clean_data

def main():
    
    data_dict = { 'Cust_ID': [1,2,3], 
                'Name': ['Amos', 'Shaney', 'Lionel'],
                'Amount': ['10','15','5'],
                'Item': ['T-shirt', 'Shorts', 'Hat'],
                }
    df = pd.DataFrame(data_dict)
    df = clean_data(df)
    print(df)
    df.info()

if __name__=="__main__":
    main()
