-- 1907. Count Salary Categories

SELECT
    'Low Salary' as Category,
    COUNT(*) as accounts_count
FROM Accounts
WHERE income<20000

UNION
SELECT
    'Average Salary' as Category,
    COUNT(*) as accounts_count
FROM Accounts
WHERE income>=20000 AND income<=50000

UNION
SELECT
    'High Salary' as Category,
    COUNT(*) as accounts_count
FROM Accounts
WHERE income>50000
