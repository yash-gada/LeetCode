-- 176. Second Highest Salary

WITH ranks as
(
SELECT
    *,
    DENSE_RANK() OVER(ORDER BY salary DESC) as rnk,
    COUNT(*) OVER() as cnt
FROM Employee
)

SELECT DISTINCT
    CASE
        WHEN cnt<2 THEN NULL ELSE (SELECT salary FROM ranks WHERE rnk = 2 LIMIT 1)
    END as SecondHighestSalary
FROM ranks


/*
-- SIMPLER SOLUTION, takes more time though
SELECT
    MAX(salary) as SecondHighestSalary
FROM Employee
WHERE salary != (SELECT MAX(salary) FROM Employee)
*/
