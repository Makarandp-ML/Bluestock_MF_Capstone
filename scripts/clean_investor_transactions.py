import pandas as pd

df = pd.read_csv(
    "data/raw/08_investor_transactions.csv"
)

print("Original Shape:", df.shape)

# Fix date
df["transaction_date"] = pd.to_datetime(
    df["transaction_date"],
    errors="coerce"
)

# Standardize transaction types
df["transaction_type"] = (
    df["transaction_type"]
    .str.strip()
    .str.title()
)

valid_types = [
    "Sip",
    "Lumpsum",
    "Redemption"
]

invalid_txn = df[
    ~df["transaction_type"].isin(valid_types)
]

print("\nInvalid Transaction Types:")
print(len(invalid_txn))

# Validate amount
invalid_amount = df[
    df["amount_inr"] <= 0
]

print("Invalid Amount Rows:")
print(len(invalid_amount))

# Validate KYC
valid_kyc = [
    "Verified",
    "Pending"
]

invalid_kyc = df[
    ~df["kyc_status"].isin(valid_kyc)
]

print("Invalid KYC Rows:")
print(len(invalid_kyc))

df.to_csv(
    "data/processed/08_investor_transactions_clean.csv",
    index=False
)

print("\nSaved Successfully")