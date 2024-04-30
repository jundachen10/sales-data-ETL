import os
from extract import extract_data_from_csv

def main():
    
    current_dir = os.path.dirname(__file__)
    project_root = os.path.dirname(current_dir)
    file_path = os.path.join(project_root, 'data', 'test_data.csv')
    
    data = extract_data_from_csv(file_path)
    
    if data is not None:
        print(data.head())
    else:
        print("error")
        
if __name__ == "__main__":
    main()