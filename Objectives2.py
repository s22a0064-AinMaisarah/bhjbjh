import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Objective 2 — Group Comparisons and Chronotype", layout="wide")

st.title("Objective 2 — Group Comparisons and Chronotype")

# Load Data
url = "https://raw.githubusercontent.com/s22a0064-AinMaisarah/Crime/refs/heads/main/df_crime_cleaned.csv"
df = pd.read_csv(url)

st.success("✅ Dataset Loaded")
st.dataframe(df.head())

# ==================== Scatter: Income vs Offense ====================
st.subheader("Income vs Offense Count by City Category")

fig_income = px.scatter(
    df, x='income', y='offense_count', color='city_cat',
    title='Income vs. Offense Count by City Category', trendline='ols',
    hover_data=['city_cat','income','offense_count','violent_crime','property_crime','whitecollar_crime','social_crime']
)
st.plotly_chart(fig_income, use_container_width=True)

# ==================== Scatter: Poverty vs Offense ====================
st.subheader("Poverty vs Offense Count by City Category")

fig_poverty = px.scatter(
    df, x='poverty', y='offense_count', color='city_cat',
    title='Poverty vs. Offense Count by City Category', trendline='ols',
    hover_data=['city_cat','poverty','offense_count','violent_crime','property_crime','whitecollar_crime','social_crime']
)
st.plotly_chart(fig_poverty, use_container_width=True)

# ==================== Scatter: Income vs City Category ====================
st.subheader("Income vs City Category (Interactive)")

fig_income_citycat = px.scatter(
    df,
    x='income',
    y='city_cat',
    color='city_cat',
    hover_data=['city_cat', 'income', 'offense_count', 'violent_crime', 'property_crime', 'whitecollar_crime', 'social_crime'],
    title='Interactive Scatter Plot: Income vs City Category',
    labels={'city_cat': 'City Category (0: Group II, 1: Group I)'}
)
st.plotly_chart(fig_income_citycat, use_container_width=True)

# ==================== Scatter: Poverty vs City Category ====================
st.subheader("Poverty % vs City Category (Interactive)")

fig_poverty_citycat = px.scatter(
    df,
    x='poverty',
    y='city_cat',
    color='city_cat',
    hover_data=['city_cat', 'poverty', 'offense_count', 'violent_crime', 'property_crime', 'whitecollar_crime', 'social_crime'],
    title='Interactive Scatter Plot: Poverty % vs City Category',
    labels={'city_cat': 'City Category (0: Group II, 1: Group I)'}
)
st.plotly_chart(fig_poverty_citycat, use_container_width=True)

st.success("✅ All visualizations loaded successfully!")
