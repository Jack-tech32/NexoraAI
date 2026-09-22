import pandas as pd
from src.profiler import profile_dataset


df = pd.DataFrame({
    "Product": ["Laptop", "Mobile", "Tablet"],
    "Sales": [50000, 30000, 20000],
    "Quantity": [5, 10, 7]
})

profile = profile_dataset(df)

print("Rows:", profile["rows"])
print("Columns:", profile["columns"])
print("Column Names:", profile["column_names"])
print("Data Types:", profile["data_types"])

print("Missing Values:", profile["missing_values"])