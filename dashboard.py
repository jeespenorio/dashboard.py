import streamlit as st
import pandas as pd

st.title("CSV Data Viewer")

uploaded_file = st.sidebar.file_uploader("Upload a CSV file", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file, low_memory=False)
    column_names = df.columns.tolist()

    # Create checkboxes to select columns
    selected_columns = st.sidebar.multiselect("Select Columns", column_names)

    # Create an empty dataframe to merge selected tables
    merged_df = pd.DataFrame()

    # Display tables for selected columns and merge them
    for column_name in selected_columns:
        st.sidebar.subheader(f"Table for {column_name}")
        table = df[[column_name]]
      #  st.sidebar.write(table)
        merged_df = pd.concat([merged_df, table], axis=1)

    # Display the merged table in the main body
    st.subheader("Merged Table")
    st.write(merged_df)
