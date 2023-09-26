# user_id is the primary key (column with unique values) for this table.
# This table contains the ID and the name of the user. The name consists of only lowercase and uppercase characters.
# Write a solution to fix the names so that only the first character is uppercase and the rest are lowercase.
# Return the result table ordered by user_id.

import pandas as pd

def fix_names(users: pd.DataFrame) -> pd.DataFrame:
    users['name'] = users['name'].str.capitalize()
    fix_names_sorted_df = users[['user_id','name']].sort_values('user_id')
    return fix_names_sorted_df



# Write your MySQL query statement below

SELECT user_id, CONCAT(UPPER(SUBSTR(name,1,1)),LOWER(SUBSTR(name,2,length(name)))) AS name
FROM Users
ORDER BY user_id ASC;

