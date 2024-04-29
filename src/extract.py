import pandas as pd
import os

def extract_data_from_csv(file_path):
    try:
        # Load the CSV data into a DataFrame
        data = pd.read_csv(file_path)

        # Display the first few rows of the DataFrame
        print("First few rows of the CSV file:")
        print(data.head())

        # Optional: Perform additional processing here
        return data
    except Exception as e:
        print(f"An error occurred while reading the CSV file: {e}")
        return None

if __name__ == "__main__":
    # Construct the file path relative to the script location
    current_dir = os.path.dirname(__file__)  # Gets the directory where the script is located
    project_root = os.path.dirname(current_dir)  # Moves up to the project root directory
    file_path = os.path.join(project_root, 'data', 'test_data.csv')  # Constructs the path to the CSV
    
    # Call the function to extract data
    data = extract_data_from_csv(file_path)