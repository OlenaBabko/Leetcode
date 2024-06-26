# id is the primary key (column with unique values) for Employees table.
# Each row of this table contains the id and the name of an employee in a company.
#
# (id, unique_id) is the primary key (combination of columns with unique values) for EmployeeUNI table.
# Each row of this table contains the id and the corresponding unique id of an employee in the company.
# Write a solution to show the unique ID of each user, If a user does not have a unique ID replace just show null.

# Return the result table in any order.


### id from Employees =  id from EmployeeUNI => unique_id


import pandas as pd

def replace_employee_id(employees: pd.DataFrame, employee_uni: pd.DataFrame) -> pd.DataFrame:
    merged = pd.merge(employees, employee_uni, on= 'id', how='left')    ### = employees.merge(employee_uni, on='id', how='left')
    replaced = merged[['unique_id', 'name']]
    return replaced


# Write your MySQL query statement below

SELECT UNI.unique_id, Employees.name
FROM Employees
LEFT JOIN EmployeeUNI AS UNI
ON Employees.id = UNI.id;

## 2
SELECT Emp.id, Emp.name, UNI.unique_id
FROM Employees AS Emp
LEFT JOIN EmployeeUNI AS  UNI
ON Emp.id = UNI.id;