import pandas as pd
import re
import nltk
from nltk.corpus import stopwords

# Read the CSV file
df = pd.read_csv('C:/Users/Habbeeba/Projects/Customer-Review-Analysis-for-Business/cleaned.csv')

# Remove specific columns by name
#columns_to_remove = ['Author Profile','Author Image','Review URL']
columns_to_remove = ['Photos','Author Profile','Author Image','Review URL','Owner Answer','Owner Answer Date']
df = df.drop(columns=columns_to_remove)

# Remove duplicates based on Review Date, Review Text, and Author
df = df.drop_duplicates(
    subset=['Date', 'Review Text', 'Author'],  # Replace with actual column names
    keep='first'  # Keep the first occurrence of duplicates
)

#remove html tags from review text 
df['Review Text'] = df['Review Text'].str.replace(r'<.*?>', '', regex=True)

#column without stopwords
nltk.download('stopwords')
stop_words = set(stopwords.words('english'))
def remove_stopwords(text):
    if isinstance(text, str):
        words = text.split()
        filtered_words = [word for word in words if word.lower() not in stop_words]
        return ' '.join(filtered_words)
    return text
df['Cleaned Review Text'] = df['Review Text'].apply(remove_stopwords)

# Function to clean text
def clean_text(text):
    if isinstance(text, str):
        # Remove URLs
        text = re.sub(r'http\S+|www\S+|https\S+', '', text, flags=re.MULTILINE)
        # Remove special characters and numbers
        text = re.sub(r'[^A-Za-z\s]', '', text)
        # Convert to lowercase
        text = text.lower()
        # Remove extra whitespace
        text = re.sub(r'\s+', ' ', text).strip()
        return text
    return text
# Apply the cleaning function to the 'Review Text' column
df['Cleaned Review Text'] = df['Cleaned Review Text'].apply(clean_text)

# Save the modified dataframe
df.to_csv('C:/Users/Habbeeba/Projects/Customer-Review-Analysis-for-Business/cleaned2.csv', index=False)
