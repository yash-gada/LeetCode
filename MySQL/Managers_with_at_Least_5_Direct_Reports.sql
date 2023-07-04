-- 570. Managers with at Least 5 Direct Reports

SELECT
    m.name
FROM Employee m
INNER JOIN Employee e
ON e.managerId = m.id
GROUP BY m.id, m.name
HAVING COUNT(e.managerId) >= 5;
