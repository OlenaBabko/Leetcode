# product_id is the primary key (column with unique values) for this table.
# low_fats is an ENUM (category) of type ('Y', 'N') where 'Y' means this
# product is low fat and 'N' means it is not.
# recyclable is an ENUM (category) of types ('Y', 'N') where 'Y' means
# this product is recyclable and 'N' means it is not.
#
# Write a solution to find the ids of products that are both low fat and recyclable.

import pandas as pd

# ids of  low fat AND recyclable

def find_products(products: pd.DataFrame) -> pd.DataFrame:
    find_products_df = products[(products['low_fats'] == 'Y') & (products['recyclable'] == 'Y')]
    return find_products_df[['product_id']]


# Write your MySQL query statement below

SELECT product_id
FROM products
WHERE (low_fats = 'Y') AND (recyclable = 'Y');