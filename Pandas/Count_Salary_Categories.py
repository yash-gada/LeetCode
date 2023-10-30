# 1907. Count Salary Categories

import pandas as pd

def count_salary_categories(accounts: pd.DataFrame) -> pd.DataFrame:
    new = pd.DataFrame()
    new["category"] = ["Low Salary", "Average Salary", "High Salary"]
    new["accounts_count"] = [None, None, None]

    new.loc[new["category"]=="Low Salary", "accounts_count"] = accounts.loc[accounts["income"]<20000, "account_id"].shape[0]
    new.loc[new["category"]=="Average Salary", "accounts_count"] = accounts.loc[(20000<=accounts["income"]) & (accounts["income"]<=50000), "account_id"].shape[0]
    new.loc[new["category"]=="High Salary", "accounts_count"] = accounts.loc[accounts["income"]>50000, "account_id"].shape[0]

    '''
    # nunique() slower than shape[0]
    
    new.loc[new["category"]=="Low Salary", "accounts_count"] = accounts.loc[accounts["income"]<20000, "account_id"].nunique()
    new.loc[new["category"]=="Average Salary", "accounts_count"] = accounts.loc[(20000<=accounts["income"]) & (accounts["income"]<=50000), "account_id"].nunique()
    new.loc[new["category"]=="High Salary", "accounts_count"] = accounts.loc[accounts["income"]>50000, "account_id"].nunique()
    '''
    return new
