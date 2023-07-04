-- 1934. Confirmation Rate

SELECT
    s.user_id,
    ROUND(SUM(CASE WHEN action = 'confirmed' THEN 1 ELSE 0 END)/COUNT(*), 2) as confirmation_rate
FROM Signups s
LEFT JOIN Confirmations c
ON s.user_id = c.user_id
GROUP BY s.user_id
