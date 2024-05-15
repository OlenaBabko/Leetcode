# There is no primary key (column with unique values) for this table. It may contain duplicates.
# Each row of this table contains the product name and the date it was sold in a market.
# Write a solution to find for each date the number of different products sold and their names.
# The sold products names for each date should be sorted lexicographically.

# Return the result table ordered by sell_date.


## sorted lexicographically


import pandas as pd

def categorize_products(activities: pd.DataFrame) -> pd.DataFrame:
    duplicats = activities.drop_duplicates(['product','sell_date'])
    sorted =  duplicats.sort_values(['sell_date','product'])
    grouped = sorted.groupby('sell_date')
    aggregation = grouped.agg(num_sold = ('product', 'count'), products = ('product', ','.join)).reset_index()
    return aggregation




SELECT sell_date,
    COUNT(DISTINCT(product), sell_date) AS num_sold,
    GROUP_CONCAT(DISTINCT product ORDER BY product)  AS products
FROM Activities
GROUP BY sell_date
ORDER BY sell_date;
# GROUP_CONCAT(DISTINCT product order by product ASC separator ',' ) as products
### GROUP_CONCAT, in which you can also specify the sorting mechanism for the group concatenation (aggregation).