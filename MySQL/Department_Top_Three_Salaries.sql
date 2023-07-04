-- 185. Department Top Three Salaries

With rsal as (
SELECT DISTINCT
    d.id,
    d.name,
    e.name as ename,
    e.salary,
    DENSE_RANK() OVER(PARTITION BY d.id ORDER BY e.salary DESC) as drank
FROM Employee e
INNER JOIN Department d
ON e.departmentId = d.id
)

SELECT 
    name as Department,
    ename as Employee,
    salary 
FROM rsal 
WHERE drank <= 3 
