-- 180. Consecutive Numbers

SELECT DISTINCT
    l1.num as ConsecutiveNums
FROM Logs l1
INNER JOIN Logs l2
ON l1.num = l2.num
INNER JOIN Logs l3
ON l1.num = l3.num
WHERE l1.id+1 = l2.id AND l2.id+1 = l3.id
