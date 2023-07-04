-- 602. Friend Requests II: Who Has the Most Friends

WITH collated as 
(SELECT
    requester_id as id
FROM RequestAccepted
UNION ALL
SELECT
    accepter_id as id
FROM RequestAccepted
)

SELECT
    id,
    COUNT(id) as num
FROM collated
GROUP BY id
ORDER BY num DESC
LIMIT 1
