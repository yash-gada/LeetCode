-- 1890. The Latest Login in 2020

SELECT
    user_id,
    MAX(time_stamp) as last_stamp
FROM Logins
WHERE DATE_FORMAT(time_stamp, '%Y') = 2020
GROUP BY user_id
