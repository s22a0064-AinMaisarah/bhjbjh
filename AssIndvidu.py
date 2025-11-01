import streamlit as st

st.set_page_config(page_title="Urban Crime Analytics Visualization Dashboard", layout="wide")

st.header("Explore trends, hotspots, and patterns through interactive visuals")

st.write("""
This dashboard presents an interactive visualization of urban crime data, enabling deeper
understanding of crime distribution and supporting data-driven decision-making for urban safety and policy planning.
""")

st.write("""
This dataset, originally titled "Uber and Urban Crime" (Bryan Weber, 2019), focuses on
crime-related data within urban environments. While it references Uber, this dashboard
analyzes the crime dimension — exploring patterns, frequency, and distribution.
""")

st.sidebar.success("Select a page above to explore the objectives.")
