# clustering.py
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
import pandas as pd

def train_kmeans(df, features, n_clusters):
    kmodel = KMeans(n_clusters=n_clusters).fit(df[features])
    return kmodel

def calculate_wcss(df, features, k_range):
    WCSS = []
    K = []
    for i in k_range:
        kmodel = KMeans(n_clusters=i).fit(df[features])
        WCSS.append(kmodel.inertia_)
        K.append(i)
    return pd.DataFrame({'cluster': K, 'WSS_Score': WCSS})

def calculate_silhouette(df, features, k_range):
    ss = []
    K = []
    for i in k_range:
        kmodel = KMeans(n_clusters=i).fit(df[features])
        ypred = kmodel.labels_
        sil_score = silhouette_score(df[features], ypred)
        K.append(i)
        ss.append(sil_score)
    return pd.DataFrame({'cluster': K, 'Silhouette_Score': ss})