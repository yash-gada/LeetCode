# 1527. Patients With a Condition

import pandas as pd

def find_patients(patients: pd.DataFrame) -> pd.DataFrame:
    
    return patients[(patients["conditions"].str.startswith("DIAB1")==True)|(patients["conditions"].str.contains(" DIAB1")==True)]
