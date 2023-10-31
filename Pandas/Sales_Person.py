# 607. Sales Person

import pandas as pd

def sales_person(sales_person: pd.DataFrame, company: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    merged = sales_person[["sales_id", "name"]].merge(orders[["order_id", "com_id", "sales_id"]], how="left")

    merged = merged.merge(company[["com_id", "name"]], on="com_id", how="left", suffixes=("", "_com"))

    red = merged[merged["name_com"] == "RED"]["sales_id"].unique()

    merged = merged[~merged["sales_id"].isin(red)]["name"].unique()

    return pd.DataFrame({"name":merged})
