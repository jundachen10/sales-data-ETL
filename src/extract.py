import pandas as pd
import os

def extract_data_from_csv(file_path):
    """
    Reads a CSV file into a pandas DataFrame.
    
    Parameters:
    - file_path (str): The full path to the CSV file.
    
    Returns:
    - pandas.DataFrame: The data from the CSV file, or None if an error occurs.
    """
    try:
        # Load the CSV data into a DataFrame
        data = pd.read_csv(file_path)
        return data
    
    except Exception as e:
        print(f"An error occurred while reading the CSV file: {e}")
        return None