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
    st.title("📊 Crime Analytics Dashboard")
    
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
Use **K-Means clustering** to group cities based on crime behavior patterns 
(violent, property, white-collar, social).  
This helps detect crime similarities, identify high-risk zones, and support data-driven prevention strategies.
""")

# ---------------------------------------------------------
# LOAD DATA
# ---------------------------------------------------------
url = "https://raw.githubusercontent.com/s22a0064-AinMaisarah/Crime/refs/heads/main/df_crime_cleaned.csv"
df = pd.read_csv(url)

st.success("✅ Dataset Loaded Successfully")

# Dataset Info
with st.expander("📂 About This Dataset"):
    st.write("""
This dataset, originally titled **"Uber and Urban Crime"** and published on **12 Oct 2019** by *Bryan Weber (Mendeley)*,
focuses on urban crime behavior.  
Although Uber is mentioned, the primary purpose here is to analyze **urban crime patterns** and cluster similar crime regions.
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
# INSIGHTS
# ---------------------------------------------------------
st.markdown("""
---
### 📌 Key Insights

| Crime Cluster | Description |
|---|---|
| **Cluster 0** | High crime region — high violent & property crime |
| **Cluster 1** | Medium crime distribution across all types |
| **Cluster 2** | Low-crime region — safe zone |

🛑 Areas with high violent/property crime may require **extra policing & surveillance**  
✅ Low-crime areas show **stable urban safety behavior**

---
""")
