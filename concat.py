import pandas as pd
import os

# Set the directory path where the Excel files are stored
directory_path = '/path/to/directory'

# Initialize an empty list to store the dataframes
dfs = []

# Loop through each file in the directory
for file in os.listdir(directory_path):
    if file.endswith('.xlsx'):
        # Load the Excel file into a dataframe
        df = pd.read_excel(os.path.join(directory_path, file))
        # Append the dataframe to the list
        dfs.append(df)

# Concatenate the dataframes into a single dataframe
result = pd.concat(dfs)

# Write the concatenated dataframe to a new Excel file
result.to_excel('/path/to/output/file.xlsx', index=False)
