# name is the primary key (column with unique values) for this table.
# Each row of this table gives information about the name of a country,
# the continent to which it belongs, its area, the population, and its GDP value.
# A country is big if:
# it has an area of at least three million (i.e., 3000000 km2), or
# it has a population of at least twenty-five million (i.e., 25000000).
# Write a solution to find the name, population, and area of the big countries.

import pandas as pd

# name >=3000000 km2 OR >=25000000

def big_countries(world: pd.DataFrame) -> pd.DataFrame:
  big_countries_df = world[(world['area'] >= 3000000) | (world['population'] >= 25000000)]
  return big_countries_df[['name', 'population', 'area']]



# Write your MySQL query statement below

# SELECT name, population, area
# FROM World
# WHERE (population >= 25000000) OR (area >= 3000000) ;