
# 3497. Analyze Subscription Conversion 

import pandas as pd

def analyze_subscription_conversion(user_activity: pd.DataFrame) -> pd.DataFrame:
    
    #mask = user_activity.groupby('user_id')['activity_type'].transform('nunique') >= 2
    mask = user_activity.groupby('user_id')['activity_type'].transform(lambda x: {'free_trial', 'paid'}.issubset(set(x)))

    user_activity = user_activity[mask]

    user_activity = user_activity.groupby(['user_id', 'activity_type'])['activity_duration'].agg('mean').apply(lambda x: x+0.0001).round(2).unstack().reset_index()

    user_activity = user_activity.drop(columns=['cancelled'], errors='ignore')
    
    user_activity = user_activity.rename(columns={
    'free_trial': 'trial_avg_duration',
    'paid': 'paid_avg_duration'
    })


    mask2 = user_activity['paid_avg_duration'].isna() == False

    return user_activity[mask2].sort_values('user_id', ascending=True)
    #columns=['user_id', 'trial_avg_duration', 'paid_avg_duration'])
