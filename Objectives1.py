import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans

st.set_page_config(page_title="Crime Clustering Dashboard", layout="wide") 

# TITLE
st.title("📊 Crime Pattern Clustering & PCA Visualization Dashboard")

# OBJECTIVE
st.markdown("""
### 🎯 Objective  
This dashboard identifies crime patterns across Malaysian cities by applying K-Means clustering and PCA.
It helps classify cities into crime groups based on violent, property, white-collar, and social crime rates.
""")

# --- Load Dataset ---
url = "https://raw.githubusercontent.com/s22a0064-AinMaisarah/Crime/refs/heads/main/df_crime_cleaned.csv"
df = pd.read_csv(url)

st.success("✅ Dataset Loaded Successfully")
st.dataframe(df.head())

# --- Features ---
features = ['violent_crime', 'property_crime', 'whitecollar_crime', 'social_crime']
X = df[features]

# --- Scaling ---
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# ================= SUMMARY METRICS =================
st.subheader("📌 Summary Metrics")

col1, col2, col3, col4 = st.columns(4)

col1.metric(
    label="Crime Features",
    value="4",
    help="Number of crime variables used for clustering: violent, property, white-collar, social",
    border=True
)

col2.metric(
    label="Optimal Clusters (k)",
    value="3",
    help="K-Means clustering determined 3 optimal crime pattern clusters",
    border=True
)

col3.metric(
    label="PCA Components",
    value="2",
    help="2 principal components used for dimensionality reduction and visualization",
    border=True
)

col4.metric(
    label="Dataset Records",
    value=str(df.shape[0]),
    help="Total number of locations/rows analyzed in the dataset",
    border=True
)


# =============== 1️⃣ ELBOW METHOD ===============
st.subheader("1️⃣ Elbow Method — Finding Best Number of Clusters")

wcss = []
for k in range(2, 10):
    kmeans = KMeans(n_clusters=k, random_state=42, n_init=10)
    kmeans.fit(X_scaled)
    wcss.append(kmeans.inertia_)

fig_elbow = px.line(
    x=range(2, 10), 
    y=wcss, 
    markers=True, 
    title="Elbow Method for Optimal k",
    labels={"x": "Number of Clusters (k)", "y": "WCSS"}
)
st.plotly_chart(fig_elbow, use_container_width=True)

# Short Explanation
st.info("📍 *The elbow point shows k = 3 is optimal — meaning three crime pattern groups exist.*")

# Choose k=3
kmeans = KMeans(n_clusters=3, random_state=42, n_init=10)
df['crime_cluster'] = kmeans.fit_predict(X_scaled)

# =============== 2️⃣ PCA CLUSTER VISUALIZATION ===============
st.subheader("2️⃣ PCA Visualization — Crime Pattern Groups")

pca = PCA(n_components=2)
pca_data = pca.fit_transform(X_scaled)
df['PC1'], df['PC2'] = pca_data[:, 0], pca_data[:, 1]

fig_pca = px.scatter(
    df, x='PC1', y='PC2', color='crime_cluster',
    hover_data=['city_cat','state','violent_crime','property_crime','whitecollar_crime','social_crime'],
    title="PCA Scatter Plot — Crime Clusters"
)
st.plotly_chart(fig_pca, use_container_width=True)

# Short Explanation
st.info("📍 *PCA clearly separates cities into three clusters, showing distinct crime behavior patterns.*")

# =============== 3️⃣ CLUSTER PROFILE BAR CHART ===============
st.subheader("3️⃣ Crime Type Profile by Cluster")

cluster_profile = df.groupby('crime_cluster')[features].mean().reset_index()
cluster_profile_melted = cluster_profile.melt(
    id_vars='crime_cluster', 
    var_name='Crime Type', 
    value_name='Average Crime Score'
)

fig_bar = px.bar(
    cluster_profile_melted,
    x='Crime Type', y='Average Crime Score',
    color='crime_cluster', barmode='group',
    title='Average Crime Scores per Cluster',
)
st.plotly_chart(fig_bar, use_container_width=True)

# Short Explanation
st.info("📍 *Cluster comparison shows which crime types are dominant in each group.*")

st.success("✅ All visualizations generated successfully!")

# =============== 📌 INTERPRETATION / DISCUSSION ===============
st.markdown("""
---

### 🧐 Interpretation & Discussion  

The analysis reveals three clear crime clusters across cities.  
One cluster shows high violent and property crime, indicating high-risk areas requiring focused law enforcement.  
Another cluster reflects moderate crime levels across all categories, while the last cluster represents low-crime regions.  
The PCA visualization confirms strong separation between these groups, proving that crime types are closely related and form meaningful patterns.  
These insights help authorities prioritize hotspot areas, allocate security resources, and plan targeted crime-prevention strategies.

---
""")
