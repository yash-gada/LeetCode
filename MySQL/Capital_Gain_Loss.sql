-- 1393. Capital Gain/Loss

WITH newtab as
(
SELECT
    *,
    CASE WHEN operation = 'Buy' THEN -1*price ELSE price END as newval
FROM Stocks
)

SELECT
    stock_name,
    SUM(newval) as capital_gain_loss
FROM newtab
GROUP BY stock_name

/*
SIMPLER SOLUTION

select stock_name,
    sum( if(operation = "Buy", -1*price, price) ) as capital_gain_loss 
from Stocks
group by stock_name
*/
