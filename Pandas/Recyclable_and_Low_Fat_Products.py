# 1757. Recyclable and Low Fat Products

import pandas as pd

def find_products(products: pd.DataFrame) -> pd.DataFrame:
    
    return products.loc[(products['low_fats']=='Y') & (products['recyclable']=='Y'), ["product_id"]]

    # 2nd method to solve the question
    #return products[(products['low_fats']=='Y') & (products['recyclable']=='Y')][["product_id"]]
