
# 3570. Find Books with No Available Copies

import pandas as pd

def find_books_with_no_available_copies(library_books: pd.DataFrame, borrowing_records: pd.DataFrame) -> pd.DataFrame:

    curr = borrowing_records[borrowing_records['return_date'].isna()].groupby('book_id').size().rename('current_borrowers').reset_index()

    merged = pd.merge(library_books, curr, how='inner', on='book_id')
    
    final = merged[merged["current_borrowers"] == merged["total_copies"]]

    return final.drop('total_copies', axis=1).sort_values(['current_borrowers', 'title'], ascending=[False, True])
