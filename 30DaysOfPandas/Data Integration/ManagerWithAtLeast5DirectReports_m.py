# id is the primary key (column with unique values) for this table.
# Each row of this table indicates the name of an employee, their department, and the id of their manager.
# If managerId is null, then the employee does not have a manager.
# No employee will be the manager of themself.
# Write a solution to find managers with at least five direct reports.

# Return the result table in any order.


import pandas as pd

def find_managers(employee: pd.DataFrame) -> pd.DataFrame:
    group = employee.groupby('managerId').count().reset_index() ### grouping by 'managerId', counting number of employees in each group, resetting the index.
    filter_managers = group.loc[group['id'] >=5, 'managerId']   ### .loc to filter df, keep rows where 'id'>=5, only want to keep the 'managerId' column.
    ###  checking if 'id' of employee in the employee df is in the list of 'managerId' values from the group df (>=5)
    managers = employee.loc[employee['id'].isin(group), ['name']]
    return managers

### '.loc' is used to filter and select specific rows and columns in a DF



## 1
SELECT Employee1.name
FROM Employee AS Employee1
INNER JOIN Employee AS Employee2
ON Employee1.id = Employee2.managerId
GROUP BY Employee1.id
HAVING COUNT(Employee2.managerId)>= 5;
