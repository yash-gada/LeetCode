-- 1174. Immediate Food Delivery II

WITH totals as
(
SELECT
    customer_id,
    MIN(order_date) OVER(PARTITION BY customer_id ORDER BY customer_id, order_date) as min_d,
    customer_pref_delivery_date as pref,
    ROW_NUMBER() OVER(PARTITION BY customer_id) as tf
FROM Delivery
ORDER BY customer_id
)

SELECT
    ROUND(COUNT(CASE WHEN min_d = pref THEN 1 END)*100 / SUM(CASE WHEN tf=1 THEN 1 ELSE 0 END), 2) as immediate_percentage
FROM totals

/*
-- SIMPLER SOLUTION

select round(avg(order_date = customer_pref_delivery_date)*100,2) as immediate_percentage
from delivery 
where (customer_id, order_date) in (
select customer_id, min(order_date) as order_date
from delivery 
group by customer_id)
*/
