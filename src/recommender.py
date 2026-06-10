import pandas as pd

fund = pd.read_csv("data/raw/01_fund_master.csv")
score = pd.read_csv("reports/fund_scorecard.csv")

reco = fund.merge(score, on="amfi_code")

def recommend_funds(risk_level):
    temp = reco[reco["risk_category"] == risk_level]

    return (
        temp.sort_values("sharpe", ascending=False)[
            ["scheme_name", "fund_house", "risk_category", "sharpe"]
        ].head(3)
    )

print(recommend_funds("Moderate"))