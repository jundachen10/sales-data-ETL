import os
from extract import extract_data_from_csv
from transform import filter_and_find_popular_item

def main():
    """
    Main execution function of the application.
    
    This function constructs the file path for the CSV data, calls the data extraction function,
    and prints the first few rows of the extracted data if successful.
    """
    
    file_path = get_data_file_path()
    data = extract_data_from_csv(file_path)
    popular_item = filter_and_find_popular_item(data)
    print(f"Most popular Dine In item is: {popular_item}")
    
    if data is not None:
        print(data.head(10))
    else:
        print("error")
        
def get_data_file_path():
    """
    Constructs and returns the absolute file path to the data CSV file.
    
    Returns:
        str: The absolute path to the test data CSV file.
    """
    current_dir = os.path.dirname(__file__)
    project_root = os.path.dirname(current_dir)
    file_path = os.path.join(project_root, 'data', 'raw', 'order detail for year.csv')
    return file_path
   
if __name__ == "__main__":
    main()