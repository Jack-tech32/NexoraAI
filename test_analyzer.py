import pandas as pd

from src.analyzer import (
    analyze_average,
    analyze_count,
    analyze_unique,
    analyze_value_counts,
    analyze_grouped_average
)


df = pd.DataFrame({
    "Age": [25, 30, 35, 40, 28],
    "Income": [50000, 60000, 70000, 80000, 55000],
    "City": [
        "Pune",
        "Mumbai",
        "Pune",
        "Mumbai",
        "Pune"
    ]
})


print("\nAverage Age:")
print(analyze_average(df, "Age"))


print("\nIncome Count:")
print(analyze_count(df, "Income"))


print("\nUnique Cities:")
print(analyze_unique(df, "City"))


print("\nCity Counts:")
print(analyze_value_counts(df, "City"))


print("\nAverage Income by City:")
print(
    analyze_grouped_average(
        df,
        "City",
        "Income"
    )
)