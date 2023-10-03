# id is the primary key (column with unique values) for this table.
# Each row of this table contains an email. The emails will not contain uppercase letters.
# Write a solution to delete all duplicate emails, keeping only one unique email with the smallest id
# For SQL users, please note that you are supposed to write a DELETE statement and not a SELECT one.
# For Pandas users, please note that you are supposed to modify Person in place.
# After running your script, the answer shown is the Person table. The driver will first compile and run 
# your piece of code and then show the Person table. The final order of the Person table does not matter

# only 1 unique email with the smallest id
# a DELETE statement and not a SELECT one.


import pandas as pd
# Modify Person in place
def delete_duplicate_emails(person: pd.DataFrame) -> None:
    id_sort = person.sort_values('id', inplace=True)
    email_drop_duplicates = person.drop_duplicates(['email'], inplace=True)





# Write your MySQL query statement below
DELETE person_1
FROM Person person_1, Person person_2
WHERE person_1.email = person_2.email AND person_1.id > person_2.id;