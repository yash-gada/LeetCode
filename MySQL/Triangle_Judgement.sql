-- 610. Triangle Judgement

SELECT
    *,
    CASE
        WHEN x+y>z AND y+z>x AND x+z>y THEN 'Yes'
        ELSE 'No'
    END as triangle
FROM Triangle
