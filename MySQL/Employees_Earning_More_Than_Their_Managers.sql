-- 181. Employees Earning More Than Their Managers

/*
Alternate solution, takes more time.

SELECT
    e.name as Employee
FROM Employee e
WHERE salary > (SELECT salary FROM Employee WHERE id = e.managerId);
*/

SELECT
    e1.name as Employee
FROM Employee e1
INNER JOIN Employee e2
ON e1.managerId = e2.id
WHERE e1.salary > e2.salary;
