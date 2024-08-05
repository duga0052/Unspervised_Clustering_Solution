# data_loader.py
import pandas as pd

def load_data(file_path):
    df = pd.read_csv(file_path)
    
    # Display the first few rows of the dataframe
    print("First few rows of the dataframe:")
    print(df.head())

    print("\nDataframe information:")
    # Display information about the dataframe
    df.info()
    return df