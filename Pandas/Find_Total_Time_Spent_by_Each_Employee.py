# 1741. Find Total Time Spent by Each Employee

import pandas as pd

def total_time(employees: pd.DataFrame) -> pd.DataFrame:

    employees["out_time"] = employees["out_time"] - employees["in_time"]
    employees.drop("in_time", axis=1, inplace=True)
    employees = employees.groupby(["event_day", "emp_id"]).agg({"out_time":"sum"}).reset_index()

    return employees.rename(columns = {"event_day":"day", "out_time":"total_time"})
