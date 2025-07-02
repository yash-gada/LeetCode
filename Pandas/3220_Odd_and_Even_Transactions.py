# 3220. Odd and Even Transactions

import pandas as pd

def sum_daily_odd_even(transactions: pd.DataFrame) -> pd.DataFrame:
    
    transactions["even_sum"] = transactions['amount'].where(transactions['amount']%2==0,0)
    transactions["odd_sum"] = transactions['amount'].where(transactions['amount']%2==1,0)
    
    #print(transactions)
    transactions = transactions.groupby('transaction_date').agg({'odd_sum':'sum', 'even_sum':'sum'}).reset_index()
    #print(transactions)

    return transactions
