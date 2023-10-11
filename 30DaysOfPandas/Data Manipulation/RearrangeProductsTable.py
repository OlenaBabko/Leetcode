# product_id is the primary key (column with unique values) for this table.
# Each row in this table indicates the product's price in 3 different stores: store1, store2, and store3.
# If the product is not available in a store, the price will be null in that store's column.
# Write a solution to rearrange the Products table so that each row has (product_id, store, price). If a product 
# is not available in a store, do not include a row with that product_id and store combination in the result table.
# Return the result table in any order.


# each row has (product_id, store, price), not available = do not include
# pandas.melt(frame, id_vars=None, value_vars=None, var_name=None, value_name='value', col_level=None)

import pandas as pd

def rearrange_products_table(products: pd.DataFrame) -> pd.DataFrame:
    rearrange_df = pd.melt(products, id_vars='product_id', value_vars= ['store1', 'store2', 'store3'], var_name='store', value_name='price')
    drop_df = rearrange_df.dropna()     # get rid of the null values
    return drop_df




# Write your MySQL query statement below

SELECT product_id, 'store1' AS store, store1 AS price
FROM Products
WHERE store1 IS NOT NULL
UNION
SELECT product_id, 'store2' AS store, store2 AS price
FROM Products
WHERE store2 IS NOT NULL
UNION
SELECT product_id, 'store3' AS store, store3 AS price
FROM Products
WHERE store3 IS NOT NULL
ORDER BY product_id, store;