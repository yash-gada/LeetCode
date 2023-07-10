-- 1158. Market Analysis I

WITH filtered as
(
SELECT DISTINCT
    u.user_id,
    u.join_date,
    CASE WHEN o.order_date LIKE '2019%' THEN o.order_id ELSE 0 END as order2019
FROM Users u
LEFT JOIN Orders o
ON u.user_id = o.buyer_id
)

SELECT 
    user_id as buyer_id,
    join_date,
    SUM(IF(order2019 != 0, 1, 0)) as orders_in_2019
FROM filtered
GROUP BY user_id
