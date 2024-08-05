Unspervised_Clustering_Solution/
├── data/
│   └── mall_customers.csv          # The dataset file
├── src/
│   ├── __init__.py                 # Makes src a package
│   ├── data/
│   │   ├── __init__.py             # Makes data a package
│   │   └── data_loader.py          # Module for loading data
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

Steps to Push code from VS code to Github.
First authenticate your githib account and integrate with VS code. Click on the source control icon and complete the setup.
1. Click terminal and open new terminal
2. git config --global user.name "Swapnilin"
3. git config --global user.email swapnilforcat@gmail.com
4. git init
5. git add .
6. git commit -m "Your commit message"