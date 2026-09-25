import streamlit as st
import pandas as pd
from src.profiler import profile_dataset
from src.cleaning import clean_dataset


st.set_page_config(
    page_title="NexoraAI",
    page_icon="assets/NexoraAI.png",
    layout="wide"
)


# --------------------------------------------------
# HEADER
# --------------------------------------------------

st.image(
    "assets/NexoraAI.png",
    width=180
)

st.subheader("AI-Powered Data Analysis")

st.write(
    "Upload your dataset and analyze it using "
    "Python, Pandas and AI."
)


# --------------------------------------------------
# UPLOAD DATASET
# --------------------------------------------------

st.header("Upload Dataset")

uploaded_file = st.file_uploader(
    "Upload a CSV file",
    type=["csv"]
)


if uploaded_file is not None:

    # --------------------------------------------------
    # READ DATASET
    # --------------------------------------------------

    try:

        df = pd.read_csv(uploaded_file)

    except pd.errors.EmptyDataError:

        st.error(
            "The uploaded CSV file is empty. "
            "Please upload a valid CSV file."
        )

        st.stop()

    except pd.errors.ParserError:

        st.error(
            "Unable to read this CSV file. "
            "Please check the CSV format."
        )

        st.stop()


    if df.empty or len(df.columns) == 0:

        st.error(
            "The uploaded CSV does not contain any data."
        )

        st.stop()


    st.success("Dataset uploaded successfully!")


    # --------------------------------------------------
    # DATASET PREVIEW
    # --------------------------------------------------

    st.subheader("Dataset Preview")

    st.dataframe(
        df.head(10),
        use_container_width=True
    )


    # --------------------------------------------------
    # DATA PROFILING
    # --------------------------------------------------

    st.subheader("Data Profiling")

    profile = profile_dataset(df)


    col1, col2, col3, col4 = st.columns(4)

    col1.metric(
        "Rows",
        profile["rows"]
    )

    col2.metric(
        "Columns",
        profile["columns"]
    )

    col3.metric(
        "Duplicate Rows",
        profile["duplicate_rows"]
    )

    col4.metric(
        "Missing Values",
        sum(profile["missing_values"].values())
    )


    # --------------------------------------------------
    # COLUMN INFORMATION
    # --------------------------------------------------

    st.write("Column Information")

    column_data = pd.DataFrame({
        "Column": profile["column_names"],
        "Data Type": [
            profile["data_types"][column]
            for column in profile["column_names"]
        ]
    })

    st.dataframe(
        column_data,
        use_container_width=True,
        hide_index=True
    )


    # --------------------------------------------------
    # MISSING VALUES
    # --------------------------------------------------

    st.subheader("Missing Values")

    missing_data = pd.DataFrame({
        "Column": profile["column_names"],
        "Missing Count": [
            profile["missing_values"][column]
            for column in profile["column_names"]
        ],
        "Missing Percentage": [
            profile["missing_percentage"][column]
            for column in profile["column_names"]
        ]
    })

    st.dataframe(
        missing_data,
        use_container_width=True,
        hide_index=True
    )


    # --------------------------------------------------
    # DATA QUALITY
    # --------------------------------------------------

    st.subheader("Data Quality")

    quality = profile["data_quality"]


    # Missing Values
    if quality["missing_value_columns"]:

        st.write("Columns with Missing Values")

        missing_quality_data = pd.DataFrame(
            quality["missing_value_columns"]
        )

        st.dataframe(
            missing_quality_data,
            use_container_width=True,
            hide_index=True
        )

    else:

        st.success(
            "No missing values found in the dataset."
        )


    # High Missing Values
    if quality["high_missing_columns"]:

        st.warning(
            "Columns with High Missing Values"
        )

        high_missing_data = pd.DataFrame(
            quality["high_missing_columns"]
        )

        st.dataframe(
            high_missing_data,
            use_container_width=True,
            hide_index=True
        )

    else:

        st.success(
            "No columns have 50% or more missing values."
        )


    # Duplicate Rows
    if quality["duplicate_rows"] > 0:

        st.warning(
            f"{quality['duplicate_rows']} "
            "duplicate rows detected."
        )

    else:

        st.success(
            "No duplicate rows found."
        )


    # --------------------------------------------------
    # NUMERICAL SUMMARY
    # --------------------------------------------------

    st.subheader("Numerical Summary")

    st.dataframe(
        pd.DataFrame(
            profile["numerical_summary"]
        ).T,
        use_container_width=True
    )


    # --------------------------------------------------
    # CATEGORICAL SUMMARY
    # --------------------------------------------------

    st.subheader("Categorical Summary")

    for column, summary in profile[
        "categorical_summary"
    ].items():

        st.markdown(f"### {column}")

        category_data = pd.DataFrame({
            "Category": list(
                summary["frequency"].keys()
            ),
            "Count": list(
                summary["frequency"].values()
            ),
            "Percentage": list(
                summary["percentage"].values()
            )
        })

        st.dataframe(
            category_data,
            use_container_width=True,
            hide_index=True
        )


    # --------------------------------------------------
    # AUTOMATIC DATA CLEANING
    # --------------------------------------------------

    st.subheader("Automatic Data Cleaning")

    st.write(
        "NexoraAI automatically detects and cleans "
        "missing values and duplicate rows."
    )


    if st.button("Clean Dataset"):

        # Run cleaning engine
        cleaned_df, cleaning_report = clean_dataset(df)

        st.success(
            "Dataset cleaned successfully!"
        )


        # --------------------------------------------------
        # CLEANING RESULTS
        # --------------------------------------------------

        st.subheader("Cleaning Results")

        before_rows = len(df)
        after_rows = len(cleaned_df)

        before_missing = int(
            df.isnull().sum().sum()
        )

        after_missing = int(
            cleaned_df.isnull().sum().sum()
        )

        before_duplicates = int(
            df.duplicated().sum()
        )

        after_duplicates = int(
            cleaned_df.duplicated().sum()
        )


        col1, col2, col3 = st.columns(3)


        col1.metric(
            "Rows",
            after_rows,
            delta=after_rows - before_rows
        )


        col2.metric(
            "Missing Values",
            after_missing,
            delta=after_missing - before_missing
        )


        col3.metric(
            "Duplicate Rows",
            after_duplicates,
            delta=after_duplicates - before_duplicates
        )


        # --------------------------------------------------
        # CLEANING REPORT
        # --------------------------------------------------

        st.subheader("Cleaning Report")


        if cleaning_report:

            report_df = pd.DataFrame(
                cleaning_report
            )

            st.dataframe(
                report_df,
                use_container_width=True,
                hide_index=True
            )

        else:

            st.success(
                "No cleaning was required. "
                "The dataset is already clean."
            )


        # --------------------------------------------------
        # CLEANED DATASET
        # --------------------------------------------------

        st.subheader(
            "Cleaned Dataset Preview"
        )

        st.dataframe(
            cleaned_df.head(10),
            use_container_width=True
        )


        # --------------------------------------------------
        # DOWNLOAD CLEANED DATASET
        # --------------------------------------------------

        st.subheader(
            "Download Cleaned Dataset"
        )

        cleaned_csv = cleaned_df.to_csv(
            index=False
        ).encode("utf-8")


        st.download_button(
            label="Download Cleaned CSV",
            data=cleaned_csv,
            file_name="nexoraai_cleaned_dataset.csv",
            mime="text/csv"
        )