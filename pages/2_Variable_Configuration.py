# pages/2_Variable_Configuration.py

import streamlit as st

st.title("2. Variable Configuration")

with st.form("variable_configuration"):
    st.subheader("Adjustable Variables")
    weeks_run = st.slider("Number of Weeks Run in a Year", min_value=1, max_value=52, value=48)
    utilization_rate = st.slider("Utilization Rate (%)", min_value=0, max_value=100, value=85)
    session_length = st.number_input("Session Length (hours)", min_value=1.0, max_value=12.0, value=4.0)
    num_theatres = st.number_input("Number of Theatres", min_value=1, value=5)
    staff_availability = st.slider("Staff Availability (%)", min_value=0, max_value=100, value=90)
    equipment_constraints = st.slider("Equipment Availability (%)", min_value=0, max_value=100, value=95)
    cancellation_rate = st.slider("Cancellation Rate (%)", min_value=0, max_value=100, value=5)
    submitted = st.form_submit_button("Save Configuration")
    
    if submitted:
        st.session_state['weeks_run'] = weeks_run
        st.session_state['utilization_rate'] = utilization_rate
        st.session_state['session_length'] = session_length
        st.session_state['num_theatres'] = num_theatres
        st.session_state['staff_availability'] = staff_availability
        st.session_state['equipment_constraints'] = equipment_constraints
        st.session_state['cancellation_rate'] = cancellation_rate
        st.success("Configuration saved!")
