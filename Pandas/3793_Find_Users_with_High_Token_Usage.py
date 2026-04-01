
# 3793. Find Users with High Token Usage

import pandas as pd

def find_users_with_high_tokens(prompts: pd.DataFrame) -> pd.DataFrame:
    prompts['prompt_count'] = prompts.groupby('user_id')['prompt'].transform('size')
    prompts['avg_tokens'] = prompts.groupby(['user_id'])['tokens'].transform('mean').round(2)

    mask = (prompts['prompt_count']>=3) & (prompts['tokens'] > prompts['avg_tokens'])
    prompts = prompts[mask]

    prompts = prompts[['user_id', 'prompt_count', 'avg_tokens']].drop_duplicates()

    return prompts.sort_values(['avg_tokens', 'user_id'], ascending=[False, True])
