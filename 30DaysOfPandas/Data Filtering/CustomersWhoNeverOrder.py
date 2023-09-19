# Table: Customers
# id is the primary key .
# Each row of this table indicates the ID and name of a customer.
# Orders
# id is the primary key (column with unique values) for this table.
# customerId is a foreign key (reference columns) of the ID from the Customers table.
# Each row of this table indicates the ID of an order and the ID of the customer who ordered it.
# Write a solution to find all customers who never order anything.


import pandas as pd

def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    find_customers_who_never_df = customers[~customers['id'].isin(orders['customerId'])]
    rename_df = find_customers_who_never_df[['name']].rename(columns={'name': 'Customers'})
    return rename_df

