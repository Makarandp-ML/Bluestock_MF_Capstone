print("Program Started")

import requests
import pandas as pd

url = "https://api.mfapi.in/mf/125497"

print("Sending request...")

response = requests.get(url, timeout=10)

print("Status Code:", response.status_code)

if response.status_code == 200:

    data = response.json()

    print("API Connected Successfully")

    print("Scheme Name:")
    print(data["meta"]["scheme_name"])

    nav_df = pd.DataFrame(data["data"])

    print("Rows:", len(nav_df))

    nav_df.to_csv(
        "data/raw/HDFC_Top100_NAV.csv",
        index=False
    )

    print("CSV Saved Successfully!")

else:
    print("API request failed")