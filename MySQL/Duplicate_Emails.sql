-- 182. Duplicate Emails

/*
-- Alternate Solution

SELECT
    email
FROM (SELECT
        email,
        COUNT(*) as cnt
    FROM Person
    GROUP BY email)t
WHERE cnt>1
*/

SELECT
    email
FROM Person
GROUP BY email
HAVING COUNT(*) > 1;
