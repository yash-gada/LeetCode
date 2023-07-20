-- 627. Swap Salary

UPDATE Salary
SET sex = CASE WHEN sex = 'm' THEN 'f' ELSE 'm' END
