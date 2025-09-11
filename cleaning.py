import pandas as pd

# Read the CSV file
df = pd.read_csv('C:/Users/Habbeeba/Projects/Customer-Review-Analysis-for-Business/xr1.csv')

# Remove specific columns by name
#columns_to_remove = ['Author Profile','Author Image','Review URL']
columns_to_remove = ['Photos','Author Profile','Author Image','Review URL']
df = df.drop(columns=columns_to_remove)

# Or remove columns by index (0-based)
# df = df.drop(df.columns[[0, 2, 4]], axis=1)  # removes columns at positions 0, 2, 4

# Save the modified dataframe
df.to_csv('C:/Users/Habbeeba/Projects/Customer-Review-Analysis-for-Business/cleaned_r1.csv', index=False)