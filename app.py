'''import streamlit as st
import joblib
import numpy as np

# Load the trained model and scaler
model = joblib.load("model_and_data.pkl")  # Replace with your model file name
scaler = joblib.load("scaler.pkl")  # Replace with your scaler file name (if used)

# Streamlit app title
st.title("Credit Card Fraud Detection")

# Description
st.markdown("""
This app predicts whether a transaction is **fraudulent** or **not fraudulent** based on input features. 
Fill in the fields below and click **Predict**.
""")

# Input fields for features
st.header("Enter Transaction Details:")
features = []
num_features = 5  # Adjust this to match your model's number of input features

for i in range(1, num_features + 1):
    feature_value = st.number_input(f"Feature {i}", value=0.0)
    features.append(feature_value)

# Prediction button
if st.button("Predict"):
    try:
        # Preprocess the input (scale the features if scaler is used)
        scaled_features = scaler.transform([features])  # Make it a 2D array
        prediction = model.predict(scaled_features)
        result = "Fraudulent" if prediction[0] == 1 else "Not Fraudulent"

        # Display the result
        st.subheader("Prediction Result:")
        st.write(f"The transaction is **{result}**.")
    except Exception as e:
        st.error(f"Error during prediction: {e}")'''

import streamlit as st
import pandas as pd

# Load the CSV file
@st.cache
def load_data():
    # Replace "exportt.csv" with the path to your file
    try:
        return pd.read_csv("exportt.csv")
    except Exception as e:
        st.error(f"Error loading file: {e}")
        return None

# Load the data
data = load_data()

# Title
st.title("Credit card Fraudulence viewer")

if data is not None:
    # Display a description
    st.markdown("""
    Use this tool to fetch incident details based on inputs like insured occupation and sex. 
    """)

    # Input filters
    insured_occupation = st.selectbox("Select Insured Occupation:", options=data["insured_occupation"].unique())
    insured_sex = st.selectbox("Select Insured Sex:", options=data["insured_sex"].unique())

    # Filter data based on inputs
    filtered_data = data[
        (data["insured_occupation"] == insured_occupation) & 
        (data["insured_sex"] == insured_sex)
    ]

    if not filtered_data.empty:
        # Select columns to display
        st.subheader("Incident Details")
        st.write(filtered_data[[
            "incident_date", 
            "incident_type", 
            "incident_severity", 
            "authorities_contacted", 
            "incident_city", 
            "police_report_available", 
            "fraud_reported"
        ]])
    else:
        st.warning("No data found for the selected filters.")
else:
    st.warning("Unable to load data. Please check your file.")

# Additional UI
st.markdown("""
**Note:** Ensure the file `exportt.csv` is present in the same directory as this script, 
or provide the correct path to it.
""")
