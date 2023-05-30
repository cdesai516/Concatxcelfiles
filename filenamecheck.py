import os
import pandas as pd

# Define the directory
directory = 'path_to_your_directory'

# Create an empty DataFrame to append all files into
all_data = pd.DataFrame()

# Loop through the files in the directory
for filename in os.listdir(directory):
    if filename.endswith(".xlsx") or filename.endswith(".xls"):
        # Read the Excel file
        df = pd.read_excel(os.path.join(directory, filename))
        
        # Add the new column based on the file name
        if "Credit" in filename:
            df['New_Column'] = "Credit"
        elif "Equities" in filename:
            df['New_Column'] = "Equity"
        
        # Append the data to the master DataFrame
        all_data = all_data.append(df, ignore_index=True)
