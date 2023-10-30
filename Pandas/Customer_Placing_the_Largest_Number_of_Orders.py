# 586. Customer Placing the Largest Number of Orders

import pandas as pd

def largest_orders(orders: pd.DataFrame) -> pd.DataFrame:
    
    orders = orders.groupby("customer_number").agg({"order_number":"count"}).reset_index()

    return orders.loc[orders["order_number"] == orders["order_number"].max(), ["customer_number"]]


    # Simpler and Faster solution:
    # return orders['customer_number'].mode().to_frame()
