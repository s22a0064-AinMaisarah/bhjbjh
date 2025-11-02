import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# ===================== PAGE CONFIG =====================
st.set_page_config(page_title="Male Population, Age and Education Level Influence Crime Patterns", layout="wide")

# ===================== PAGE HEADER =====================
st.title("🧠 Objective 3 — Male Population, Age and Education Level Influence Crime Patterns")

st.markdown("""
### 🎯 Objective  
To critically evaluate how **demographic indicators**, specifically **gender composition, age structure, and educational attainment**,  
shape the distribution of various crime categories within urban settings.  

This investigation aims to uncover **socio-structural drivers of crime**, providing a foundation for  
evidence-based urban policy and targeted community safety interventions.  
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

# ---------------------------------------------------------
# 🧠 Final Insight & Interpretation
# ---------------------------------------------------------

st.subheader("🧠 Final Insight & Interpretation")

st.markdown("""
Demographics play a fundamental role in shaping crime behavior in cities.  
Findings indicate that male-dominant, youthful, and lower-education populations  
are consistently associated with higher urban crime exposure, particularly violent and property crimes.  

Conversely, regions with greater higher-education attainment show reduced physical crime rates but exhibit  
greater white-collar crime concentration, aligning with socio-economic opportunity structures.
""")
# ---------------------------------------------------------
# 🎯 KEY TAKEAWAYS
# ---------------------------------------------------------
st.subheader("🎯 Key Takeaways")

st.markdown("""
- 🔹 Higher male population ratio → Higher violent & property crime
- 🔹 Younger demographic clusters → Elevated social & property offenses
- 🔹 Higher education → Decrease in violent crime; increase in white-collar activity
- 🔹 Education emerges as a protective socio-economic factor
- 🔹 Crime is multidimensional, influenced by **population structure + opportunity + economic pressure
""")

# ---------------------------------------------------------
# ✅ POLICY IMPLICATIONS
# ---------------------------------------------------------

st.subheader("✅ Policy & Research Implications")

st.markdown("""
Urban Policy Recommendations
- 📍 Prioritize youth employment and community programs in younger-populated districts  
- 📍 Expand education & skill-development pipelines to reduce physical crime occurrence  
- 📍 Strengthen cyber-security & financial fraud monitoring in highly educated areas  
- 📍 Implement gender-focused community safety initiatives in male-skewed regions  

Research Recommendations
- 🔬 Further studies should integrate income inequality, migration patterns, and policing levels
- 🧪 Build predictive models to forecast crime risk by demographic shifts
- 🌍 Apply this model to Asian & European datasets to validate cross-regional patterns
""")

st.success("📎 This demographic-crime analysis strengthens the urban planning, criminology, and public-policy nexus through data-driven insight.")
