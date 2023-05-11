import os
import pandas as pd

# Get the current working directory
cwd = os.getcwd()

# List all the folders in the current working directory
folders = [f for f in os.listdir(cwd) if os.path.isdir(os.path.join(cwd, f))]

# Loop over all the folders in the current working directory
for folder in folders:
    # Get the path to the current folder
    folder_path = os.path.join(cwd, folder)
    
    # List all the Excel files in the current folder
    excel_files = [f for f in os.listdir(folder_path) if f.endswith('.xlsx') or f.endswith('.xls') or f.endswith('.XLSX') or f.endswith('.XLS')]
    
    # Loop over all the Excel files in the current folder
    for excel_file in excel_files:
        # Get the path to the current Excel file
        excel_file_path = os.path.join(folder_path, excel_file)
        
        # Create an ExcelFile object
        excel = pd.ExcelFile(excel_file_path)
        
        # List all the sheet names in the current Excel file
        sheet_names = excel.sheet_names
        
        # Print the sheet names
        print("Excel file '{}': Sheet names = {}".format(excel_file, sheet_names))
