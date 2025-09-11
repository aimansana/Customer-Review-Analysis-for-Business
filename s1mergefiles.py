import pandas as pd
import os

# List of raw data files from different branches
raw_files = [
    'C:/Users/Habbeeba/Projects/Customer-Review-Analysis-for-Business/r1.csv',
    'C:/Users/Habbeeba/Projects/Customer-Review-Analysis-for-Business/r2.csv',
    'C:/Users/Habbeeba/Projects/Customer-Review-Analysis-for-Business/r3.csv',
    'C:/Users/Habbeeba/Projects/Customer-Review-Analysis-for-Business/r4.csv',
    'C:/Users/Habbeeba/Projects/Customer-Review-Analysis-for-Business/r5.csv',
    'C:/Users/Habbeeba/Projects/Customer-Review-Analysis-for-Business/r6.csv'

]

# Output file path
output_file = 'C:/Users/Habbeeba/Projects/Customer-Review-Analysis-for-Business/merged_reviews.csv'

# Read and merge files
try:
    # Read all CSV files into a list of DataFrames
    dfs = [pd.read_csv(f) for f in raw_files]
    
    # Concatenate all DataFrames
    merged_df = pd.concat(dfs, ignore_index=True)
    
    # Save the merged DataFrame to CSV
    merged_df.to_csv(output_file, index=False)
    
    print(f"Successfully merged {len(raw_files)} files!")
    print(f"Total records: {len(merged_df)}")
    print(f"Merged file saved as: {output_file}")
    
except FileNotFoundError as e:
    print(f"Error: File not found - {e}")
except Exception as e:
    print(f"An error occurred: {e}")