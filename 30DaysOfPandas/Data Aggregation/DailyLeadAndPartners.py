# There is no primary key (column with unique values) for this table. It may contain duplicates.
# This table contains the date and the name of the product sold and the IDs of the lead and partner it was sold to.
# The name consists of only lowercase English letters.
# For each date_id and make_name, find the number of distinct lead_id's and distinct partner_id's.

# Return the result table in any order.


#
import pandas as pd
def daily_leads_and_partners(daily_sales: pd.DataFrame) -> pd.DataFrame:
    grouped = daily_sales.groupby(['date_id', 'make_name']).nunique().reset_index()
    renamed = grouped.rename(columns={'lead_id': 'unique_leads', 'partner_id': 'unique_partners'})
    return renamed
 # grouped.columns = ['date_id', 'make_name', 'unique_leads', 'unique_partners']




SELECT date_id, make_name,
    COUNT(DISTINCT(lead_id), date_id, make_name) AS unique_leads,
    COUNT(DISTINCT(partner_id), date_id, make_name) AS unique_partners
FROM DailySales
GROUP BY date_id, make_name;
