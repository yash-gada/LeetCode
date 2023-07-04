-- 1251. Average Selling Price

SELECT
    p.product_id,
    ROUND(SUM(p.price * us.units)/SUM(us.units), 2) as average_price
FROM Prices p
INNER JOIN UnitsSold us
ON p.product_id = us.product_id
AND us.purchase_date BETWEEN p.start_date AND p.end_date
GROUP BY p.product_id
