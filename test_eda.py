import pandas as pd

from src.eda import run_eda


df = pd.DataFrame({
    "Date": [
        "2026-01-01",
        "2026-01-02",
        "2026-01-03",
        "2026-01-04",
        "2026-01-05"
    ],
    "Product": [
        "Laptop",
        "Mobile",
        "Tablet",
        "Monitor",
        "Keyboard"
    ],
    "Sales": [50000, 30000, 20000, 25000, 200000],
    "Quantity": [5, 10, 8, 7, 50]
})


# Run complete EDA pipeline
eda_result = run_eda(df)


print("EDA Result:")
print(eda_result)


print("\nEDA Sections:")
print(eda_result.keys())