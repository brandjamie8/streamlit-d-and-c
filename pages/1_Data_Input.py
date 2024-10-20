# pages/1_Data_Input.py

import streamlit as st
import pandas as pd
import numpy as np

st.title("1. Data Input")

data_option = st.radio("Select Data Input Method:", ("Upload Data", "Use Simulated Data"))

if data_option == "Upload Data":
    uploaded_file = st.file_uploader("Upload your CSV or Excel file", type=["csv", "xlsx"])
    if uploaded_file:
        try:
            if uploaded_file.name.endswith('.csv'):
                data = pd.read_csv(uploaded_file)
            else:
                data = pd.read_excel(uploaded_file)
            st.success("Data loaded successfully!")
            st.write("Data Preview:")
            st.dataframe(data.head())
            st.session_state['data'] = data
        except Exception as e:
            st.error(f"Error loading data: {e}")
else:
    st.subheader("Simulated Data Parameters")
    num_procedures = st.number_input("Number of Procedures", min_value=1, value=10)
    avg_patients = st.number_input("Average Patients Added per Procedure per Day", min_value=1, value=5)
    avg_duration = st.number_input("Average Procedure Duration (hours)", min_value=0.1, value=1.0)
    num_days = st.number_input("Number of Days to Simulate", min_value=1, value=365)
    
    simulate_button = st.button("Generate Simulated Data")
    
    if simulate_button:
        procedures = [f"Procedure {i+1}" for i in range(num_procedures)]
        data_list = []
        for day in range(num_days):
            for proc in procedures:
                num_added = np.random.poisson(avg_patients)
                duration = np.random.normal(avg_duration, 0.1 * avg_duration)
                data_list.append({
                    'Date': pd.Timestamp('2023-01-01') + pd.Timedelta(days=day),
                    'Procedure': proc,
                    'Number Added': max(num_added, 0),
                    'Average Duration': max(duration, 0.1)
                })
        data = pd.DataFrame(data_list)
        st.success("Simulated data generated successfully!")
        st.write("Data Preview:")
        st.dataframe(data.head())
        st.session_state['data'] = data
