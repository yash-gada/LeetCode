# 1148. Article Views I

import pandas as pd

def article_views(views: pd.DataFrame) -> pd.DataFrame:
    
    df = views.loc[views["author_id"]==views["viewer_id"], "author_id"]
    df = df.sort_values()
    return pd.DataFrame(df.unique(), columns=["id"])
    '''
    #Slower
    return views[views["author_id"]==views["viewer_id"]][["author_id"]].rename(columns={"author_id":"id"}).drop_duplicates().sort_values("id")
    '''
