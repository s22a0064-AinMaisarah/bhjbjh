import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

st.set_page_config(page_title="Objective 3 — Preferred Start Time & Correlation Matrix", layout="wide")

st.title("Objective 3 — Demographic Influence on Crime Categories")

# Load dataset
url = "https://raw.githubusercontent.com/s22a0064-AinMaisarah/Crime/refs/heads/main/df_crime_cleaned.csv"
df = pd.read_csv(url)

crime_cols = ['violent_crime', 'property_crime', 'whitecollar_crime', 'social_crime']

# -------------------- Gender Based Crime Plot --------------------
df['male_category'] = pd.qcut(df['male'], q=3, labels=['Low-Male', 'Balanced-Gender', 'High-Male'])
male_means = df.groupby('male_category')[crime_cols].mean().reset_index()
melted = male_means.melt(id_vars='male_category', var_name='Crime Type', value_name='Average Crime Score')

fig_gender = px.bar(
    melted, x='Crime Type', y='Average Crime Score', color='male_category',
    title='Average Crime Scores by Male Population Category'
)
st.plotly_chart(fig_gender)

# -------------------- Radar Chart based on Age --------------------
age_means = df.groupby('age')[crime_cols].mean().reset_index()

fig = go.Figure()
for _, row in age_means.iterrows():
    fig.add_trace(go.Scatterpolar(r=row[crime_cols].tolist(), theta=crime_cols, fill='toself', name=f"Age {row['age']}"))
fig.update_layout(title='Radar Chart: Crime Scores by Age Group', showlegend=True)
st.plotly_chart(fig)

# -------------------- Education vs Crime Violin Plot --------------------
st.subheader("Education Level vs Crime Distribution")

education_cols = ['high_school_below', 'high_school', 'some_college', 'bachelors_degree']

# Melt crime columns
crime_melted = df.melt(
    value_vars=crime_cols,
    var_name='Crime Type',
    value_name='Crime Score',
    id_vars=education_cols
)

# Melt education columns within crime melted data
education_crime_melted = crime_melted.melt(
    id_vars=['Crime Type', 'Crime Score'],
    value_vars=education_cols,
    var_name='Education Level',
    value_name='Education Percentage'
)

# Violin Plot
fig_violin = px.violin(
    education_crime_melted,
    x='Education Level',
    y='Crime Score',
    color='Crime Type',
    box=True,
    points="all",
    hover_data=['Crime Type', 'Crime Score', 'Education Level', 'Education Percentage'],
    title='Distribution of Crime Scores by Education Level and Crime Type',
    labels={'Education Level': 'Education Level', 'Crime Score': 'Crime Score'}
)

fig_violin.update_layout(xaxis_title='Education Level', yaxis_title='Crime Score')

st.plotly_chart(fig_violin, use_container_width=True)
