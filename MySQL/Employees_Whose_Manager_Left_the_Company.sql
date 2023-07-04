-- 1978. Employees Whose Manager Left the Company

SELECT
    e.employee_id
FROM Employees e
LEFT JOIN Employees m
ON e.manager_id = m.employee_id
WHERE m.employee_id IS NULL
AND e.salary < 30000
AND e.manager_id IS NOT NULL
ORDER BY employee_id
