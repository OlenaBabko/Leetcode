# (player_id, event_date) is the primary key (combination of columns with unique values) of this table.
# This table shows the activity of players of some games.
# Each row is a record of a player who logged in and played a number of games 
# (possibly 0) before logging out on someday using some device.
# Write a solution to find the first login date for each player.

# Return the result table in any order.


import pandas as pd

def game_analysis(activity: pd.DataFrame) -> pd.DataFrame:
    game_activity_df = activity.sort_values(['player_id', 'event_date'])
    game_activity_id_df = game_activity_df.groupby('player_id')['event_date'].min().reset_index()
    game_activity_rename_df = game_activity_id_df.rename(columns={'event_date': 'first_login'})
    return game_activity_rename_df





