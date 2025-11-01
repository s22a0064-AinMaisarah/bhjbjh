import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

st.set_page_config(page_title="Objective 3 — Preferred Start Time & Correlation Matrix", layout="wide")

st.title("Objective 3 — Demographic Influence on Crime Categories")

url = "https://raw.githubusercontent.com/s22a0064-AinMaisarah/Crime/refs/heads/main/df_crime_cleaned.csv"
df = pd.read_csv(url)

crime_cols = ['violent_crime', 'property_crime', 'whitecollar_crime', 'social_crime']

df['male_category'] = pd.qcut(df['male'], q=3, labels=['Low-Male', 'Balanced-Gender', 'High-Male'])
male_means = df.groupby('male_category')[crime_cols].mean().reset_index()
melted = male_means.melt(id_vars='male_category', var_name='Crime Type', value_name='Average Crime Score')

fig_gender = px.bar(
    melted, x='Crime Type', y='Average Crime Score', color='male_category',
    title='Average Crime Scores by Male Population Category'
)
st.plotly_chart(fig_gender)

age_means = df.groupby('age')[crime_cols].mean().reset_index()

fig = go.Figure()
for _, row in age_means.iterrows():
    fig.add_trace(go.Scatterpolar(r=row[crime_cols].tolist(), theta=crime_cols, fill='toself', name=f"Age {row['age']}"))
fig.update_layout(title='Radar Chart: Crime Scores by Age Group', showlegend=True)
st.plotly_chart(fig)
