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

    def __init__(self, gender: str, dob: datetime, race: str) -> None:
        """Initialize patient demographic information."""
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


def num_older_than(age: float, patient_core: list[Patient]) -> int:
    """Compute total number of patients older than input number."""
    count_older = 0
    for i in range(len(patient_core)):  # O(N)
        if patient_core[i].age > age:
            count_older += 1
    return count_older


def sick_patients(
    lab: str, gt_lt: str, value_compare: float, labs_core: list[Lab]
) -> set[str]:
    """Each if conditional statement has constant complexity and are not counted in overall. Function has O(N)."""
    sick_patient_list: set[str] = set()
    # check_lab_value = [float(i) for i in labs_core.value()]  # O(N)
    for i in range(len(labs_core)):  # O(N)
        if lab == labs_core[i]._label:  # O(1)
            if gt_lt == ">":
                if labs_core[i]._value > value_compare:  # O(2)
                    patient_id = labs_core[i]._patID  # O(2)
                    sick_patient_list.add(patient_id)  # O(1)
            elif gt_lt == "<":  # O(1)
                if labs_core[i]._value < value_compare:  # O(2)
                    patient_id = labs_core[i]._patID  # O(2)
                    sick_patient_list.add(patient_id)  # O(1)
            else:
                raise ValueError(f"Unexpected inequality symbol: {gt_lt}")

    if len(sick_patient_list) == 0:
        logging.info(" No patients found under these conditions.")
    else:
        return sick_patient_list
    return sick_patient_list


def first_admission_age(
    patientID: str, patient_core: dict[str, list[str]], labs_core: dict[str, list[str]]
):
    """Compute age at first admission for specific a patient."""
    test_date_list: list[date] = []
    for i, patID in enumerate(patient_core["PatientID"]):
        if patientID != patID:
            continue
        year, month, day = patient_core["PatientDateOfBirth"][i].split()[0].split("-")
        dob = date(int(year), int(month), int(day))
        for j, lab_time in enumerate(labs_core["LabDateTime"]):
            if patientID == labs_core["PatientID"][j]:
                year_visit, month_visit, day_visit = (
                    labs_core["LabDateTime"][j].split()[0].split("-")
                )
                admission_dates = date(
                    int(year_visit), int(month_visit), int(day_visit)
                )
                test_date_list.append(admission_dates)
    first_admission = min(test_date_list)
    diff = (first_admission - dob) / DAYS_IN_YEAR
    first_admission_age = diff.days
    return first_admission_age


# def first_admission_age(
#     patientID: str, patient_core: list[Patient], labs_core: list[Lab]
# ) -> float:
#     """Compute age at first admission for specific a patient."""
#     test_date_list: list[datetime] = []
#     for i in range(len(labs_core)):
#         if patientID != labs_core[i]._patID:
#             continue
#         dob = patient_core[i]._dob
#         for j in range(len(labs_core)):
#             if patientID == labs_core[j]._patID:
#                 admission_dates = labs_core[j]._LabDateTime
#                 test_date_list.append(admission_dates)
#     first_admission = min(test_date_list)
#     diff = first_admission - dob
#     first_admission_age = diff.days / DAYS_IN_YEAR
#     return first_admission_age
