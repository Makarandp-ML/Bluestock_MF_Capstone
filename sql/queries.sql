-- 1. Top 5 Funds by AUM
SELECT *
FROM aum_by_fund_house
ORDER BY aum_lakh_crore DESC
LIMIT 5;

-- 2. Average NAV by Fund
SELECT amfi_code,
AVG(nav) avg_nav
FROM nav_history
GROUP BY amfi_code;

-- 3. Monthly Average NAV
SELECT substr(date,1,7) month,
AVG(nav)
FROM nav_history
GROUP BY month;

-- 4. Transactions by State
SELECT state,
COUNT(*) total_transactions
FROM investor_transactions
GROUP BY state
ORDER BY total_transactions DESC;

-- 5. Expense Ratio below 1%
SELECT scheme_name,
expense_ratio_pct
FROM fund_master
WHERE expense_ratio_pct < 1;

-- 6. Total Redemption Amount
SELECT SUM(amount_inr)
FROM investor_transactions
WHERE transaction_type='Redemption';

-- 7. Category Wise Fund Count
SELECT category,
COUNT(*)
FROM fund_master
GROUP BY category;

-- 8. Top Sharpe Ratio Funds
SELECT amfi_code,
sharpe_ratio
FROM scheme_performance
ORDER BY sharpe_ratio DESC
LIMIT 5;

-- 9. Average Return by Category
SELECT fm.category,
AVG(sp.return_3yr_pct)
FROM fund_master fm
JOIN scheme_performance sp
ON fm.amfi_code=sp.amfi_code
GROUP BY fm.category;

-- 10. SIP Inflow Trend
SELECT month,
sip_inflow_crore
FROM monthly_sip_inflows
ORDER BY month;