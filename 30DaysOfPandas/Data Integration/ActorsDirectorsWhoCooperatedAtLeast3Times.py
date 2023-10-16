# timestamp is the primary key (column with unique values) for this table.
# Write a solution to find all the pairs (actor_id, director_id) where
# the actor has cooperated with the director at least three times.

# Return the result table in any order.


import pandas as pd

def actors_and_directors(actor_director: pd.DataFrame) -> pd.DataFrame:
    grouped = actor_director.groupby(['actor_id','director_id'])
    aggregation = grouped.agg(count=('timestamp', 'count')).reset_index()
    actors_and_directors = aggregation[aggregation['count']>=3]
    return actors_and_directors[['actor_id', 'director_id']]




