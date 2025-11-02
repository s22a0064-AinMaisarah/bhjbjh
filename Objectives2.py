import streamlit as st
import pandas as pd
import plotly.express as px

# ---------------------------------------------------------
# PAGE HEADER
# ---------------------------------------------------------
st.title("🚨 Socioeconomic Determinants of Crime: Income, Poverty & Offense Patterns Across Cities")

st.markdown("""
### 🎯 Research Objective  

To investigate how income levels and poverty rates influence overall crime incidence across different city categories.  
This analysis aims to determine whether socioeconomic disparities serve as predictors of crime intensity, providing insights into how economic conditions shape urban crime dynamics.
""")

# Load Data
url = "https://raw.githubusercontent.com/s22a0064-AinMaisarah/Crime/refs/heads/main/df_crime_cleaned.csv"
df = pd.read_csv(url)

st.success("✅ Dataset Loaded")
st.dataframe(df.head())

# ====================== SUMMARY METRICS ======================
st.markdown("### 📊 Key Dataset Summary")

col1, col2, col3, col4 = st.columns(4)

col1.metric("Crime Variables", "4", help="violent, property, white-collar, social crime", border=True)
col2.metric("Demographic Dimensions", "3", help="Gender, Age, Education", border=True)
col3.metric("Dataset Size", str(df.shape[0]), help="Total city-level observations analyzed", border=True)
col4.metric("Education Groups", "4", help="High school below, high school, college, bachelor’s", border=True)


# ==============================================
# ✅ Income vs Offense Count
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
# ✅ Poverty vs Offense Count
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
# ✅ Income vs City Category — Yellow Theme
# ==============================================
st.subheader("Income vs City Category")

fig_income_citycat = px.scatter(
    df,
    x='income',
    y='city_cat',
    color='city_cat',
    color_discrete_sequence=['gold', 'yellow'],
    hover_data=['city_cat', 'income', 'offense_count', 'violent_crime', 
                'property_crime', 'whitecollar_crime', 'social_crime'],
    title='Income vs City Category',
    labels={'city_cat': 'City Category (0: Group II, 1: Group I)'}
)
st.plotly_chart(fig_income_citycat, use_container_width=True)

# ==============================================
# ✅ Poverty vs City Category — Yellow Theme
# ==============================================
st.subheader("Poverty % vs City Category")

fig_poverty_citycat = px.scatter(
    df,
    x='poverty',
    y='city_cat',
    color='city_cat',
    color_discrete_sequence=['gold', 'yellow'],
    hover_data=['city_cat', 'poverty', 'offense_count', 'violent_crime', 
                'property_crime', 'whitecollar_crime', 'social_crime'],
    title='Poverty % vs City Category',
    labels={'city_cat': 'City Category (0: Group II, 1: Group I)'}
)
st.plotly_chart(fig_poverty_citycat, use_container_width=True)

st.success("✅ Updated interactive charts successfully loaded!")

# ===================== INTERPRETATION =====================
st.markdown("""
---
### 🧠 Final Insight & Interpretation

The visual analytics collectively highlight the critical role of socioeconomic conditions in shaping crime dynamics across urban areas. 

---

#### 📍 **Scatter Plot: Income vs Offense Count**
Cities with lower income levels demonstrate a noticeably higher number of recorded offenses.  
This inverse relationship suggests that limited economic resources may contribute to increased social vulnerability, potentially driving individuals toward unlawful activities due to:

- Financial stress and resource scarcity  
- Lower employment opportunities  
- Weak social support systems  

This pattern aligns with Economic Strain Theory, which posits that restricted financial opportunities heighten crime risk.

---

#### 📍 **Scatter Plot: Poverty Rate vs Offense Count**
A strong positive correlation is observed between poverty rate and offense rate across both city categories.  
Cities facing elevated poverty levels report substantially higher crime occurrences.  

Possible contributing factors include:

- Inequality-induced social tension  
- Limited access to education and social services  
- Structural disadvantages in high-poverty communities  

This supports Social Disorganization Theory, emphasizing that community instability drives crime.

---

#### 📍 **Income vs City Category (Yellow Theme)**
Higher-tier cities (**Group I**) exhibit greater income variation, reflecting diverse economic segments within larger urban environments.  

- Group I: Broader income range — mixed affluent + vulnerable populations  
- Group II: More income homogeneity — typically medium- or smaller-scale cities  

This variance underscores the urban economic diversity often associated with crime concentration pockets.

---

#### 📍 **Poverty vs City Category **
Group I cities show more pronounced poverty variation compared to Group II.  
This suggests that large metropolitan regions may experience wider socioeconomic inequality, which can:

- Increase crime concentration in marginalized districts  
- Create high-risk zones linked to uneven wealth distribution  

Urban inequality remains a central indicator of crime proliferation.

---

### 🎯 **Key Takeaways**
- Socioeconomic deprivation strongly correlates with higher crime levels
- Income inequality, not just average income, influences crime patterns
- Urban complexity in larger cities amplifies socioeconomic disparities
- Reducing poverty and expanding economic opportunities is essential for crime prevention strategies

---

### ✅ Policy & Research Implications
These findings reinforce the need for:

- Targeted poverty alleviation programs
- Economic empowerment and job access initiatives
- Strengthened urban social services and education
- Urban planning strategies that reduce inequality hotspots

Further research may integrate time-series crime trends, migration indicators, and policing resource distribution for deeper causal insights.

---
""")

