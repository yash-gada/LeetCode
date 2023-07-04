-- 1070. Product Sales Analysis III

SELECT
    product_id,
    year as first_year,
    quantity,
    price
FROM (
    SELECT
        *,
        RANK() OVER(PARTITION BY product_id ORDER BY year) as rnum
    FROM Sales
) t
WHERE rnum = 1
