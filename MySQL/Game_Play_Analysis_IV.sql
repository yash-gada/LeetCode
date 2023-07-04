-- 550. Game Play Analysis IV

WITH rnums as
(
SELECT
    *,
    ROW_NUMBER() OVER(PARTITION BY player_id ORDER BY player_id, event_date) as rnum
FROM Activity
),
diff as
(
SELECT
    *,
    DATEDIFF(event_date, LAG(event_date, 1) OVER(PARTITION BY player_id ORDER BY player_id, event_date)) as diff
FROM rnums
)

SELECT
    ROUND(SUM(CASE WHEN rnum = 2 AND diff = 1 THEN 1 ELSE 0 END)/COUNT(DISTINCT player_id), 2) as fraction
FROM diff
