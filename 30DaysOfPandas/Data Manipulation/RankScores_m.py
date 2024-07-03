# id is the primary key (column with unique values) for this table.
# Each row of this table contains the score of a game. Score is a floating point value with two decimal places.
# Write a solution to find the rank of the scores. The ranking should be calculated according to the following rules:

# The scores should be ranked from the highest to the lowest.
# If there is a tie between two scores, both should have the same ranking.
# After a tie, the next ranking number should be the next consecutive integer value. In other words, there should be no holes between ranks.
# Return the result table ordered by score in descending order


import pandas as pd

def order_scores(scores: pd.DataFrame) -> pd.DataFrame:
    sorted = scores.sort_values('score', ascending=False)
    sorted['rank'] = sorted['score'].rank(method='dense', ascending=False)
    return sorted[['score','rank']]



###
SELECT score,
(SELECT count(distinct Score)
 FROM Scores
 WHERE Score >= score.Score) RANK
FROM Scores score
ORDER BY Score DESC


### 2
SELECT score, DENSE_RANK() OVER(ORDER BY score DESC) as "rank"
FROM Scores


### dense_rank() is a window function that assigns a rank to each row within the result set, 
# ensuring that rows with the same values get the same rank.