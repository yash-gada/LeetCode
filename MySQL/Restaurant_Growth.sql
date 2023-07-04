-- 1321. Restaurant Growth

WITH day_sum as
(
SELECT
    visited_on,
    SUM(amount) as s
FROM Customer
GROUP BY visited_on
)

SELECT
    visited_on,
    SUM(s) OVER(ORDER BY visited_on ROWS BETWEEN 6 PRECEDING AND CURRENT ROW) as amount,
    ROUND(AVG(s) OVER(ORDER BY visited_on ROWS BETWEEN 6 PRECEDING AND CURRENT ROW), 2) as average_amount
FROM day_sum
ORDER BY visited_on 
LIMIT 6, 90239102 --random highest number
