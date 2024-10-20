# pages/5_Waiting_List_and_Backlog_Management.py

import streamlit as st
import pandas as pd

st.title("5. Waiting List and Backlog Management")

with st.form("backlog_management"):
    st.subheader("Current Waiting List Details")
    current_waiting_list_size = st.number_input("Current Waiting List Size (Number of Patients)", min_value=0, value=100)
    target_weeks_wait = st.number_input("Target Weeks Wait", min_value=1, value=12)
    number_waiting_longer = st.number_input("Number Waiting Longer Than Target", min_value=0, value=20)
    percentage_for_long_waiters = st.slider("Percentage of Activity for Long Waiters (%)", min_value=0, max_value=100, value=20)
    submitted = st.form_submit_button("Calculate Backlog Projections")
    
    if submitted:
        st.session_state['current_waiting_list_size'] = current_waiting_list_size
        st.session_state['target_weeks_wait'] = target_weeks_wait
        st.session_state['number_waiting_longer'] = number_waiting_longer
        st.session_state['percentage_for_long_waiters'] = percentage_for_long_waiters
        
        # Simplified projection calculations
        data = st.session_state['data']
        total_patients_added_per_week = data.groupby(data['Date'].dt.isocalendar().week)['Number Added'].sum().mean()
        total_capacity_per_week = st.session_state.get('sessions_per_week_current', 100) * st.session_state.get('utilization_rate', 85) / 100
        
        projected_waiting_list_size = current_waiting_list_size + (total_patients_added_per_week - total_capacity_per_week) * st.session_state.get('weeks_run', 48)
        projected_backlog_size = max(projected_waiting_list_size - (total_capacity_per_week * target_weeks_wait), 0)
        
        st.subheader("Backlog Projection Results")
        st.write(f"Expected Waiting List Size at End of Year: {projected_waiting_list_size:.0f} patients")
        st.write(f"Expected Backlog Size at End of Year: {projected_backlog_size:.0f} patients")
else:
    st.error("Please input data and configure variables first.")
