import pandas as pd

# Read the CSV file
df = pd.read_csv('C:/Users/Habbeeba/Projects/Customer-Review-Analysis-for-Business/merged_reviews.csv')

# Remove specific columns by name
#columns_to_remove = ['Author Profile','Author Image','Review URL']
columns_to_remove = ['Photos','Author Profile','Author Image','Review URL','Owner Answer','Owner Answer Date']
df = df.drop(columns=columns_to_remove)

# Remove duplicates based on Review Date, Review Text, and Author
df = df.drop_duplicates(
    subset=['Date', 'Review Text', 'Author'],  # Replace with actual column names
    keep='first'  # Keep the first occurrence of duplicates
)

# Save the modified dataframe
df.to_csv('C:/Users/Habbeeba/Projects/Customer-Review-Analysis-for-Business/cleaned_2.csv', index=False)
