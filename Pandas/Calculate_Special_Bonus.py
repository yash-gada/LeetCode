# 1873. Calculate Special Bonus

import pandas as pd

def calculate_special_bonus(employees: pd.DataFrame) -> pd.DataFrame:
    employees.loc[(employees["employee_id"]%2!=0) & (~employees["name"].str.startswith("M")), "bonus"] = employees["salary"]
    employees["bonus"].fillna(0, inplace=True)
    return employees[["employee_id", "bonus"]].sort_values("employee_id")
