# 511. Game Play Analysis I

import pandas as pd

def game_analysis(activity: pd.DataFrame) -> pd.DataFrame:
    return activity.groupby("player_id").agg({"event_date":"min"}).reset_index().rename(columns = {"event_date":"first_login"})
