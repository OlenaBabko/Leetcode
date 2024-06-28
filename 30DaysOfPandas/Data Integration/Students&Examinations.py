# student_id is the primary key (column with unique values) for this table.
# Each row of this table contains the ID and the name of one student in the school.
# subject_name is the primary key (column with unique values) for this table.
# Each row of this table contains the name of one subject in the school.
#  There is no primary key (column with unique values) for this table. It may contain duplicates.
# Each student from the Students table takes every course from the Subjects table.
# Each row of this table indicates that a student with ID student_id attended the exam of subject_name.
# Write a solution to find the number of times each student attended each exam.

# Return the result table ordered by student_id and subject_name


import pandas as pd

def students_and_examinations(students: pd.DataFrame, subjects: pd.DataFrame, examinations: pd.DataFrame) -> pd.DataFrame:
    # group and count each subject
    examinations = examinations.groupby(['student_id', 'subject_name']).agg(attended_exams=('subject_name', 'count')).reset_index() 
    students = students.merge(subjects, how='cross')
    examinations = examinations.merge(students, on=['student_id', 'subject_name'],how='right')
    # filling null values with 0
    examinations = examinations.fillna(0)
    examinations = examinations.sort_values(['student_id', 'subject_name'])
    return examinations[['student_id', 'student_name', 'subject_name', 'attended_exams']]



