# employee_id is the primary key (column with unique values) for this table.
# Each row of this table indicates the employee ID, employee name, and salary.
# Write a solution to calculate the bonus of each employee. The bonus of an employee is 100% of their
# salary if the ID of the employee is an odd number and the employee's name does not start with the character 'M'.
# The bonus of an employee is 0 otherwise.
#
# Return the result table ordered by employee_id.


# bonus = 100% if  ID = odd number AND name does not start with 'M'


import pandas as pd

def calculate_special_bonus(employees: pd.DataFrame) -> pd.DataFrame:
    employees['bonus'] = 0
    employees.loc[(employees['employee_id'] %2 != 0) & (~employees['name'].str.startswith('M')), 'bonus'] = employees['salary']
    bonus_df = employees[['employee_id', 'bonus']].sort_values('employee_id')
    return bonus_df




# Write your MySQL query statement belo

SELECT employee_id, IF ((employee_id%2 != 0) AND (name NOT LIKE 'M%'), salary, 0) AS bonus
FROM Employees
ORDER BY employee_id ASC;