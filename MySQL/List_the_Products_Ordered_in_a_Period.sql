-- 1327. List the Products Ordered in a Period

WITH t as
(
SELECT
    *,
    SUM(unit) as su
FROM Orders
WHERE order_date BETWEEN '2020-02-01' AND '2020-02-29'
GROUP BY product_id
)

SELECT
    p.product_name,
    su as unit
FROM t
INNER JOIN Products p
ON t.product_id = p.product_id
WHERE su>=100
