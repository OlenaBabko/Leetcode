# patient_id is the primary key (column with unique values) for this table.
# 'conditions' contains 0 or more code separated by spaces. 
# This table contains information of the patients in the hospital.
# Write a solution to find the patient_id, patient_name, and conditions of 
# the patients who have Type I Diabetes. Type I Diabetes always starts with DIAB1 prefix.
# Return the result table in any order.



# patient_id, patient_name, conditions who starts with DIAB1 prefix



import pandas as pd

def find_patients(patients: pd.DataFrame) -> pd.DataFrame:
    find_patients_df = patients[patients['conditions'].str.contains(r'\bDIAB1')]
    return find_patients_df

# The \b in the pattern is a word boundary assertion that ensures 'DIAB1' is a separate word and not part of another word


