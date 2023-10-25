# 1517. Find Users With Valid E-Mails

import pandas as pd

def valid_emails(users: pd.DataFrame) -> pd.DataFrame:
  
    valid = users[users["mail"].str.match(r'^[A-Za-z][A-Za-z0-9_\.\-]*@leetcode\.com$')]
    
    return valid
  
