-- 184. Department Highest Salary

SELECT
    d.name as Department,
    e.name as Employee,
    e.salary as Salary
FROM Department d
INNER JOIN Employee e
ON d.id = e.departmentId
WHERE salary = (SELECT MAX(salary) FROM Employee WHERE departmentid = d.id);
