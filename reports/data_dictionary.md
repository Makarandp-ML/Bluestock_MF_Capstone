# Mutual Fund Analytics Data Dictionary

## 01_fund_master

| Column            | Type | Description                   |
| ----------------- | ---- | ----------------------------- |
| amfi_code         | TEXT | Unique AMFI scheme identifier |
| fund_house        | TEXT | Mutual fund company           |
| scheme_name       | TEXT | Scheme name                   |
| category          | TEXT | Equity/Debt/Hybrid            |
| sub_category      | TEXT | Large Cap, Mid Cap, Small Cap |
| expense_ratio_pct | REAL | Annual expense ratio          |
| risk_category     | TEXT | SEBI risk classification      |

## 02_nav_history

| Column    | Type | Description       |
| --------- | ---- | ----------------- |
| amfi_code | TEXT | Scheme identifier |
| date      | DATE | NAV date          |
| nav       | REAL | Net Asset Value   |

## 07_scheme_performance

| Column         | Type | Description          |
| -------------- | ---- | -------------------- |
| return_1yr_pct | REAL | One year return      |
| return_3yr_pct | REAL | Three year CAGR      |
| sharpe_ratio   | REAL | Risk-adjusted return |
| beta           | REAL | Market sensitivity   |

## 08_investor_transactions

| Column           | Type | Description            |
| ---------------- | ---- | ---------------------- |
| investor_id      | TEXT | Investor identifier    |
| transaction_date | DATE | Transaction date       |
| amount_inr       | REAL | Transaction amount     |
| transaction_type | TEXT | SIP/Lumpsum/Redemption |
| state            | TEXT | Investor state         |
| kyc_status       | TEXT | Verified/Pending       |
