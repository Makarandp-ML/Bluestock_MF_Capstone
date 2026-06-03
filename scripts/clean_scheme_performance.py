import pandas as pd

df = pd.read_csv(
    "data/raw/07_scheme_performance.csv"
)

print("Original Shape:", df.shape)

# Numeric columns
numeric_cols = [
    "return_1yr_pct",
    "return_3yr_pct",
    "return_5yr_pct",
    "benchmark_3yr_pct",
    "alpha",
    "beta",
    "sharpe_ratio",
    "sortino_ratio",
    "std_dev_ann_pct",
    "max_drawdown_pct"
]

for col in numeric_cols:
    df[col] = pd.to_numeric(
        df[col],
        errors="coerce"
    )

# Check nulls after conversion
print("\nNull Values:")
print(df[numeric_cols].isnull().sum())

# Expense ratio check
invalid_expense = df[
    (df["expense_ratio_pct"] < 0.1) |
    (df["expense_ratio_pct"] > 2.5)
]

print("\nInvalid Expense Ratio Rows:")
print(len(invalid_expense))

# Extreme return anomaly
anomaly_returns = df[
    (df["return_1yr_pct"] > 100) |
    (df["return_1yr_pct"] < -100)
]

print("Return Anomalies:")
print(len(anomaly_returns))

df.to_csv(
    "data/processed/07_scheme_performance_clean.csv",
    index=False
)

print("\nSaved Successfully")