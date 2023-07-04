-- 1789. Primary Department for Each Employee

SELECT
    employee_id,
    department_id
FROM Employee
WHERE primary_flag = 'Y' 
UNION DISTINCT
SELECT
    employee_id,
    department_id
FROM Employee
GROUP BY employee_id
HAVING COUNT(department_id) = 1
