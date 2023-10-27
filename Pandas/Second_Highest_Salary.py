# 176. Second Highest Salary

import pandas as pd

def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    if(len(employee["salary"].unique()) < 2):
        return pd.DataFrame([None], columns=["SecondHighestSalary"])
    return pd.DataFrame([sorted(employee["salary"].unique(), reverse=True)[1]], columns=["SecondHighestSalary"])
