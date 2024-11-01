import os, faker
from faker.providers import BaseProvider
import re
import pandas as pd
from streamlit import selectbox, text_input, button, write
from utils import *

# **Faker Instance**
fake = faker.Faker()

# **Function to Generate Synthetic Data**
def generate_synthetic_data(selected_columns, num_records):
    data = {column: [schema[column]["generator"]() for _ in range(num_records)] for column in selected_columns}
    df = pd.DataFrame(data)
    # Basic Validation Check (More thorough checks might be needed based on specific requirements)
    for column, values in df.items():
        for value in values:
            if not re.match(schema[column]["regex"], str(value)):
                print(f"Validation Error: {column} - {value}")
    return df

# **Streamlit App**
if __name__ == "__main__":
    import streamlit as st
    
    st.title("Synthetic Medical Data Generator")
    
    # **Column Selection**
    selected_columns = st.multiselect("Select Columns to Generate", list(schema.keys()), default=list(schema.keys()))
    
    # **Number of Records Input**
    num_records = st.number_input("Enter Number of Records", min_value=1, value=10)
    
    # **Generate Button**
    if st.button("Generate Data"):
        df = generate_synthetic_data(selected_columns, num_records)
        st.write(df)
        @st.cache
        def convert_df(df):
            return df.to_csv(index=False).encode('utf-8')
        csv = convert_df(df)
        st.download_button("Download as CSV", csv, file_name="synthetic_medical_data.csv", mime='text/csv')
