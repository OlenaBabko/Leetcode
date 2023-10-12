# id is the primary key (column with unique values) for this table.
# departmentId is a foreign key (reference columns) of the ID from the Department table.
# Each row of this table indicates the ID, name, and salary of an employee. It also contains the ID of their department.
#  id is the primary key (column with unique values) for this table. It is guaranteed that department name is not NULL.
# Each row of this table indicates the ID of a department and its name.
# Write a solution to find employees who have the highest salary in each of the departments.

# Return the result table in any order.

import pandas as pd

def department_highest_salary(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:
    employee_renamed = employee.rename(columns={'name': 'Employee', 'salary': 'Salary'})
    department_renamed = department.rename(columns={'name': 'Department'})
    merged = employee_renamed.merge(department_renamed, left_on='departmentId', right_on='id')
    max_salary = merged.groupby('Department')['Salary'].transform(max)
    max_in_department = merged[merged['Salary'] == max_salary]
    dep_h_sal_df = max_in_department[['Department', 'Employee', 'Salary']]
    return dep_h_sal_df





# Write your MySQL query statement below

SELECT Department.name AS Department, Employee.name AS Employee, Employee.salary AS Salary
FROM Employee
LEFT JOIN Department
ON Employee.departmentId = Department.id
WHERE (Employee.departmentID, Employee.salary) IN (
    SELECT departmentID, max(Employee.salary)
    FROM Employee
    GROUP BY Employee.departmentID);