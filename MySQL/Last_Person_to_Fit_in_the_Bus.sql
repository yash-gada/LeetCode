-- 1204. Last Person to Fit in the Bus

WITH sums as 
(
SELECT
    person_id,
    person_name,
    SUM(weight) OVER(ORDER BY turn) as tw,
    ROW_NUMBER() OVER(ORDER BY turn)  as rnum
FROM Queue
ORDER BY rnum DESC
)

SELECT
    person_name
FROM sums
GROUP BY person_id
HAVING MAX(tw) <= 1000
ORDER BY rnum DESC LIMIT 1
