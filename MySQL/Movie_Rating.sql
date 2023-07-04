-- 1341. Movie Rating

(SELECT
    u.name as results
FROM Users u
INNER JOIN MovieRating mr
ON u.user_id = mr.user_id
GROUP BY mr.user_id
ORDER BY COUNT(*) DESC, u.name
LIMIT 1)
UNION ALL
(SELECT
    m.title as results
FROM MovieRating mr
INNER JOIN Movies m
ON m.movie_id = mr.movie_id
WHERE mr.created_at LIKE '2020-02%'
GROUP BY mr.movie_id
ORDER BY AVG(rating) DESC, m.title
LIMIT 1)
