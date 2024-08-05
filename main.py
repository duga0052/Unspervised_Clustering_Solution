import os
import logging
import pandas as pd
import warnings
from src.data.data_loader import load_data
from src.visualization.visualization import plot_pairplot, plot_clusters, plot_elbow, plot_silhouette
from src.model.clustering import train_kmeans, calculate_wcss, calculate_silhouette

# Set the environment variable to avoid memory leak issue with KMeans on Windows
os.environ['OMP_NUM_THREADS'] = '1'

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Suppress specific sklearn warnings
warnings.filterwarnings("ignore", message="KMeans is known to have a memory leak on Windows with MKL")

def main():
    try:
        # Load data
        logging.info("Loading data...")
        df = load_data('mall_customers.csv')  # Update the path here if necessary
        
        # Display the first few rows and dataframe information
        logging.info("Displaying the first few rows of the dataframe:")
        print(df.head())
        
        logging.info("Displaying dataframe information:")
        print(df.info())

        # Plot pairplot
        logging.info("Plotting pairplot...")
        plot_pairplot(df, ['Age', 'Annual_Income', 'Spending_Score'])

        # Train KMeans model
        logging.info("Training KMeans model...")
        kmodel = train_kmeans(df, ['Annual_Income', 'Spending_Score'], 5)

        # Add cluster labels to dataframe
        df['Cluster'] = kmodel.labels_

        # Plot clusters
        logging.info("Plotting clusters...")
        plot_clusters(df, 'Annual_Income', 'Spending_Score', 'Cluster')

        # Calculate WCSS and plot elbow plot
        logging.info("Calculating WCSS and plotting elbow plot...")
        wss_df = calculate_wcss(df, ['Annual_Income', 'Spending_Score'], range(3, 9))
        logging.info("WCSS scores:\n%s", wss_df)
        plot_elbow(wss_df)

        # Calculate silhouette scores and plot silhouette plot
        logging.info("Calculating silhouette scores and plotting silhouette plot...")
        silhouette_df = calculate_silhouette(df, ['Annual_Income', 'Spending_Score'], range(3, 9))
        logging.info("Silhouette scores:\n%s", silhouette_df)
        plot_silhouette(silhouette_df)

    except FileNotFoundError as e:
        logging.error("File not found: %s", e)
    except pd.errors.EmptyDataError as e:
        logging.error("No data: %s", e)
    except pd.errors.ParserError as e:
        logging.error("Parsing error: %s", e)
    except Exception as e:
        logging.error("An unexpected error occurred: %s", e)

if __name__ == "__main__":
    main()