-- 1164. Product Price at a Given Date

SELECT DISTINCT
    p1.product_id,
    IFNULL(t.new_price, 10) as price
FROM Products p1
LEFT JOIN (
    SELECT
        *,
        RANK() OVER(PARTITION BY product_id ORDER BY change_date DESC) as rnk
    FROM Products
    WHERE change_date<='2019-08-16'
) t
ON p1.product_id = t.product_id AND t.rnk = 1
