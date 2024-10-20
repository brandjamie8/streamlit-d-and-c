# pages/3_Current_Capacity_Analysis.py

import streamlit as st
import pandas as pd

st.title("3. Current Capacity Analysis")

if 'data' in st.session_state:
    data = st.session_state['data']
    st.write("Using data from previous steps.")

    # Calculations
    total_patients = data['Number Added'].sum()
    avg_duration = data['Average Duration'].mean()

    weeks_run = st.session_state.get('weeks_run', 48)
    utilization_rate = st.session_state.get('utilization_rate', 85)
    session_length = st.session_state.get('session_length', 4.0)
    num_theatres = st.session_state.get('num_theatres', 5)
    effective_session_time = session_length * (utilization_rate / 100)
    
    total_hours_needed = total_patients * avg_duration
    total_sessions_needed = total_hours_needed / effective_session_time
    sessions_per_week_needed = total_sessions_needed / weeks_run
    sessions_per_week_current = num_theatres * (40 / session_length)  # Assuming 40 hours per week per theatre
    
    st.subheader("Capacity Analysis Results")
    st.write(f"Total Patients Added: {total_patients}")
    st.write(f"Average Procedure Duration: {avg_duration:.2f} hours")
    st.write(f"Total Hours Needed: {total_hours_needed:.2f} hours")
    st.write(f"Effective Session Time: {effective_session_time:.2f} hours")
    st.write(f"Total Sessions Needed: {total_sessions_needed:.2f}")
    st.write(f"Sessions Needed per Week: {sessions_per_week_needed:.2f}")
    st.write(f"Current Sessions per Week Available: {sessions_per_week_current:.2f}")
    st.write(f"Difference in Sessions per Week: {sessions_per_week_needed - sessions_per_week_current:.2f}")
else:
    st.error("Please input data in the Data Input page first.")
