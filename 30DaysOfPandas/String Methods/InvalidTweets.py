# tweet_id is the primary key (column with unique values) for this table.
# This table contains all the tweets in a social media app.
# Write a solution to find the IDs of the invalid tweets. The tweet is
# invalid if the number of characters used in the content of the tweet is strictly greater than 15.
# Return the result table in any order.


# tweet is invalid if characters in  content > 15

import pandas as pd

def invalid_tweets(tweets: pd.DataFrame) -> pd.DataFrame:
    invalid_tweets_df = tweets[tweets['content'].str.len('content') > 15]
    invalid_tweets_id_df = invalid_tweets_df[['tweet_id']]
    return invalid_tweets_id_df




# Write your MySQL query statement below

SELECT tweet_id
FROM Tweets
WHERE (LENGTH (content) > 15);