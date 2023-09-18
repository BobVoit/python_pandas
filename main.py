from sklearn.datasets import make_blobs
import matplotlib.pyplot as plt
import pandas as pd
from sqlalchemy import create_engine


# features, target = make_blobs(
#     n_samples=100,
#     n_features=2,
#     centers=3,
#     cluster_std=0.5,
#     shuffle=True,
#     random_state=1
# )

# url = "https://raw.githubusercontent.com/chrisalbon/simulated_datasets/master/data.csv"
# dataframe = pd.read_csv(url)

# url = "https://tinyurl.com/simulated-excel"
# dataframe = pd.read_excel(url, sheet_name=0, header=0)

# url = "https://tinyurl.com/simulated-json"
# dataframe = pd.read_json(url, orient="columns")

database_connection = create_engine('sqlite:///sample.db')

dataframe = pd.read_sql_query("SELECT * FROM data", database_connection)

print(dataframe.head(2))