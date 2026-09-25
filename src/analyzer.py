import pandas as pd


def analyze_average(df, column):
    """
    Calculate the average of a numerical column.
    """

    if column not in df.columns:
        raise ValueError(
            f"Column '{column}' does not exist in the dataset."
        )

    if not pd.api.types.is_numeric_dtype(df[column]):
        raise ValueError(
            f"Column '{column}' is not numerical."
        )

    return df[column].mean()


def analyze_count(df, column):
    """
    Count non-null values in a column.
    """

    if column not in df.columns:
        raise ValueError(
            f"Column '{column}' does not exist in the dataset."
        )

    return int(df[column].count())


def analyze_unique(df, column):
    """
    Count unique values in a column.
    """

    if column not in df.columns:
        raise ValueError(
            f"Column '{column}' does not exist in the dataset."
        )

    return int(df[column].nunique())


def analyze_value_counts(df, column):
    """
    Count occurrences of each category/value.
    """

    if column not in df.columns:
        raise ValueError(
            f"Column '{column}' does not exist in the dataset."
        )

    return df[column].value_counts()


def analyze_grouped_average(df, group_column, value_column):
    """
    Calculate the average of a numerical column
    grouped by another column.
    """

    if group_column not in df.columns:
        raise ValueError(
            f"Column '{group_column}' does not exist."
        )

    if value_column not in df.columns:
        raise ValueError(
            f"Column '{value_column}' does not exist."
        )

    if not pd.api.types.is_numeric_dtype(df[value_column]):
        raise ValueError(
            f"Column '{value_column}' must be numerical."
        )

    return (
        df.groupby(group_column)[value_column]
        .mean()
        .sort_values(ascending=False)
        .round(2)
)