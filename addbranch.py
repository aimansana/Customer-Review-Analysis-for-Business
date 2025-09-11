import pandas as pd

# Read the CSV file
df = pd.read_csv('C:/Users/Habbeeba/Projects/Customer-Review-Analysis-for-Business/r6.csv')

# Add a new column as the FIRST column with the same value for all entries
df.insert(0, 'Branch', 'Jayanagar')
# Save the modified dataframe
df.to_csv('C:/Users/Habbeeba/Projects/Customer-Review-Analysis-for-Business/r6.csv', index=False)
