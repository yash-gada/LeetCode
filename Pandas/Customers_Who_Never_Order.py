# 183. Customers Who Never Order

import pandas as pd

def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    '''
    # Slower method
    
    df = pd.merge(left=customers, right=orders, how="left", left_on="id", right_on="customerId")
    return df.loc[df["id_y"].isna() == True, ["name"]].rename(columns={"name":"Customers"})
    '''

    df = customers[~customers["id"].isin(orders["customerId"])]
    return df[["name"]].rename(columns={"name":"Customers"})
