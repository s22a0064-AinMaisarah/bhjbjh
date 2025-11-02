import streamlit as st
import pandas as pd
import plotly.express as px

# ---------------------------------------------------------
# PAGE SETTINGS
# ---------------------------------------------------------
st.set_page_config(
    page_title="Objective 2 — Socioeconomic vs Crime Analysis",
    page_icon="📊",
    layout="wide"
)

# ---------------------------------------------------------
# SIDEBAR
# ---------------------------------------------------------
with st.sidebar:
    st.title("📊 Objective 2 Dashboard")
    st.caption("Analyzing socioeconomic indicators & crime patterns")
    st.markdown("---")
    st.caption("📍 Developed by Ain Maisarah")

# ---------------------------------------------------------
# PAGE TITLE & INTRO
# ---------------------------------------------------------
st.title("📈 Objective 2 — Socioeconomic Factors & Crime Patterns")

st.markdown("""
### 🎯 Objective  
To investigate whether **socioeconomic factors** such as **income** and **poverty levels** 
influence **crime rates** across different city categories.

We aim to identify relationships between:  
- 💰 **Income** → Crime levels  
- 📉 **Poverty rate** → Crime levels  
- 🏙️ **City category groups** (Urban classifications)  

This helps understand how **economic status impacts crime behavior**.
""")

# ---------------------------------------------------------
# LOAD DATA
# ---------------------------------------------------------
url = "https://raw.githubusercontent.com/s22a0064-AinMaisarah/Crime/refs/heads/main/df_crime_cleaned.csv"
df = pd.read_csv(url)

st.success("✅ Dataset Loaded Successfully")

# Dataset description box
with st.expander("📂 Dataset Information"):
    st.write("""
This dataset originates from the **Urban Crime Analysis** compiled in **2019**.  
It includes socioeconomic and crime indicators across urban locations.

**Key Variables Used:**
- `income` → Average income of city population  
- `poverty` → % population below poverty line  
- `offense_count` → Total recorded offenses  
- `city_cat` → City category (0 = Group II, 1 = Group I)  
- Crime breakdown → violent, property, white-collar, social crime  

The goal is to explore how **economics influences crime behavior** in different city groups.
""")

st.subheader("🧾 Dataset Preview")
st.dataframe(df.head(), use_container_width=True)

st.markdown("---")

# ---------------------------------------------------------
# ✅ Income vs Offense Count
# ---------------------------------------------------------
st.header("💰 Income vs Crime — Does Higher Income Reduce Crime?")

fig_income_offense = px.scatter(
    df,
    x='income',
    y='offense_count',
    color='city_cat',
    hover_data=['city_cat', 'income', 'offense_count', 'violent_crime',
                'property_crime', 'whitecollar_crime', 'social_crime', 'state', 'age'],
    title="Income vs Offense Count by City Category",
    labels={'city_cat': 'City Category (0: Group II, 1: Group I)'},
    trendline='ols'
)
st.plotly_chart(fig_income_offense, use_container_width=True)

st.info("💡 Higher-income cities show **lower offense counts**, supporting socioeconomic influence on crime.")

st.markdown("---")

# ---------------------------------------------------------
# ✅ Poverty vs Offense Count
# ---------------------------------------------------------
st.header("📉 Poverty vs Crime — Does Poverty Increase Crime?")

fig_poverty_offense = px.scatter(
    df,
    x='poverty',
    y='offense_count',
    color='city_cat',
    hover_data=['city_cat', 'poverty', 'offense_count', 'violent_crime',
                'property_crime', 'whitecollar_crime', 'social_crime', 'state', 'age'],
    title="Poverty % vs Offense Count by City Category",
    labels={'city_cat': 'City Category (0: Group II, 1: Group I)'},
    trendline='ols'
)
st.plotly_chart(fig_poverty_offense, use_container_width=True)

st.warning("📌 Higher poverty levels tend to correlate with **increased crime activity**.")

st.markdown("---")

# ---------------------------------------------------------
# ✅ Income vs City Category — Yellow Theme
# ---------------------------------------------------------
st.header("💛 Income vs City Category (Yellow Theme)")

fig_income_citycat = px.scatter(
    df,
    x='income',
    y='city_cat',
    color='city_cat',
    color_discrete_sequence=['gold', 'yellow'],
    hover_data=['city_cat', 'income', 'offense_count', 'violent_crime',
                'property_crime', 'whitecollar_crime', 'social_crime'],
    title="Income vs City Category (Yellow Theme)",
    labels={'city_cat': 'City Category (0: Group II, 1: Group I)'}
)
st.plotly_chart(fig_income_citycat, use_container_width=True)

st.markdown("---")

# ---------------------------------------------------------
# ✅ Poverty vs City Category — Yellow Theme
# ---------------------------------------------------------
st.header("💛 Poverty % vs City Category (Yellow Theme)")

fig_poverty_citycat = px.scatter(
    df,
    x='poverty',
    y='city_cat',
    color='city_cat',
    color_discrete_sequence=['gold', 'yellow'],
    hover_data=['city_cat', 'poverty', 'offense_count', 'violent_crime',
                'property_crime', 'whitecollar_crime', 'social_crime'],
    title="Poverty % vs City Category (Yellow Theme)",
    labels={'city_cat': 'City Category (0: Group II, 1: Group I)'}
)
st.plotly_chart(fig_poverty_citycat, use_container_width=True)

st.success("✅ Visualizations Rendered Successfully — Objective 2 Complete 🎉")
