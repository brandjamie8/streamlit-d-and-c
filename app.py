# app.py

import streamlit as st

st.set_page_config(page_title="Hospital Demand and Capacity Modeling", layout="wide")

st.title("Hospital Demand and Capacity Modeling")

st.sidebar.success("Select a page above.")

st.markdown("""
Welcome to the **Hospital Demand and Capacity Modeling** app. Use the sidebar to navigate through the pages.

This app allows you to:

- Input real or simulated data.
- Configure variables such as operational weeks and utilization rates.
- Analyze current capacity and model optimal capacity.
- Manage waiting lists and backlogs.
- Calculate capacity requirements to clear backlogs.
- Visualize results with advanced charts.
""")
