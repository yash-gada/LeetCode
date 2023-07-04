-- 1378. Replace Employee ID With The Unique Identifier

SELECT
    unique_id,
    e.name
FROM EmployeeUNI eu
RIGHT JOIN Employees e
ON e.id = eu.id;
