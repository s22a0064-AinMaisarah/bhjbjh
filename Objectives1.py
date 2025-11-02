import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans

st.set_page_config(page_title="Crime Clustering Dashboard", layout="wide")
st.title("Objective 1 — Distribution and Correlation: Crime Clustering Analysis")

# --- Load Dataset ---
url = "https://raw.githubusercontent.com/s22a0064-AinMaisarah/Crime/refs/heads/main/df_crime_cleaned.csv"
df = pd.read_csv(url)

st.success("✅ Dataset Loaded Successfully")
st.dataframe(df.head())

# --- Select Features ---
features = ['violent_crime', 'property_crime', 'whitecollar_crime', 'social_crime']
X = df[features]

# --- Scaling ---
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# =============== 1️⃣ ELBOW METHOD ===============
st.subheader("1️⃣ Elbow Method to Find Optimal k")

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

# Choose k=3
kmeans = KMeans(n_clusters=3, random_state=42, n_init=10)
df['crime_cluster'] = kmeans.fit_predict(X_scaled)

# =============== 2️⃣ PCA CLUSTER VISUALIZATION ===============
st.subheader("2️⃣ PCA Visualization of Crime Clusters")

pca = PCA(n_components=2)
pca_data = pca.fit_transform(X_scaled)
df['PC1'], df['PC2'] = pca_data[:, 0], pca_data[:, 1]

fig_pca = px.scatter(
    df, 
    x='PC1', y='PC2',
    color='crime_cluster',
    hover_data=['violent_crime','property_crime','whitecollar_crime','social_crime','city_cat','state'],
    title="Crime Pattern Clusters (PCA)"
)
st.plotly_chart(fig_pca, use_container_width=True)

# =============== 3️⃣ BAR CHART — Cluster Crime Profiles ===============
st.subheader("3️⃣ Cluster Profile by Average Crime Type")

cluster_profile = df.groupby('crime_cluster')[features].mean().reset_index()
cluster_profile_melted = cluster_profile.melt(
    id_vars='crime_cluster', 
    var_name='Crime Type', 
    value_name='Average Crime Score'
)

fig_bar = px.bar(
    cluster_profile_melted,
    x='Crime Type',
    y='Average Crime Score',
    color='crime_cluster',
    barmode='group',
    title='Average Crime Scores per Cluster',
    hover_data=['crime_cluster', 'Crime Type', 'Average Crime Score']
)
st.plotly_chart(fig_bar, use_container_width=True)

st.success("✅ All visualizations generated: Elbow, PCA, Bar Chart")
