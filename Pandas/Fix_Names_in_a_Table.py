# 1667. Fix Names in a Table

import pandas as pd

def fix_names(users: pd.DataFrame) -> pd.DataFrame:

    # Slower
    #users["name"] = users["name"].apply(lambda x:x[0].upper()+x[1:].lower())
    
    users["name"] = users["name"].str.capitalize()
    return users.sort_values("user_id")
