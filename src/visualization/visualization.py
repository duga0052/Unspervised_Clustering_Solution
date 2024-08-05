# data_visualization.py
import seaborn as sns
import matplotlib.pyplot as plt

def plot_pairplot(df, columns):
    sns.pairplot(df[columns])
    plt.show()

def plot_clusters(df, x_col, y_col, cluster_col):
    sns.scatterplot(x=x_col, y=y_col, data=df, hue=cluster_col, palette='colorblind')
    plt.show()

def plot_elbow(wss_df):
    wss_df.plot(x='cluster', y='WSS_Score')
    plt.xlabel('No. of clusters')
    plt.ylabel('WSS Score')
    plt.title('Elbow Plot')
    plt.show()

def plot_silhouette(silhouette_df):
    silhouette_df.plot(x='cluster', y='Silhouette_Score')
    plt.xlabel('No. of clusters')
    plt.ylabel('Silhouette Score')
    plt.title('Silhouette Plot')
    plt.show()