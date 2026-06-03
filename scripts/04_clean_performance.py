import pandas as pd

perf = pd.read_csv("data/raw/scheme_performance.csv")

# Convert numeric columns
num_cols = ['return_1yr', 'return_3yr', 'expense_ratio']

for col in num_cols:
    perf[col] = pd.to_numeric(perf[col], errors='coerce')

# Drop invalid rows
perf = perf.dropna(subset=num_cols)

# Expense ratio validation (0.1% to 2.5%)
perf = perf[(perf['expense_ratio'] >= 0.1) & (perf['expense_ratio'] <= 2.5)]

# Flag anomalies (optional)
perf['return_flag'] = perf['return_1yr'].apply(lambda x: 'HIGH' if x > 30 else 'NORMAL')

perf.to_csv("data/processed/scheme_performance_clean.csv", index=False)

print("Performance cleaned done")