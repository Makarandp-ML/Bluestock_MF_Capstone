import pandas as pd
import sqlite3

conn = sqlite3.connect("bluestock_mf.db")

tables = [
    "fund_master",
    "nav_history",
    "scheme_performance",
    "investor_transactions"
]

for table in tables:

    count = pd.read_sql(
        f"SELECT COUNT(*) cnt FROM {table}",
        conn
    )

    print(table)
    print(count)

conn.close()