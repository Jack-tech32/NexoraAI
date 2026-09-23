import streamlit as st
import pandas as pd
from src.profiler import profile_dataset


st.set_page_config(
    page_title="NexoraAI",
    page_icon="assets/NexoraAI.png",
    layout="wide"
)


# Logo
st.image(
    "assets/NexoraAI.png",
    width=180
)


st.subheader("AI-Powered Data Analysis")

st.write(
    "Upload your dataset and analyze it using "
    "Python, Pandas and AI."
)


# Upload Dataset
st.header("Upload Dataset")

uploaded_file = st.file_uploader(
    "Upload a CSV file",
    type=["csv"]
)


# Read Dataset
if uploaded_file is not None:

    st.success("Dataset uploaded successfully!")

    df = pd.read_csv(uploaded_file)

    st.subheader("Dataset Preview")

    st.dataframe(df.head())
    st.subheader("Data Profiling")

    profile = profile_dataset(df)
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Rows", profile["rows"])
    col2.metric("Columns", profile["columns"])
    col3.metric("Duplicate Rows", profile["duplicate_rows"])
    col4.metric( "Missing Values",sum(profile["missing_values"].values()))
                
  
    st.write("Column Names:", profile["column_names"])
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
    
    st.subheader("Data Quality")
    quality = profile["data_quality"]

# Missing Values
    if quality["missing_value_columns"]:

        st.write("Columns with Missing Values")

        missing_data = pd.DataFrame(
        quality["missing_value_columns"]
        )

        st.dataframe(
        missing_data,
        use_container_width=True,
        hide_index=True
        )

    else:
        st.success("No missing values found in the dataset.")


# High Missing Values
    if quality["high_missing_columns"]:

        st.warning("Columns with High Missing Values")

        high_missing_data = pd.DataFrame(
        quality["high_missing_columns"]
        )

        st.dataframe(
        high_missing_data,
        use_container_width=True,
        hide_index=True
        )

    else:
        st.success("No columns have 50% or more missing values.")


# Duplicate Rows
    if quality["duplicate_rows"] > 0:
        st.warning(
            f"{quality['duplicate_rows']} duplicate rows detected."
        )
    else:
        st.success("No duplicate rows found.")







    st.subheader("Numerical Summary")
    st.dataframe(
    pd.DataFrame(profile["numerical_summary"]).T
    )





    st.subheader("Categorical Summary")

    for column, summary in profile["categorical_summary"].items():

        st.markdown(f"### {column}")

        category_data = pd.DataFrame({
        "Category": list(summary["frequency"].keys()),
        "Count": list(summary["frequency"].values()),
        "Percentage": list(summary["percentage"].values())
        })

        st.dataframe(
        category_data,
        use_container_width=True,
        hide_index=True
        )