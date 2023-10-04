# 2882. Drop Duplicate Rows

import pandas as pd

def dropDuplicateEmails(customers: pd.DataFrame) -> pd.DataFrame:
    customers.drop_duplicates("email", inplace=True)
    return customers
