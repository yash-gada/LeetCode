# 570. Managers with at Least 5 Direct Reports

import pandas as pd

def find_managers(employee: pd.DataFrame) -> pd.DataFrame:
    merged = pd.merge(employee[["id","name"]], employee, right_on="managerId", left_on="id", suffixes=("", "_emp"))

    merged = merged.groupby(["id", "name"]).agg({"id_emp":"count"}).reset_index()

    return merged[merged["id_emp"]>4][["name"]]
