# 178. Rank Scores

import pandas as pd

def order_scores(scores: pd.DataFrame) -> pd.DataFrame:
    scores.sort_values(by="score", ascending=False, inplace=True)
    scores["rank"] = pd.factorize(scores["score"])[0]+1
    return scores[["score", "rank"]]
