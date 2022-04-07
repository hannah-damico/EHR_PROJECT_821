"""Computational Complexity and Data Structures Project."""

import logging

from datetime import date, datetime, timedelta


logging.basicConfig(format="%(levelname)s:%(message)s", level=logging.DEBUG)


DAYS_IN_YEAR = 365.25


class Lab:
    """Create a class with lab information."""

    def __init__(
        self,
        patID: str,
        ad_id: str,
        label: str,
        value: float,
        LabDateTime: datetime,
    ):
        """Initialize lab information."""
        self._patID = patID
        self.ad_id = ad_id
        self._label = label
        self._value = value
        self._LabDateTime = LabDateTime


class Patient:
    """Create a class with patient information."""

    def __init__(self, patID: str, gender: str, dob: datetime, race: str) -> None:
        """Initialize patient demographic information."""
        self._patID = patID
        self._gender = gender
        self._dob = dob
        self._race = race
        self._labs: list[Lab] = []

    @property
    def age(self) -> float:
        """Calculate patient age."""
        current_time = datetime.now()
        dob = self._dob
        time_diff = current_time - dob
        age = time_diff.days / DAYS_IN_YEAR
        return age

    @property
    def first_admission_age(self):
        """Compute patient age at first admission."""
        min_lab_date = self._labs[0]._LabDateTime
        for lab in self._labs:
            if lab.ad_id == "1" and lab._LabDateTime < min_lab_date:
                min_lab_date = lab._LabDateTime
        diff = min_lab_date - self._dob
        return diff.days / DAYS_IN_YEAR

    def retrieve_labs(self, lab: Lab) -> None:
        """Retrieve labs from Lab."""
        self._labs.append(lab)


def parse_data(filename: str) -> dict[str, list[str]]:
    """After dropping constant order operations, we have O(N^2 + N) complexity since we nested for loops."""
    with open(filename, mode="r", encoding="utf-8-sig") as text_file:
        line_by_line = text_file.readlines()

    col_names = line_by_line[0]
    col_names_list = col_names.strip().split("\t")
    dataframe: dict[str, list] = {}
    for var in col_names_list:  # O(N)
        dataframe[var] = []

    for i in range(1, len(line_by_line)):  # O(N)
        line_data_list = line_by_line[i].strip().split("\t")
        for j in range(len(col_names_list)):  # O(N)
            dataframe[col_names_list[j]].append(line_data_list[j])

    text_file.close()
    return dataframe


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
            patID=data_dict["PatientID"],
            gender=data_dict["PatientGender"],
            dob=datetime.strptime(data_dict["PatientDateOfBirth"], "%Y-%m-%d"),
            race=data_dict["PatientRace"],
        )
        patient_dict[patient._patID] = patient
    return patient_dict


print(
    parse_data_Patient("/Users/hannahdamico/EHR_PROJECT_821/patient_core_test_data.txt")
)


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
            patID=data_dict["PatientID"],
            ad_id=data_dict["AdmissionID"],
            label=data_dict["LabName"],
            value=float(data_dict["LabValue"]),
            LabDateTime=datetime.strptime(data_dict["LabDateTime"], "%Y-%m-%d"),
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
        if lab_name == lab._label:  # O(1)
            if gt_lt == ">":
                if lab._value > value_compare:  # O(2)
                    patient_id = lab._patID  # O(2)
                    sick_patient_list.add(patient_id)  # O(1)
            elif gt_lt == "<":  # O(1)
                if lab._value < value_compare:  # O(2)
                    patient_id = lab._patID  # O(2)
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
):
    """Compute age at first admission for specific a patient."""
    test_date_list: list[date] = []
    for lab in labs_core.values():
        if patientID == lab._patID:
            test_date_list.append(lab._LabDateTime)
    first_admission = min(test_date_list)
    diff = (first_admission - patient_core[patientID]._dob) / DAYS_IN_YEAR
    # first_admission_age = diff.days
    return first_admission_age
