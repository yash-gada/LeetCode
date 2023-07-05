-- 1084. Sales Analysis III

SELECT DISTINCT
    s.product_id,
    p.product_name
FROM Sales s
INNER JOIN Product p
ON s.product_id = p.product_id
WHERE s.product_id NOT IN (SELECT DISTINCT product_id FROM Sales WHERE sale_date>'2019-03-31' OR sale_date<'2019-01-01') 
AND s.sale_date BETWEEN '2019-01-01' AND '2019-03-31'; -- This condition is to eliminate products that have never been sold
