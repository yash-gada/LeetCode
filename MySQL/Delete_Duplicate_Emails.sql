-- 196. Delete Duplicate Emails\

-- 2 SOLUTIONS, second one seems simpler (slightly)

/*
DELETE p2 FROM Person p1
INNER JOIN Person p2
WHERE p1.id < p2.id
AND p1.email = p2.email
*/

DELETE FROM Person
WHERE id NOT IN 
( 
SELECT * FROM (SELECT MIN(id) FROM Person GROUP BY email)t
)
