# 177. Nth Highest Salary

import pandas as pd

def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
    employee = employee["salary"].drop_duplicates()
    if(N > len(employee)):
        return pd.DataFrame([pd.NA], columns=[f"getNthHighestSalary({N})"])
    ans = employee.sort_values(ascending=False).reset_index(drop=True)[N-1]
    return pd.DataFrame([ans], columns=[f"getNthHighestSalary({N})"])
