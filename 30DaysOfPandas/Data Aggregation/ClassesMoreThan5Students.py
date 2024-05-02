# (student, class) is the primary key (combination of columns with unique values) for this table.
# Each row of this table indicates the name of a student and the class in which they are enrolled.
# Write a solution to find all the classes that have at least five students.

# Return the result table in any order.


import pandas as pd

def find_classes(courses: pd.DataFrame) -> pd.DataFrame:
    classes_df = courses.groupby('class')['student'].count().reset_index()
    find_classes_df = classes_df[classes_df['student'] >=5][['class']]  # [['class']]- OUTPUT
    return find_classes_df

# df = courses.groupby('class').count().reset_index()


