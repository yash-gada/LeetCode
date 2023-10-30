# 1280. Students and Examinations

import pandas as pd

def students_and_examinations(students: pd.DataFrame, subjects: pd.DataFrame, examinations: pd.DataFrame) -> pd.DataFrame:
    
    merged = students.merge(subjects, how="cross")
    examinations["attended_exams"] = 0
    examinations = examinations.groupby(["student_id", "subject_name"]).agg("count").reset_index()

    merged = merged.merge(examinations, on=["student_id", "subject_name"], how="left").fillna(0)

    return merged.sort_values(by=["student_id", "subject_name"])[["student_id", "student_name", "subject_name", "attended_exams"]]
