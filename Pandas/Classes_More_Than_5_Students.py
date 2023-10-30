# 596. Classes More Than 5 Students

import pandas as pd

def find_classes(courses: pd.DataFrame) -> pd.DataFrame:
    
    courses = courses.groupby("class")["student"].nunique().reset_index()

    return courses[courses["student"]>4][["class"]]
