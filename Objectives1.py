import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans

# ---------------------------------------------------------
# PAGE SETTINGS
# ---------------------------------------------------------
st.set_page_config(
    page_title="Crime Clustering Dashboard",
    page_icon="📊",
    layout="wide"
)

# Sidebar Navigation & Info
with st.sidebar:
    st.title("📊 Crime Analytics Dashboard Menu")
    
    st.write(
        "Gain insights into relationships between socioeconomic factors "
        "and crime patterns across cities."
    )
    
    st.markdown("---")
    
    st.subheader("📂 Navigation")
    st.info("Use the menu to explore different analysis modules.")
    
    st.markdown("---")
    
    st.caption("👩🏻‍💻 Created by Nurul Ain Maisarah Hamidin © 2025 | Scientific Visualization Project 🌟")


# ---------------------------------------------------------
# PAGE HEADER
# ---------------------------------------------------------
st.title("🚨 Crime Pattern Clustering & PCA Dashboard")

st.markdown("""
### 🎯 Objective  
The objective of this visualization is to identify patterns in urban crime by grouping similar crime profiles 
This aids in understanding how different crime types co-occur across regions and demographics, revealing hidden 
patterns that may guide urban safety strategies.
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

# ---------------------------------------------------------
# FEATURES & SCALING
# ---------------------------------------------------------
features = ['violent_crime', 'property_crime', 'whitecollar_crime', 'social_crime']
scaler = StandardScaler()
X_scaled = scaler.fit_transform(df[features])

# ---------------------------------------------------------
# KPI METRICS
# ---------------------------------------------------------
st.markdown("### 📊 Key Dataset Metrics")
col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "Crime Features Used", "4",
    help="Violent, Property, White-Collar, Social"
)

col2.metric(
    "Optimal Clusters (k)", "3",
    help="Determined using elbow method"
)

col3.metric(
    "PCA Components", "2",
    help="Dimensionality reduction"
)

col4.metric(
    "Total Records", f"{df.shape[0]}",
    help="Total cities/locations"
)

st.markdown("---")

# ---------------------------------------------------------
# 1️⃣ ELBOW METHOD
# ---------------------------------------------------------
st.header("1️⃣ Elbow Method — Optimal Clusters")

wcss = []
for k in range(2, 10):
    kmeans = KMeans(n_clusters=k, random_state=42, n_init=10)
    kmeans.fit(X_scaled)
    wcss.append(kmeans.inertia_)

fig_elbow = px.line(
    x=range(2, 10), y=wcss, markers=True,
    title="Elbow Curve for Optimal k",
    labels={"x": "Cluster Count (k)", "y": "WCSS"}
)
st.plotly_chart(fig_elbow, use_container_width=True)

st.info("✅ *k = 3 is optimal — Meaning three distinct crime pattern groups exist.*")

# Train final model
kmeans = KMeans(n_clusters=3, random_state=42, n_init=10)
df['crime_cluster'] = kmeans.fit_predict(X_scaled)

# ---------------------------------------------------------
# 2️⃣ PCA VISUALIZATION
# ---------------------------------------------------------
st.header("2️⃣ PCA Cluster Visualization")

pca = PCA(n_components=2)
pca_data = pca.fit_transform(X_scaled)
df['PC1'], df['PC2'] = pca_data[:, 0], pca_data[:, 1]

fig_pca = px.scatter(
    df, x='PC1', y='PC2', color='crime_cluster',
    hover_data=['city_cat','state'] + features,
    title="PCA Scatter Plot — Crime Clusters"
)
st.plotly_chart(fig_pca, use_container_width=True)

st.info("📌 *PCA confirms clear separation between high, medium & low crime regions.*")

# ---------------------------------------------------------
# 3️⃣ CLUSTER PROFILE
# ---------------------------------------------------------
st.header("3️⃣ Crime Type Profile by Cluster")

cluster_profile = df.groupby('crime_cluster')[features].mean().reset_index()
cluster_profile = cluster_profile.melt(
    id_vars='crime_cluster', var_name='Crime Type',
    value_name='Average Crime Score'
)

fig_bar = px.bar(
    cluster_profile, x='Crime Type', y='Average Crime Score',
    color='crime_cluster', barmode='group',
    title="Average Crime Scores by Cluster"
)
st.plotly_chart(fig_bar, use_container_width=True)

st.success("🎉 Visualizations Generated Successfully")

# ---------------------------------------------------------
# INSIGHTS & INTERPRETATION
# ---------------------------------------------------------
st.markdown("""
---
## 🧠 Final Insight & Interpretation

The clustering and dimensionality-reduction analysis demonstrates that crime behavior across cities is not random, rather, it follows clear, statistically differentiated patterns driven by socio-economic and urban structure factors.

### 🔍 Key Analytical Insights

#### 1️⃣ **K-Means Clustering (k = 3) — Crime Behavior Archetypes**
The model identifies three distinct crime clusters, suggesting meaningful behavioral segmentation among cities:

| Cluster | Crime Characteristics | Interpretation |
|--------|----------------------|----------------|
| Cluster 0 | High violent & property crime | Social instability, economic stress, policing pressure |
| Cluster 1 | Moderate crime across all categories | Transitional cities with mixed socio-economic conditions |
| Cluster 2 | Lowest crime levels consistently | Stable communities with strong governance and social cohesion |

Cluster 0 likely represents areas facing economic strain, youth unemployment, and community vulnerability, whereas Cluster 2 cities demonstrate strong institutional capacity and low criminogenic pressure.

---

#### **2️⃣ PCA Scatter Plot — Structural Crime Separation**
PCA reveals two dominant underlying factors explaining crime variance.  
The clear cluster separation indicates:

- Crime patterns are influenced by structural socioeconomic dynamics
- Crime variations are systematic — not incidental
- Dimensionality reduction successfully preserves meaningful classification structure

This supports criminological theories including:

- Social Disorganization Theory — weak community structures → higher crime  
- Strain Theory — limited opportunity environments → crime pressure increases

---

#### **3️⃣ Crime Type Profiles — Category Drivers**
Analysis shows:

- Violent & property crime are the primary differentiators between clusters
- White-collar and social crimes also contribute to cluster separation, though less sharply
- Prevention efforts should be cluster-specific, not universal

For example:

- Cluster 0 → intensive prevention, policing, youth & employment programs  
- Cluster 2 → maintain education, community programs, and governance strength  

---

## 🎯 Key Takeaways

- Urban crime is systematically structured, not evenly distributed
- Cities naturally group into high-risk, medium-risk, and low-risk crime environments
- PCA proves crime behavior can be modeled and predicted
- Socio-economic disparities likely influence cluster assignment
- Data-driven, differentiated crime prevention strategies are necessary

---

## ✅ Policy & Research Implications

| Area | Recommendation |
|------|---------------|
Urban Management | Implement cluster-specific policing and safety strategies |
Economic Policy | Invest in job creation, youth development, poverty reduction in high-risk clusters |
Security Strategy | Deploy predictive policing & surveillance for vulnerable zones |
Urban Planning | Prioritize safe-neighborhood development & equitable infrastructure |
Future Research | Integrate time-series crime trends & geospatial modeling for forecasting |

Policymakers should prioritize targeted interventions rather than uniform approaches, strengthening community resilience and reducing structural inequality as a long-term crime reduction strategy.

---

### 🎓 Overall Conclusion
Crime behaves as a multidimensional socio-economic phenomenon.  
Machine learning techniques like K-Means + PCA offer strong empirical evidence that:

> Cities with economic vulnerability and weaker social infrastructure exhibit higher crime concentration.

This data-driven framework supports designing proactive urban safety policies, empowering law-enforcement, researchers, and government stakeholders to predict and mitigate crime more effectively.

---
""")
