# Import libraries
import pandas as pd
from src.preprocessing import DataPreparation
import yaml

def main():

    # Configuration file path
    config_path = "./src/config.yaml"

    with open(config_path, "r") as file:
        config = yaml.safe_load(file)
    
    data_dict = { 'Cust_ID': [1,2,3,4], 
                'Name': ['Amos', 'Shaney', 'Lionel', 'Ameer'],
                'Amount': ['10','15','5', '25'],
                'Item': ['T-shirt', 'Shorts', 'Hat', 'Coat'],
                'Merchant': ['H&M', 'Uniqlo', 'UNiQlO', 'H2M'],
                }
    df = pd.DataFrame(data_dict)

    # Initialize and run data preparation
    data_prep = DataPreparation(config)
    df = data_prep.clean_data(df)

    print(df)
    df.info()

if __name__=="__main__":
    main()
