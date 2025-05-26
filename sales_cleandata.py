import pandas as pd
import numpy as np

# Step 1: Load the dataset
df = pd.read_csv("sales_data_sample.csv", encoding='latin1')
print("Initial dataset shape:", df.shape)

# Step 2: Basic exploration
print("\nDataset Info:")
print(df.info())
print("\nSummary Statistics:")
print(df.describe(include='all'))

# Step 3: Check and handle missing values
missing_values = df.isnull().sum()
print("\nMissing Values:\n", missing_values)

# Drop rows with missing values (if any)
df = df.dropna()
print("\nShape after dropping missing values:", df.shape)

# Step 4: Remove duplicate records
duplicates = df.duplicated().sum()
print("\nNumber of duplicate rows:", duplicates)
df = df.drop_duplicates()
print("Shape after removing duplicates:", df.shape)

# Step 5: Standardize column headers
df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")

# Step 6: Standardize text values (example: 'status' column if available)
if 'status' in df.columns:
    df['status'] = df['status'].str.strip().str.upper()

# Step 7: Convert date columns to datetime format
if 'orderdate' in df.columns:
    df['orderdate'] = pd.to_datetime(df['orderdate'], errors='coerce')
    print("\nConverted 'orderdate' to datetime.")

# Step 8: Fix data types (example)
if 'quantityordered' in df.columns:
    df['quantityordered'] = pd.to_numeric(df['quantityordered'], errors='coerce', downcast='integer')
if 'priceeach' in df.columns:
    df['priceeach'] = pd.to_numeric(df['priceeach'], errors='coerce')

# Step 9: Final cleaning (drop any irrelevant columns if needed)
# Example: drop columns that are mostly empty or irrelevant
# df.drop(columns=['column_name'], inplace=True)

# Step 10: Reset index
df.reset_index(drop=True, inplace=True)

# Step 11: Save cleaned dataset
df.to_csv("cleaned_sales_data.csv", index=False)
print("\nCleaned data saved to 'cleaned_sales_data.csv'.")
