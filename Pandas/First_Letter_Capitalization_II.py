# 3374. First Letter Capitalization II

import pandas as pd

def capitalize_content(user_content: pd.DataFrame) -> pd.DataFrame:

    user_content['converted_text'] = user_content['content_text'].str.title()
    
    user_content.rename(columns={'content_text':'original_text'}, inplace=True)
    return user_content
