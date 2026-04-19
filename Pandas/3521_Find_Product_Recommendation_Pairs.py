
# 3521. Find Product Recommendation Pairs

import pandas as pd

def find_product_recommendation_pairs(product_purchases: pd.DataFrame, product_info: pd.DataFrame) -> pd.DataFrame:

    product_purchases = product_purchases[['user_id', 'product_id']]
    pairs = pd.merge(product_purchases, product_purchases, how='inner', on='user_id', suffixes=('_a', '_b')).rename(columns = {'product_id_a':'product1_id', 'product_id_b':'product2_id'})

    pairs = pairs[pairs['product1_id'] < pairs['product2_id']]

    pairs = pairs.groupby(['product1_id', 'product2_id'])['user_id'].size().reset_index(name='customer_count')
    pairs = pairs[pairs['customer_count'] >= 3]

    product_info = product_info[['product_id', 'category']]

    pairs = pd.merge(pairs, product_info, left_on='product1_id', right_on='product_id').rename(columns={'category': 'product1_category'}).drop(columns='product_id')
    pairs = pd.merge(pairs, product_info, left_on='product2_id', right_on='product_id').rename(columns={'category': 'product2_category'}).drop(columns='product_id')

    pairs = pairs[['product1_id', 'product2_id', 'product1_category', 'product2_category', 'customer_count']]

    return pairs.sort_values(['customer_count', 'product1_id', 'product2_id'], ascending=[False, True, True])
