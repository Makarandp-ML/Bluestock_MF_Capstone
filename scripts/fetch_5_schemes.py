import requests
import pandas as pd
import os

os.makedirs("data/raw/nav_files", exist_ok=True)

funds = {
    "SBI_Bluechip": 119551,
    "ICICI_Bluechip": 120503,
    "Nippon_Large_Cap": 118632,
    "Axis_Bluechip": 119092,
    "Kotak_Bluechip": 120841
}

for fund_name, code in funds.items():

    url = f"https://api.mfapi.in/mf/{code}"

    response = requests.get(url)

    if response.status_code == 200:

        data = response.json()

        nav_df = pd.DataFrame(data["data"])

        filename = f"data/raw/nav_files/{fund_name}.csv"

        nav_df.to_csv(filename, index=False)

        print(f"Saved: {fund_name}")

    else:
        print(f"Failed: {fund_name}")