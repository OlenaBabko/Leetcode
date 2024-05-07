# order_number is the primary key (column with unique values) for this table.
# This table contains information about the order ID and the customer ID.
# Write a solution to find the customer_number for the customer who has placed the largest number of orders.

# The test cases are generated so that exactly one customer will have placed more orders than any other customer.



# # # customer_number - placed the largest number of orders



import pandas as pd

def largest_orders(orders: pd.DataFrame) -> pd.DataFrame:
  group = orders.groupby('customer_number')['order_number'].count().reset_index()
  largest = group.sort_values('order_number', ascending=False)
  largest_orders =  largest[['customer_number']][0:1]
  return largest_orders




# Write your MySQL query statement below

SELECT customer_number
FROM Orders
GROUP BY customer_number
ORDER BY COUNT(order_number) DESC
LIMIT 1


# # # Subquery
# WITH subquery AS (
#     SELECT
#         customer_number
#         , COUNT(*) counts
#     FROM Orders
#         GROUP BY customer_number)
#
# SELECT
#     customer_number
# FROM subquery
#     ORDER BY counts DESC
# LIMIT 1