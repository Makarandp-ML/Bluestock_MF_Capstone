import pandas as pd
import os

folder = "data/raw"

print("=== DATA INGESTION STARTED ===")

for file in os.listdir(folder):

    if file.endswith(".csv"):

        filepath = os.path.join(folder, file)

        print("\n" + "="*50)
        print("FILE:", file)

        df = pd.read_csv(filepath)

        print("Shape:", df.shape)

        print("\nColumns:")
        print(df.columns.tolist())

        print("\nData Types:")
        print(df.dtypes)

        print("\nFirst 5 Rows:")
        print(df.head())