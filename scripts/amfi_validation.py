import pandas as pd

fund_master = pd.read_csv("data/raw/01_fund_master.csv")
nav_history = pd.read_csv("data/raw/02_nav_history.csv")

# Remove null values
master_codes = set(fund_master["amfi_code"].dropna())
nav_codes = set(nav_history["amfi_code"].dropna())

missing_codes = master_codes - nav_codes

print("Missing Codes:")
print(missing_codes)

print("\nTotal Missing:")
print(len(missing_codes))