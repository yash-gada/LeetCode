-- 1141. User Activity for the Past 30 Days I

SELECT DISTINCT 
    activity_date as day, 
    COUNT(DISTINCT user_id) as active_users
FROM Activity
WHERE activity_date <= '2019-07-27'
AND DATEDIFF('2019-07-27', activity_date)<30
GROUP BY activity_date;
--HAVING COUNT(activity_type)>2; 
