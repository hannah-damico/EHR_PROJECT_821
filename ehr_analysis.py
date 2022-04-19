"""Computational Complexity and Data Structures Project."""

import logging

from datetime import date, datetime, timedelta
from math import floor


logging.basicConfig(format="%(levelname)s:%(message)s", level=logging.DEBUG)


DAYS_IN_YEAR = 365.25


class Lab:
    """Create a class with lab information."""

    def __init__(
        self,
        pat_id: str,
        ad_id: str,
        label: str,
        value: float,
        lab_date_time: datetime,
    ):
        """Initialize lab information."""
        self.pat_id = pat_id
        self.ad_id = ad_id
        self.label = label
        self.value = value
        self.lab_date_time = lab_date_time


class Patient:
    """Create a class with patient information."""

    def __init__(self, pat_id: str, gender: str, dob: datetime, race: str) -> None:
        """Initialize patient demographic information."""
        self.pat_id = pat_id
        self.gender = gender
        self.dob = dob
        self.race = race
        self.labs: list[Lab] = []

    @property
    def age(self) -> float:
        """Calculate patient age."""
        current_time = datetime.now()
        dob = self.dob
        time_diff = current_time - dob
        age = time_diff.days / DAYS_IN_YEAR
        return age


def parse_data_Patient(filename: str) -> dict[str, Patient]:
    """After dropping constant order operations, we have O(N^2 + N) complexity since we nested for loops."""
    with open(filename, mode="r", encoding="utf-8-sig") as text_file:
        line_by_line = text_file.readlines()

    col_names = line_by_line[0]
    col_names_list = col_names.strip().split("\t")

    rows_data = [row_string.split("\t") for row_string in line_by_line[1:]]

    patient_dict = {}
    for rows in rows_data:
        data_dict = dict(zip(col_names_list, rows))
        patient = Patient(
            pat_id=data_dict["PatientID"],
            gender=data_dict["PatientGender"],
            dob=datetime.strptime(data_dict["PatientDateOfBirth"], "%Y-%m-%d"),
            race=data_dict["PatientRace"],
        )
        patient_dict[patient.pat_id] = patient
    return patient_dict


def parse_data_Labs(filename: str) -> dict[int, Lab]:
    """After dropping constant order operations, we have O(N^2 + N) complexity since we nested for loops."""
    with open(filename, mode="r", encoding="utf-8-sig") as text_file:
        line_by_line = text_file.readlines()

    col_names = line_by_line[0]
    col_names_list = col_names.strip().split("\t")

    rows_data = [row_string.split("\t") for row_string in line_by_line[1:]]

    Labs_dict = {}
    for i, rows in enumerate(rows_data):
        data_dict = dict(zip(col_names_list, rows))
        lab = Lab(
            pat_id=data_dict["PatientID"],
            ad_id=data_dict["AdmissionID"],
            label=data_dict["LabName"],
            value=float(data_dict["LabValue"]),
            lab_date_time=datetime.strptime(data_dict["LabDateTime"][0:10], "%Y-%m-%d"),
        )
        Labs_dict[i] = lab
    return Labs_dict


def num_older_than(age: float, patient_core: dict[str, Patient]) -> int:
    """Compute total number of patients older than input number."""
    count_older = 0
    for patient in patient_core.values():  # O(N)
        if patient.age > age:
            count_older += 1
    return count_older


def sick_patients(
    lab_name: str, gt_lt: str, value_compare: float, labs_core: dict[int, Lab]
) -> set[str]:
    """Each if conditional statement has constant complexity and are not counted in overall. Function has O(N)."""
    sick_patient_list: set[str] = set()
    # check_lab_value = [float(i) for i in labs_core.value()]  # O(N)
    for lab in labs_core.values():  # O(N)
        if lab_name == lab.label:  # O(1)
            if gt_lt == ">":
                if lab.value > value_compare:  # O(2)
                    patient_id = lab.pat_id  # O(2)
                    sick_patient_list.add(patient_id)  # O(1)
            elif gt_lt == "<":  # O(1)
                if lab.value < value_compare:  # O(2)
                    patient_id = lab.pat_id  # O(2)
                    sick_patient_list.add(patient_id)  # O(1)
            else:
                raise ValueError(f"Unexpected inequality symbol: {gt_lt}")

    if len(sick_patient_list) == 0:
        logging.info(" No patients found under these conditions.")
    else:
        return sick_patient_list
    return sick_patient_list


def first_admission_age(
    patientID: str, patient_core: dict[str, Patient], labs_core: dict[int, Lab]
) -> int:
    """Compute age at first admission for specific a patient."""
    test_date_list: list[date] = []
    for lab in labs_core.values():
        if patientID == lab.pat_id:
            test_date_list.append(lab.lab_date_time)
    first_admission = min(test_date_list)
    diff = (first_admission - patient_core[patientID].dob) / DAYS_IN_YEAR
    first_admission_age = diff.days
    return first_admission_age
