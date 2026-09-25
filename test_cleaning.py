import pandas as pd

from src.cleaning import clean_dataset


df = pd.DataFrame({
    "Age": [25, 30, None, 40, 25],
    "Income": [50000, None, 70000, 60000, 50000],
    "City": ["Pune", "Mumbai", None, "Pune", "Pune"],
    "Gender": ["Male", "Female", "Male", None, "Male"]
})


print("Original Rows:")
print(len(df))


print("\nOriginal Missing Values:")
print(df.isnull().sum())


print("\nOriginal Duplicate Rows:")
print(df.duplicated().sum())


# Automatic Cleaning
cleaned_df, cleaning_report = clean_dataset(df)


print("\nCleaned Rows:")
print(len(cleaned_df))


print("\nCleaned Data:")
print(cleaned_df)


print("\nMissing Values After Cleaning:")
print(cleaned_df.isnull().sum())


print("\nDuplicate Rows After Cleaning:")
print(cleaned_df.duplicated().sum())


print("\nCleaning Report:")
print(cleaning_report)