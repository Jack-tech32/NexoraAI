import pandas as pd


def clean_missing_values(df):

    cleaned_df = df.copy()
    cleaning_report = []

    numerical_columns = cleaned_df.select_dtypes(
        include="number"
    ).columns

    categorical_columns = cleaned_df.select_dtypes(
        include=["object", "category"]
    ).columns


    # Numerical columns
    for column in numerical_columns:

        missing_count = cleaned_df[column].isnull().sum()

        if missing_count > 0:

            median_value = cleaned_df[column].median()

            cleaned_df[column] = cleaned_df[column].fillna(
                median_value
            )

            cleaning_report.append({
                "column": column,
                "issue": "Missing Values",
                "action": "Filled with Median",
                "affected_rows": int(missing_count)
            })


    # Categorical columns
    for column in categorical_columns:

        missing_count = cleaned_df[column].isnull().sum()

        if missing_count > 0:

            mode_value = cleaned_df[column].mode()[0]

            cleaned_df[column] = cleaned_df[column].fillna(
                mode_value
            )

            cleaning_report.append({
                "column": column,
                "issue": "Missing Values",
                "action": "Filled with Mode",
                "affected_rows": int(missing_count)
            })


    return cleaned_df, cleaning_report


def remove_duplicates(df):

    cleaned_df = df.copy()

    duplicate_count = cleaned_df.duplicated().sum()

    cleaned_df = cleaned_df.drop_duplicates()

    cleaning_report = []

    if duplicate_count > 0:

        cleaning_report.append({
            "column": "All Columns",
            "issue": "Duplicate Rows",
            "action": "Removed Duplicates",
            "affected_rows": int(duplicate_count)
        })

    return cleaned_df, cleaning_report


def clean_dataset(df):

    cleaned_df = df.copy()

    full_report = []


    # Clean missing values
    cleaned_df, missing_report = clean_missing_values(
        cleaned_df
    )

    full_report.extend(missing_report)


    # Remove duplicate rows
    cleaned_df, duplicate_report = remove_duplicates(
        cleaned_df
    )

    full_report.extend(duplicate_report)


    return cleaned_df, full_report