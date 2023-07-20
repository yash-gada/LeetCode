-- 183. Customers Who Never Order

/*
-- Alternate Solution

SELECT
    c.name as Customers
FROM Customers c
LEFT JOIN Orders o
ON c.id = o.customerId
WHERE o.id IS NULL;
*/

SELECT
    name as Customers
FROM Customers
WHERE id NOT IN (SELECT customerId FROM Orders)
