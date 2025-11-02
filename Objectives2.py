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

# ==============================================
# ✅ Interactive Scatter: Income vs Offense Count
# ==============================================
st.subheader("Income vs Offense Count by City Category")

fig_income_offense = px.scatter(
    df,
    x='income',
    y='offense_count',
    color='city_cat',
    hover_data=['city_cat', 'income', 'offense_count', 'violent_crime', 
                'property_crime', 'whitecollar_crime', 'social_crime', 'state', 'age'],
    title='Interactive Scatter Plot: Income vs Offense Count by City Category',
    labels={'city_cat': 'City Category (0: Group II, 1: Group I)'},
    trendline='ols'
)
st.plotly_chart(fig_income_offense, use_container_width=True)

# ==============================================
# ✅ Interactive Scatter: Poverty vs Offense Count
# ==============================================
st.subheader("Poverty % vs Offense Count by City Category")

fig_poverty_offense = px.scatter(
    df,
    x='poverty',
    y='offense_count',
    color='city_cat',
    hover_data=['city_cat', 'poverty', 'offense_count', 'violent_crime', 
                'property_crime', 'whitecollar_crime', 'social_crime', 'state', 'age'],
    title='Interactive Scatter Plot: Poverty % vs Offense Count by City Category',
    labels={'city_cat': 'City Category (0: Group II, 1: Group I)'},
    trendline='ols'
)
st.plotly_chart(fig_poverty_offense, use_container_width=True)

# ==============================================
# ✅ Income vs City Category — change color to Yellow
# ==============================================
st.subheader("Income vs City Category (Yellow Theme)")

fig_income_citycat = px.scatter(
    df,
    x='income',
    y='city_cat',
    color='city_cat',
    color_discrete_sequence=['gold', 'yellow'], # 🔥 Yellow tones
    hover_data=['city_cat', 'income', 'offense_count', 'violent_crime', 
                'property_crime', 'whitecollar_crime', 'social_crime'],
    title='Income vs City Category (Yellow Theme)',
    labels={'city_cat': 'City Category (0: Group II, 1: Group I)'}
)
st.plotly_chart(fig_income_citycat, use_container_width=True)

# ==============================================
# ✅ Poverty vs City Category — change color to Yellow
# ==============================================
st.subheader("Poverty % vs City Category (Yellow Theme)")

fig_poverty_citycat = px.scatter(
    df,
    x='poverty',
    y='city_cat',
    color='city_cat',
    color_discrete_sequence=['gold', 'yellow'], # 🔥 Yellow tones
    hover_data=['city_cat', 'poverty', 'offense_count', 'violent_crime', 
                'property_crime', 'whitecollar_crime', 'social_crime'],
    title='Poverty % vs City Category (Yellow Theme)',
    labels={'city_cat': 'City Category (0: Group II, 1: Group I)'}
)
st.plotly_chart(fig_poverty_citycat, use_container_width=True)

st.success("✅ Updated interactive charts successfully loaded!")
