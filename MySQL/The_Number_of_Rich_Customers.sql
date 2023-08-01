-- 2082. The Number of Rich Customers

/*
SELECT
    COUNT(DISTINCT CASE 
            WHEN amount>500 THEN customer_id 
        END) as rich_count
FROM Store
*/

SELECT
  COUNT(DISTINCT customer_id) as rich_count
FROM Store
WHERE amount>500
