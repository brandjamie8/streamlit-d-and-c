# pages/4_Optimal_Capacity_Modeling.py

import streamlit as st

st.title("4. Optimal Capacity Modeling")

if 'data' in st.session_state:
    st.write("Adjust variables to model optimal capacity.")
    
    with st.form("optimal_capacity"):
        new_utilization_rate = st.slider("Utilization Rate (%)", min_value=0, max_value=100, value=st.session_state.get('utilization_rate', 85))
        new_num_theatres = st.number_input("Number of Theatres", min_value=1, value=st.session_state.get('num_theatres', 5))
        new_session_length = st.number_input("Session Length (hours)", min_value=1.0, max_value=12.0, value=st.session_state.get('session_length', 4.0))
        submitted = st.form_submit_button("Run Optimal Capacity Analysis")
        
        if submitted:
            data = st.session_state['data']
            total_patients = data['Number Added'].sum()
            avg_duration = data['Average Duration'].mean()
            weeks_run = st.session_state.get('weeks_run', 48)
            effective_session_time = new_session_length * (new_utilization_rate / 100)
            total_hours_needed = total_patients * avg_duration
            total_sessions_needed = total_hours_needed / effective_session_time
            sessions_per_week_needed = total_sessions_needed / weeks_run
            sessions_per_week_current = new_num_theatres * (40 / new_session_length)
            
            st.subheader("Optimal Capacity Analysis Results")
            st.write(f"Sessions Needed per Week: {sessions_per_week_needed:.2f}")
            st.write(f"Available Sessions per Week with New Configuration: {sessions_per_week_current:.2f}")
            st.write(f"Difference in Sessions per Week: {sessions_per_week_needed - sessions_per_week_current:.2f}")
else:
    st.error("Please input data in the Data Input page first.")
