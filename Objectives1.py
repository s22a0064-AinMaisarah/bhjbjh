import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans
import plotly.io as pio

st.set_page_config(page_title="Objective 1 — Distribution and Correlation", layout="wide")

st.title("Objective 1 — Distribution and Correlation")

url = "https://raw.githubusercontent.com/s22a0064-AinMaisarah/Crime/refs/heads/main/df_crime_cleaned.csv"
df = pd.read_csv(url)

st.write("✅ File loaded successfully!")
st.dataframe(df.head())

features = ['violent_crime', 'property_crime', 'whitecollar_crime', 'social_crime']
X = df[features]

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

wcss = []
for k in range(2, 10):
    kmeans = KMeans(n_clusters=k, random_state=42, n_init=10)
    kmeans.fit(X_scaled)
    wcss.append(kmeans.inertia_)

fig_elbow = px.line(x=range(2, 10), y=wcss, markers=True, title="Elbow Method for Optimal k")
st.plotly_chart(fig_elbow)

kmeans = KMeans(n_clusters=3, random_state=42, n_init=10)
df['crime_cluster'] = kmeans.fit_predict(X_scaled)

pca = PCA(n_components=2)
pca_data = pca.fit_transform(X_scaled)
df['PC1'], df['PC2'] = pca_data[:, 0], pca_data[:, 1]

fig_clusters = px.scatter(
    df, x='PC1', y='PC2', color='crime_cluster',
    hover_data=['violent_crime', 'property_crime', 'whitecollar_crime', 'social_crime', 'city_cat', 'state'],
    title='Crime Pattern Clusters (PCA)'
)
st.plotly_chart(fig_clusters)
