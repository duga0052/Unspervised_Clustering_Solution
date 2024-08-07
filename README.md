Unspervised_Clustering_Solution/

Purpose:

This project aims to segment customers based on their purchasing behavior using K-Means clustering. The dataset includes information about customers' age, annual income, and spending score. The project involves data loading, preprocessing, clustering, and visualization.

-------------

How to Run This Code:

 - Ensure you have Python installed on your system along with the required packages.
 - Place mall_customers.csv in the directory where the script is located.
 - Run the main.py script in a Python environment.

--------------

Dependencies:

The following libraries are required:

pandas: For data manipulation and analysis
numpy: For numerical operations
matplotlib: For plotting graphs
seaborn: For data visualization
scikit-learn: For machine learning algorithms and evaluation metrics
logging: For logging errors and information

-------------------

Ensure they are installed using pip:

pip install pandas numpy matplotlib seaborn scikit-learn

-------------------

Project Structure

├── data/
│   └── mall_customers.csv          # The dataset file
├── src/
│   ├── __init__.py                 # Makes src a package
│   ├── data/
│   │   ├── __init__.py             # Makes data a package
│   │   └── data_loader.py          # Module for loading data
├── feature/
│   │   ├── __init__.py             # Makes feature_engineering a package
│   │   └── build_features.py  # Module for feature engineering
│   ├── visualization/
│   │   ├── __init__.py             # Makes visualization a package
│   │   └── data_visualization.py   # Module for data visualization
│   ├── clustering/
│   │   ├── __init__.py             # Makes clustering a package
│   │   └── clustering.py           # Module for clustering operations
├── tests/
│   ├── __init__.py                 # Makes tests a package
│   ├── test_data_loader.py         # Unit tests for data_loader.py
│   ├── test_data_visualization.py  # Unit tests for data_visualization.py
│   └── test_clustering.py          # Unit tests for clustering.py
├── main.py                         # Main script to run the project
├── README.md                       # Project description and instructions
├── requirements.txt                # List of dependencies
└── .gitignore                      # Git ignore file

-------------

Detailed Steps
1. Data Loading
The dataset is loaded from a CSV file named mall_customers.csv using the load_data function from data_loader.py. This function reads the data into a pandas DataFrame and performs initial preprocessing.
2. Data Exploration
Initial Inspection: Display the first few rows of the dataset to understand its structure and contents.
Check for Missing Values: Identify any missing values in the dataset to plan for imputation.
3. Data Visualization
Pairplot: Visualize the relationships between different features using the plot_pairplot function.
Clusters: Visualize the clusters formed by the K-Means algorithm using the plot_clusters function.
Elbow Plot: Determine the optimal number of clusters using the plot_elbow function.
Silhouette Plot: Evaluate the quality of clusters using the plot_silhouette function.
4. Clustering
Train KMeans Model: Train a K-Means clustering model using the train_kmeans function.
Calculate WCSS: Calculate the Within-Cluster Sum of Squares (WCSS) for different numbers of clusters using the calculate_wcss function.
Calculate Silhouette Scores: Calculate the silhouette scores for different numbers of clusters using the calculate_silhouette function.

-------------

Conclusion
This project demonstrates a complete workflow for customer segmentation using K-Means clustering. It covers data preprocessing, clustering, and visualization. The models are evaluated using WCSS and silhouette scores to ensure robustness and reliability. The visualizations provide a comprehensive approach to understanding and interpreting the clusters formed based on customer purchasing behavior


Steps to Push code from VS code to Github.
First authenticate your githib account and integrate with VS code. Click on the source control icon and complete the setup.
1. Click terminal and open new terminal
2. git config --global user.name "Swapnilin"
3. git config --global user.email swapnilforcat@gmail.com
4. git init
5. git add .
6. git commit -m "Your commit message"