"""
Part 4 of EHR Cumulative project.
Implementing SQLite.
"""

import sqlite3
import os

if os.path.exists("ehr_data.db"):
    os.remove("ehr_data.db")


con = sqlite3.connect("/Users/hannahdamico/EHR_PROJECT_821/ehr_data.db")

cur = con.cursor()

cur.execute(
    """CREATE TABLE patient(pat_id VARCHAR PRIMARY KEY,
    gender VARCHAR,
    dob VARCHAR,
    race VARCHAR,
    marital_status VARCHAR,
    language VARCHAR,
    pop_below_poverty FLOAT)
    """
)

cur.execute(
    """CREATE TABLE labs ([pat_id] VARCHAR NOT NULL,
    [admission_id] VARCHAR NOT NULL,
    [lab_name] VARCHAR,
    [lab_value] FLOAT,
    [lab_units] VARCHAR,
    [lab_date_time] VARCHAR,
    CONSTRAINT lab_id PRIMARY KEY (pat_id, admission_id))
    """
)


def parse_data_patient(file: str):
    """Parse Data for Patients."""
    filename = open(file)
    next(filename)
    for row in filename:
        observations = row.strip().split("\t")
        data = observations[0:7]
        cur.execute("INSERT INTO patient VALUES (?, ?, ?, ?, ?, ?, ?)", data)


def parse_data_labs(file: str):
    """Parse Data for Labs."""
    filename = open(file)
    next(filename)
    for row in filename:
        observations = row.strip().split("\t")
        data = observations[0:6]
        cur.execute("INSERT INTO labs VALUES (?, ?, ?, ?, ?, ?)", data)


def num_older_than(age: int) -> int:
    """Compute total number of patients older than input number."""
    age_list = [age]
    count_older = cur.execute(
        "SELECT COUNT (pat_id) FROM patient WHERE  (JULIANDAY('now') - JULIANDAY(dob))/365.25 > ?",
        age_list,
    )
    return count_older.fetchall()[0][0]


def sick_patients(lab_name: str, value: float, gt_lt: str):
    """Return a list of patients with specific lab & lab value."""
    lab_name_match = [lab_name, value]
    sick_patient_list = cur.execute(
        f"""SELECT pat_id,lab_date_time FROM labs WHERE lab_name = ? AND lab_value {gt_lt} ?
        """,
        lab_name_match,
    )
    return sick_patient_list.fetchall()


def first_admission_age(pat_id: str):
    """Calculate age of patient at first admission."""
    patient_id = [pat_id]
    age = cur.execute(
        """SELECT DATE(labs.lab_date_time) - DATE(patient.dob)
        FROM patient INNER JOIN labs ON patient.pat_id = labs.pat_id
        WHERE labs.admission_id = 1 AND patient.pat_id = ?

    """,
        patient_id,
    )
    return age.fetchall()[0][0]


parse_data_patient("patient_core_test_data.txt")
parse_data_labs("labs_core_test_data.txt")
