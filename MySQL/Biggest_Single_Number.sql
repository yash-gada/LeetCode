-- 619. Biggest Single Number

SELECT
    CASE WHEN COUNT(*) = 1 THEN num ELSE NULL END as num
FROM MyNumbers
GROUP BY num
ORDER BY num desc LIMIT 1;
