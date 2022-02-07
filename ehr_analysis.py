"""Computational Complexity and Data Structures Project."""

from datetime import date
import logging

logging.basicConfig(format="%(levelname)s:%(message)s", level=logging.DEBUG)


DAYS_IN_YEAR = 365.25


def parse_data(filename: str) -> dict[str, list]:
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


patient_core = parse_data2("/Users/hannahdamico/EHR_PROJECT_821/test_data2.txt")
labs_core = parse_data2("/Users/hannahdamico/EHR_PROJECT_821/test_table.txt")


def num_older_than(age: float, patient_core: dict[str, list]) -> int:
    """Compute total number of patients older than input number."""
    days_old = age * DAYS_IN_YEAR
    count_older = 0
    for values in patient_core["PatientDateOfBirth"]:  # O(N)
        year, month, day = values.split()[0].split("-")
        patient_age = date.today() - date(int(year), int(month), int(day))
        if patient_age.days > days_old:  # O(1)
            count_older += 1
    return count_older


def sick_patients(
    lab: str, gt_lt: str, value_compare: float, labs_core: dict[str, list]
) -> set[str]:
    """Each if conditional statement has constant complexity and are not counted in overall. Function has O(N)."""
    sick_patient_list: set[str] = set()
    check_lab_value = [float(i) for i in labs_core["LabValue"]]  # O(N)
    for i, lab_name in enumerate(labs_core["LabName"]):  # O(N)
        if lab == lab_name:  # O(1)
            if gt_lt == ">":
                if check_lab_value[i] > value_compare:  # O(2)
                    patient_id = labs_core["PatientID"][i]  # O(2)
                    sick_patient_list.add(patient_id)  # O(1)
            elif gt_lt == "<":  # O(1)
                if check_lab_value[i] < value_compare:  # O(2)
                    patient_id = labs_core["PatientID"][i]  # O(2)
                    sick_patient_list.add(patient_id)  # O(1)
            else:
                raise ValueError(f"Unexpected inequality symbol: {gt_lt}")

    if len(sick_patient_list) == 0:
        logging.info(" No patients found under these conditions.")
    else:
        return sick_patient_list
    return sick_patient_list


def first_admission_age(
    patientID: str, patient_core: dict[str, list], labs_core: dict[str, list]
):
    """Return patient age at first admission."""
    for i, values in enumerate(patient_core["PatientDateOfBirth"]):
        if patientID == patient_core["PatientID"][i]:
            year, month, day = values.split()[0].split("-")
            dob = date(int(year), int(month), int(day))
        for j in labs_core["LabDateTime"][i]:
            test_date_list: list[date] = []
            year_visit, month_visit, day_visit = (
                labs_core["LabDateTime"][i].split()[0].split("-")
            )
            admission_dates = date(int(year_visit), int(month_visit), int(day_visit))
            test_date_list.append(admission_dates)
            first_admission = min(test_date_list)
    diff = abs((first_admission - dob)) / DAYS_IN_YEAR
    first_admission_age = diff.days
    return (
        f"Patient {patientID} was {first_admission_age} years old at first admission."
    )
