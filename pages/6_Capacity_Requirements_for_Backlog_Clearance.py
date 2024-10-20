# pages/6_Capacity_Requirements_for_Backlog_Clearance.py

import streamlit as st

st.title("6. Capacity Requirements for Backlog Clearance")

if 'number_waiting_longer' in st.session_state:
    st.subheader("Calculate Additional Capacity Needed")
    with st.form("backlog_clearance"):
        clearance_timeframe_weeks = st.number_input("Desired Backlog Clearance Timeframe (Weeks)", min_value=1, value=12)
        submitted = st.form_submit_button("Calculate Required Capacity")
        
        if submitted:
            number_waiting_longer = st.session_state['number_waiting_longer']
            avg_duration = st.session_state['data']['Average Duration'].mean()
            total_hours_needed = number_waiting_longer * avg_duration
            effective_session_time = st.session_state.get('session_length', 4.0) * (st.session_state.get('utilization_rate', 85) / 100)
            additional_sessions_needed_per_week = (total_hours_needed / effective_session_time) / clearance_timeframe_weeks
            st.subheader("Additional Capacity Requirements")
            st.write(f"Additional Sessions Needed per Week: {additional_sessions_needed_per_week:.2f}")
else:
    st.error("Please input waiting list details in the previous page.")
