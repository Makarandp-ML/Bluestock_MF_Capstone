import pandas as pd
from sqlalchemy import create_engine

engine = create_engine("sqlite:///data/db/bluestock_mf.db")

# Load processed data
nav = pd.read_csv("data/processed/nav_history_clean.csv")
txn = pd.read_csv("data/processed/investor_transactions_clean.csv")
perf = pd.read_csv("data/processed/scheme_performance_clean.csv")

# Write to SQLite
nav.to_sql("nav_history", engine, if_exists="replace", index=False)
txn.to_sql("transactions", engine, if_exists="replace", index=False)
perf.to_sql("performance", engine, if_exists="replace", index=False)

print("Data loaded into SQLite")