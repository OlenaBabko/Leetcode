# id is the primary key (column with unique values) for this table.
# Each row of this table contains information about the salary of an employee.
# Write a solution to find the second highest salary from the Employee table. 
# If there is no second highest salary, return null (return None in Pandas).


import pandas as pd

def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    duplicates = employee['salary'].drop_duplicates()
    sort = duplicates.sort_values(ascending=False)
    if len(sort) > 1:
        second_highest_salary = sort.iloc[1]
    else:
        second_highest_salary = None
    return pd.DataFrame({'SecondHighestSalary': [second_highest_salary]})
## iloc[1] means you want to select the value at the index position 1.
##  sort.iloc[1] selects the second-highest salary from the sorted list of salaries




# Write your MySQL query statement bel

SELECT (
    SELECT DISTINCT salary
    FROM Employee
    ORDER BY salary DESC
    LIMIT 1 OFFSET 1)
AS SecondHighestSalary;
