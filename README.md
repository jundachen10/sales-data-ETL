# POS Sales data 

## Project Overview
This project is designed to build an ETL (Extract, Transform, Load) pipeline for a point of sale (POS) system. Initially, the focus is on extracting data from CSV files, which contain daily sales and operational details. The goal is to streamline data handling, prepare for advanced analytics and generate actionable insights to improve business operations.

## Features
- **Data Extraction**: Implement a Python script to read and validate data from CSV files.

### Prerequisites
- Python 3.12 or higher
- pip (Python package installer)

### Setup Environment
1. Clone the repository:
git clone https://github.com/jundachen10/sales-data-ETL.git
2. Create a virtual environment
python3 -m venv {name of env}
3. Activiate the virtual environment
source {name of env}/bin/activate

### Loading data csv
1. CSV file should be placed into the /data/raw folder
2. In main.py enter your CSV filename 
    file_path = os.path.join(project_root, "data", "raw", "Cleaned Order Details for the year.csv")
### Running program
1. python3 main.py