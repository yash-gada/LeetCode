-- 262. Trips and Users

SELECT
    t.request_at as Day,
    ROUND(SUM(IF(t.status LIKE 'cancelled_by_%', 1, 0))/ COUNT(*), 2) as'Cancellation Rate'
FROM Trips t
WHERE t.client_id NOT IN (SELECT users_id FROM Users WHERE banned = 'Yes')
AND t.driver_id NOT IN (SELECT users_id FROM Users WHERE banned = 'Yes')
AND t.request_at BETWEEN '2013-10-01' AND "2013-10-03"
GROUP BY t.request_at;
