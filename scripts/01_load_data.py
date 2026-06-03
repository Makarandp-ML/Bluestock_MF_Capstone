import pandas as pd

nav = pd.read_csv("data/raw/nav_history.csv")
txn = pd.read_csv("data/raw/investor_transactions.csv")
perf = pd.read_csv("data/raw/scheme_performance.csv")

print(nav.head())
print(txn.head())
print(perf.head())