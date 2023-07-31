-- 626. Exchange Seats

SELECT
    id,
    CASE
        WHEN id%2=0 THEN lag(student, 1) OVER(ORDER BY id)
        ELSE IFNULL(lead(student, 1) OVER(ORDER BY id), student)
    END as student
FROM Seat
