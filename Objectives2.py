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

# ---------------------------------------------------------
# LOAD DATA
# ---------------------------------------------------------
url = "https://raw.githubusercontent.com/s22a0064-AinMaisarah/Crime/refs/heads/main/df_crime_cleaned.csv"
df = pd.read_csv(url)

st.success("✅ Dataset Loaded Successfully")

# ===================== DATASET INFORMATION =====================
with st.expander("📂 About This Dataset"):
    st.write("""
This dataset, originally titled **"Uber and Urban Crime"**, was published on  
**12 October 2019** by *Bryan Weber* on **Mendeley Data**.  

Although associated with mobility (Uber) in its original context, the primary focus here is to examine  
**urban crime patterns** and evaluate how crime types vary across different demographic environments.

### 🧾 Crime Classification Framework

For this study, crime indicators have been grouped into four structured categories:

#### 1) **Violent Crimes**
Crimes involving force or threat of force:
- homicide  
- kidnapping  
- sex_forcible  
- robbery  
- assault  
- weapon_violations  
- human_traffic  

#### 2) **Property Crimes**
Crimes involving theft, damage, or unlawful property access:
- burglary_bne  
- larceny_theft  
- motor_vehicle_theft  
- arson  
- stolen_property  
- destruction_property  

#### 3) **White-Collar / Financial Crimes**
Non-violent, financially motivated offenses:
- counterfit_forge  
- fraud  
- embezzelment  
- extortion_blackmail  

#### 4) **Moral / Social Offenses**
Crimes involving moral, social, or public-order violations:
- drug_offenses  
- sex_nonforcible  
- porn  
- prostitution  
- gambling  

---
    """)


st.subheader("🧾 Dataset Preview")
st.dataframe(df.head(), use_container_width=True)

# ====================== SUMMARY METRICS ======================
st.markdown("### 📊 Key Dataset Summary")

# ====================== SUMMARY METRICS ======================
st.markdown("### 📊 Key Crime–Socioeconomic Overview")

col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "Socioeconomic Factors",
    "2",
    help="Income level and poverty rate used as key predictors",
    border=True
)

col2.metric(
    "Crime Indicator",
    "1",
    help="Total offense count as the aggregate crime intensity measure",
    border=True
)

col3.metric(
    "City Categories",
    "2",
    help="Group I (Large urban cities) vs Group II (Smaller/medium cities)",
    border=True
)

col4.metric(
    "Total Observations",
    str(df.shape[0]),
    help="Number of city-level data points analyzed",
    border=True
)



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

