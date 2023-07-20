-- 1587. Bank Account Summary II

SELECT
    u.name,
    SUM(amount) as Balance    
FROM Users u
INNER JOIN Transactions t
ON u.account = t.account
GROUP BY u.account, u.name
HAVING SUM(amount) > 10000;
