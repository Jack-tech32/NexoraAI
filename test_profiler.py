import pandas as pd
from src.profiler import profile_dataset


df = pd.DataFrame({
    "Product": ["Laptop", "Mobile", "Tablet"],
    "Sales": [50000, None, None],
    "Quantity": [5, 10, None]
})




profile = profile_dataset(df)

print("Rows:", profile["rows"])
print("Columns:", profile["columns"])
print("Column Names:", profile["column_names"])
print("Data Types:", profile["data_types"])

print("Missing Values:", profile["missing_values"])
print("Missing Percentage:", profile["missing_percentage"])
print("Duplicate Rows:", profile["duplicate_rows"])
print("Numerical Summary:", profile["numerical_summary"])
print("Categorical Summary:", profile["categorical_summary"])
print("Data Quality:", profile["data_quality"])
print("High Missing Columns:", profile["data_quality"]["high_missing_columns"])