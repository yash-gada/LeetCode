# 184. Department Highest Salary

import pandas as pd

def department_highest_salary(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:
    merged = employee.merge(department, left_on="departmentId", right_on="id", suffixes=("_emp", "_dep"))
    
    merged = merged.groupby("id_dep").apply(lambda x:x[x["salary"]==x["salary"].max()])

    merged = merged[["name_dep", "name_emp", "salary"]]
    merged.rename(columns={"name_dep":"Department", "name_emp":"Employee", "salary":"Salary"}, inplace=True)

    return merged
