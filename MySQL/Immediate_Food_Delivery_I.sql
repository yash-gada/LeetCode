-- 1173. Immediate Food Delivery I

/*
WITH imme as
(
SELECT
    COUNT(delivery_id) as cnt_del 
FROM Delivery
WHERE order_date = customer_pref_delivery_date
)
SELECT
    ROUND((i.cnt_del*100)/COUNT(delivery_id), 2) as immediate_percentage
FROM imme i, Delivery d
*/
SELECT 
    ROUND((SUM(CASE WHEN order_date = customer_pref_delivery_date THEN 1 ELSE 0 end)/count(*)) *100, 2) as immediate_percentage 
FROM Delivery
