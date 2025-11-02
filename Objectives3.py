import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# ===================== PAGE CONFIG =====================
st.set_page_config(page_title="Objective 3 — Demographics & Crime Patterns", layout="wide")

# ===================== PAGE HEADER =====================
st.title("🧠 Objective 3 — Demographic Influence on Crime Categories")

st.markdown("""
### 🎯 Objective  
To analyze how demographics — **gender ratio, age distribution, and education level** — influence different crime categories across cities.  
This helps identify social factors linked with crime behavior and urban safety patterns.  
""")

# ===================== LOAD DATA =====================
url = "https://raw.githubusercontent.com/s22a0064-AinMaisarah/Crime/refs/heads/main/df_crime_cleaned.csv"
df = pd.read_csv(url)

with st.expander("📂 About the Dataset"):
    st.write("""
This dataset was originally titled **“Uber and Urban Crime”**, published by Bryan Weber (2019, Mendeley Database).  
It includes socio-demographic and crime statistics across U.S. cities, focusing on relationships between  
**urban population characteristics and crime distribution**.

In this section, the focus is on:
- Gender ratio (Male population %)
- Age groups
- Education attainment levels  

and how they relate to **violent, property, white-collar, and social crimes**.
""")

st.success("✅ Dataset Loaded Successfully")
st.dataframe(df.head())

# ===================== SUMMARY METRICS =====================
st.subheader("📊 Summary Metrics")

col1, col2, col3, col4 = st.columns(4)

col1.metric("Crime Variables", "4", help="violent, property, white-collar, social crime", border=True)
col2.metric("Demographic Dimensions", "3", help="Gender, Age, Education", border=True)
col3.metric("Dataset Size", str(df.shape[0]), help="Total city-level observations analyzed", border=True)
col4.metric("Education Groups", "4", help="High school below, high school, college, bachelor’s", border=True)

# Common crime columns
crime_cols = ['violent_crime', 'property_crime', 'whitecollar_crime', 'social_crime']

st.markdown("---")

# ===================== GENDER ANALYSIS =====================
st.subheader("👥 Crime Patterns by Male Population Category")

df['male_category'] = pd.qcut(df['male'], q=3, labels=['Low-Male', 'Balanced-Gender', 'High-Male'])
male_means = df.groupby('male_category')[crime_cols].mean().reset_index()
melted = male_means.melt(id_vars='male_category', var_name='Crime Type', value_name='Average Crime Score')

fig_gender = px.bar(
    melted,
    x='Crime Type', y='Average Crime Score',
    color='male_category',
    title='Average Crime Scores by Male Population Groups'
)
st.plotly_chart(fig_gender, use_container_width=True)

st.info("📍 *Cities with higher male ratios tend to show greater violent and property crime scores.*")

st.markdown("---")

# ===================== AGE ANALYSIS (RADAR CHART) =====================
st.subheader("📅 Crime Distribution Across Age Groups")

age_means = df.groupby('age')[crime_cols].mean().reset_index()

fig = go.Figure()
for _, row in age_means.iterrows():
    fig.add_trace(go.Scatterpolar(
        r=row[crime_cols].tolist(),
        theta=crime_cols,
        fill='toself',
        name=f"Age {row['age']}"
    ))

fig.update_layout(title='Radar Chart: Crime Scores by Age Group', showlegend=True)
st.plotly_chart(fig, use_container_width=True)

st.info("📍 *Younger-population cities tend to have higher social and property crime trends.*")

st.markdown("---")

# ===================== EDUCATION VS CRIME =====================
st.subheader("🎓 Education Level vs Crime Distribution")

education_cols = ['high_school_below', 'high_school', 'some_college', 'bachelors_degree']

crime_melted = df.melt(
    value_vars=crime_cols,
    var_name='Crime Type',
    value_name='Crime Score',
    id_vars=education_cols
)

education_crime_melted = crime_melted.melt(
    id_vars=['Crime Type', 'Crime Score'],
    value_vars=education_cols,
    var_name='Education Level',
    value_name='Education Percentage'
)

fig_violin = px.violin(
    education_crime_melted,
    x='Education Level',
    y='Crime Score',
    color='Crime Type',
    box=True,
    points="all",
    hover_data=['Crime Type', 'Crime Score', 'Education Level', 'Education Percentage'],
    title='Distribution of Crime Scores by Education Level and Crime Type'
)

fig_violin.update_layout(xaxis_title='Education Level', yaxis_title='Crime Score')
st.plotly_chart(fig_violin, use_container_width=True)

st.info("📍 *Higher education levels correlate with lower violent crime but mixed trends for white-collar crime.*")

# ===================== INTERPRETATION =====================
st.markdown("""
---

### 🧠 Final Insight & Interpretation

Demographic factors play a significant role in shaping crime trends:

- **Higher male population cities** tend to show **greater violent and property crime**
- **Younger cities** show elevated **social and property offenses**
- **Higher education attainment** appears protective for **violent crime**,  
  but **white-collar crime** may increase in highly educated areas

These findings underline the importance of **community-level social development** in crime prevention.

---
""")
