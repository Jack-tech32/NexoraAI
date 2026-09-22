import pandas as pd


def numerical_analysis(df):
    numerical_columns = df.select_dtypes(include="number").columns

    analysis = {}

    for column in numerical_columns:
        analysis[column] = {
            "mean": float(round(df[column].mean(), 2)),
            "median": float(round(df[column].median(), 2)),
            "min": float(round(df[column].min(), 2)),
            "max": float(round(df[column].max(), 2)),
            "std": float(round(df[column].std(), 2)),
            "25%": float(round(df[column].quantile(0.25), 2)),
            "50%": float(round(df[column].quantile(0.50), 2)),
            "75%": float(round(df[column].quantile(0.75), 2))
        }

    return analysis

def categorical_analysis(df):
    categorical_columns = df.select_dtypes(
        include=["object", "category"]
    ).columns

    analysis = {}

    for column in categorical_columns:
        value_counts = df[column].value_counts(dropna=False)
        percentages = (value_counts / len(df)) * 100

        analysis[column] = {
            "unique_values": int(df[column].nunique(dropna=True)),
            "frequency": value_counts.to_dict(),
            "percentage": percentages.round(2).to_dict()
        }

    return analysis

def correlation_analysis(df):
    numerical_columns = df.select_dtypes(include="number").columns

    if len(numerical_columns) < 2:
        return {}

    correlation_matrix = df[numerical_columns].corr()

    return correlation_matrix.round(2).to_dict()

def outlier_analysis(df):
    numerical_columns = df.select_dtypes(include="number").columns

    analysis = {}

    for column in numerical_columns:
        q1 = df[column].quantile(0.25)
        q3 = df[column].quantile(0.75)

        iqr = q3 - q1

        lower_bound = q1 - (1.5 * iqr)
        upper_bound = q3 + (1.5 * iqr)

        outliers = df[
            (df[column] < lower_bound) |
            (df[column] > upper_bound)
        ][column]

        analysis[column] = {
            "q1": float(round(q1, 2)),
            "q3": float(round(q3, 2)),
            "iqr": float(round(iqr, 2)),
            "lower_bound": float(round(lower_bound, 2)),
            "upper_bound": float(round(upper_bound, 2)),
            "outlier_count": int(len(outliers)),
            "outlier_values": outliers.tolist()
        }

    return analysis

def date_analysis(df):
    analysis = {}

    for column in df.columns:

        # Skip numerical columns
        if pd.api.types.is_numeric_dtype(df[column]):
            continue

        converted_dates = pd.to_datetime(
            df[column],
            errors="coerce",
            format="mixed"
        )

        valid_dates = converted_dates.dropna()

        if len(valid_dates) == 0:
            continue

        conversion_percentage = len(valid_dates) / len(df)

        if conversion_percentage < 0.8:
            continue

        analysis[column] = {
            "min_date": valid_dates.min().strftime("%Y-%m-%d"),
            "max_date": valid_dates.max().strftime("%Y-%m-%d"),
            "unique_dates": int(valid_dates.nunique()),
            "date_range_days": int(
                (valid_dates.max() - valid_dates.min()).days
            )
        }

    return analysis

def trend_analysis(df):
    analysis = {}

    date_columns = []

    for column in df.columns:
        if pd.api.types.is_numeric_dtype(df[column]):
            continue

        converted_dates = pd.to_datetime(
            df[column],
            errors="coerce",
            format="mixed"
        )

        valid_dates = converted_dates.dropna()

        if len(valid_dates) == 0:
            continue

        conversion_percentage = len(valid_dates) / len(df)

        if conversion_percentage >= 0.8:
            date_columns.append(column)

    if not date_columns:
        return {}

    date_column = date_columns[0]

    numerical_columns = df.select_dtypes(
        include="number"
    ).columns

    for column in numerical_columns:
        trend_data = pd.DataFrame({
            "date": pd.to_datetime(
                df[date_column],
                errors="coerce",
                format="mixed"
            ),
            "value": df[column]
        }).dropna()

        trend_data = trend_data.sort_values("date")

        analysis[column] = {
            "date_column": date_column,
            "data": [
                {
                    "date": row["date"].strftime("%Y-%m-%d"),
                    "value": float(row["value"])
                }
                for _, row in trend_data.iterrows()
            ]
        }

    return analysis

def run_eda(df):
    return {
        "numerical_analysis": numerical_analysis(df),
        "categorical_analysis": categorical_analysis(df),
        "correlation_analysis": correlation_analysis(df),
        "outlier_analysis": outlier_analysis(df),
        "date_analysis": date_analysis(df),
        "trend_analysis": trend_analysis(df)
    }