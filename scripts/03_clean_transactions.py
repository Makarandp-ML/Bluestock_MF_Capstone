import pandas as pd

txn = pd.read_csv("data/raw/investor_transactions.csv")

# 1. Date format fix
txn['date'] = pd.to_datetime(txn['date'], errors='coerce')

# 2. Standardize transaction types
txn['transaction_type'] = txn['transaction_type'].str.upper().str.strip()

valid_types = ['SIP', 'LUMPSUM', 'REDEMPTION']
txn = txn[txn['transaction_type'].isin(valid_types)]

# 3. Amount validation
txn = txn[txn['amount'] > 0]

# 4. KYC validation
txn['kyc_status'] = txn['kyc_status'].str.upper().str.strip()
txn = txn[txn['kyc_status'].isin(['VERIFIED', 'PENDING', 'REJECTED'])]

# Save
txn.to_csv("data/processed/investor_transactions_clean.csv", index=False)

print("Transactions cleaned done")