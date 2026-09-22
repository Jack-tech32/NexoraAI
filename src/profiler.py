import pandas as pd


def profile_dataset(df):
    missing_count = df.isnull().sum()
    missing_percentage = (missing_count / len(df)) * 100
    duplicate_count = df.duplicated().sum()
    numerical_summary = df.describe().round(2).to_dict()
    categorical_columns = df.select_dtypes(include=["object", "category"]).columns

    categorical_summary = {}

    for column in categorical_columns:
            value_counts = df[column].value_counts(dropna=False)
            percentages = (value_counts / len(df)) * 100

            categorical_summary[column] = {
             "unique_values": int(df[column].nunique(dropna=True)),
             "frequency": value_counts.to_dict(),
             "percentage": percentages.round(2).to_dict()
            }

    data_quality = {
    "missing_value_columns": [],
    "high_missing_columns": [],
    "duplicate_rows": int(duplicate_count)
}

    for column, count in missing_count.items():
        if count > 0:
            percentage = (count / len(df)) * 100

            data_quality["missing_value_columns"].append({
            "column": column,
            "missing_count": int(count),
            "missing_percentage": round(percentage, 2)
             })

            if percentage >= 50:
                 data_quality["high_missing_columns"].append({
                "column": column,
                "missing_percentage": round(percentage, 2)
            })


    profile = {
        "data_quality": data_quality,
        "categorical_summary": categorical_summary,
        "numerical_summary": numerical_summary,
        "duplicate_rows": int(duplicate_count),
        "rows": df.shape[0],
        "columns": df.shape[1],
        "column_names": df.columns.tolist(),
        "data_types": df.dtypes.astype(str).to_dict(),
        "missing_values": missing_count.to_dict(),
        "missing_percentage": missing_percentage.round(2).to_dict()
       
    }

    return profile