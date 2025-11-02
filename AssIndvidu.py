import streamlit as st

st.set_page_config(page_title="Crime Analytics Dashboard")

# Import pages
page1 = st.Page("Objectives1.py", title="K-Means Clustering + PCA", icon=":material/analytics:")
page2 = st.Page("Objectives2.py", title="Income vs Crime", icon=":material/scatter_plot:")
page3 = st.Page("Objectives3.py", title="Radar Chart by Age Group", icon=":material/radar:")

# Navigation
navigation = st.navigation(
    {
        "Crime Analysis Dashboard": [page1, page2, page3]
    }
)

navigation.run()
