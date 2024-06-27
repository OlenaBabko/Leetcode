# sales_id is the primary key (column with unique values) for this table.
# Each row of this table indicates the name and the ID of a salesperson alongside
# their salary, commission rate, and hire date.
# com_id is the primary key (column with unique values) for this table.
# Each row of this table indicates the name and the ID of a company and the city in which the company is located.
# order_id is the primary key (column with unique values) for this table.
# com_id is a foreign key (reference column) to com_id from the Company table.
# sales_id is a foreign key (reference column) to sales_id from the SalesPerson table.
# Each row of this table contains information about one order. This includes the ID of
# the company, the ID of the salesperson, the date of the order, and the amount paid.
# Write a solution to find the names of all the salespersons who did not have any
# orders related to the company with the name "RED".
# Return the result table in any order.


### names who did not have orders with "RED"

# # SalesPerson
# sales_id, name, salary, commission_rate, hire_date
# # Company
# com_id, name, city
# # Orders
# order_id, order_date, com_id, sales_id, amount


import pandas as pd

def sales_person(sales_person: pd.DataFrame, company: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    com_id = pd.merge(company, orders, on= 'com_id')
    red = com_id[com_id['name'] == 'RED']['sales_id'].unique()
    sales_person_not_red = sales_person[~sales_person['sales_id'].isin(red)][['name']]
    return sales_person_not_red

### 2
def sales_person(sales_person: pd.DataFrame, company: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    com_id = pd.merge(company, orders, on= 'com_id')
    red = com_id[com_id['name'] == 'RED']
    not_red = red.sales_id.unique()
    sales_person_not_red = sales_person[~sales_person['sales_id'].isin(not_red)][['name']]
    return sales_person_not_red



