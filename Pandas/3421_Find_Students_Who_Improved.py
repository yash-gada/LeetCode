
# 3421. Find Students Who Improved

import pandas as pd

def find_students_who_improved(scores: pd.DataFrame) -> pd.DataFrame:

    grouped = scores.groupby(['student_id', 'subject'])['score'].agg(['first', 'last']).reset_index()

    mask = grouped['first']<grouped['last']
    grouped = grouped[mask]

    grouped.columns=['student_id', 'subject','first_score', 'latest_score']

    return grouped.sort_values(['student_id', 'subject'], ascending=[True, True])
