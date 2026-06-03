import pandas as pd
from sqlalchemy import create_engine

engine = create_engine(
    "sqlite:///bluestock_mf.db"
)

files = {
    "fund_master":
    "data/raw/01_fund_master.csv",

    "nav_history":
    "data/processed/02_nav_history_clean.csv",

    "scheme_performance":
    "data/processed/07_scheme_performance_clean.csv",

    "investor_transactions":
    "data/processed/08_investor_transactions_clean.csv",

    "aum_by_fund_house":
    "data/raw/03_aum_by_fund_house.csv",

    "monthly_sip_inflows":
    "data/raw/04_monthly_sip_inflows.csv",

    "category_inflows":
    "data/raw/05_category_inflows.csv",

    "industry_folio_count":
    "data/raw/06_industry_folio_count.csv",

    "portfolio_holdings":
    "data/raw/09_portfolio_holdings.csv",

    "benchmark_indices":
    "data/raw/10_benchmark_indices.csv"
}

for table, file in files.items():

    df = pd.read_csv(file)

    df.to_sql(
        table,
        engine,
        if_exists="replace",
        index=False
    )

    print(f"Loaded {table}")