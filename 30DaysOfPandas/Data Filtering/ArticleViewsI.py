# There is no primary key (column with unique values) for this table, the table may have duplicate rows.
# Each row of this table indicates that some viewer viewed an article (written by some author) on some date.
# Note that equal author_id and viewer_id indicate the same person.
# Write a solution to find all the authors that viewed at least one of their own articles.
# Return the result table sorted by id in ascending order.


# author_id  == viewer_id == id AND IS unique

import pandas as pd

def article_views(views: pd.DataFrame) -> pd.DataFrame:
  own_article_views_df = views[views['author_id'] == views['viewer_id']]
  own_article_views_unique_df = own_article_views_df[['author_id']].drop_duplicates()
  own_article_views_sorted_df = own_article_views_unique_df.sort_values('author_id')
  own_article_views_rename_df = own_article_views_sorted_df.rename(columns = {'author_id' : 'id'})
  return own_article_views_rename_df





# Write your MySQL query statement below

SELECT DISTINCT author_id as id
FROM Views
WHERE author_id = viewer_id
ORDER BY id ASC;