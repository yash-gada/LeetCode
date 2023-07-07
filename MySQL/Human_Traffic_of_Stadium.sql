-- 601. Human Traffic of Stadium

WITH consec as
(
SELECT
    *,
    lead(id, 1) OVER() as second_id,
    lead(id, 2) OVER() as third_id,
    lag(id, 1) OVER() as prev1_id,
    lag(id, 2) OVER() as prev2_id
FROM Stadium
WHERE people>=100 
)

SELECT
    id,
    visit_date,
    people
FROM consec
WHERE (second_id-id = 1 AND third_id-id = 2)
OR (id-prev1_id = 1 AND second_id-id = 1)
OR (id-prev1_id = 1 AND id-prev2_id = 2)
