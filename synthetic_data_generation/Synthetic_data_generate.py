import faker
from faker.providers import BaseProvider
import re
import pandas as pd
from streamlit import selectbox, text_input, button, write

# **Schema Dictionary with Regex Patterns**
schema = {
    "first_name": {"faker": "first_name", "regex": r"^[A-Za-z ]+$"},
    "last_name": {"faker": "last_name", "regex": r"^[A-Za-z ]+$"},
    "address": {"faker": "address", "regex": r"^[A-Za-z0-9\s,.-]+$"},
    "HCID": {"generator": lambda: faker.Faker().numerify("##########"), "regex": r"^\d{9}$"},
    "UM_id": {"generator": lambda: faker.Faker().numerify("########"), "regex": r"^\d{8}$"},
    "DCN": {"generator": lambda: faker.Faker().numerify("##########"), "regex": r"^\d{9}$"},
    "policy number": {"generator": lambda: faker.Faker().numerify("######-####"), "regex": r"^\d{6}-\d{4}$"},
    "claim amount": {"generator": lambda: round(faker.Faker().random.uniform(100.0, 5000.0), 2), "regex": r"^\d+(\.\d{2})?$"},
    "ICD-10 codes": {"generator": lambda: faker.Faker().random_element(elements=("S06.0X0A", "I10", "Z91.81")), "regex": r"^[A-Z][0-9].[0-9]{1}([A-Z])?$"},
    "CPT codes": {"generator": lambda: faker.Faker().random_element(elements=("99213", "77067", "36415-59")), "regex": r"^\d{5}(?:-\d{1,2})?$"}
}

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
