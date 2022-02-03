"""Computational Complexity and Data Structures Project."""

import datetime
from datetime import date

DAYS_IN_YEAR = 365.25


def parse_data2(filename: str) -> dict:
    """Create a dict based on the txt file."""
    text_file = open(filename, mode="r", encoding="utf-8-sig")
    line_by_line = text_file.readlines()

    col_names = line_by_line[0]
    col_names_list = col_names.strip().split("\t")
    dataframe: dict[str, list] = {}
    for var in col_names_list:
        dataframe[var] = []

    for i in range(1, len(line_by_line)):
        line_data_list = line_by_line[i].strip().split("\t")
        for j in range(len(col_names_list)):
            dataframe[col_names_list[j]].append(line_data_list[j])

    text_file.close()
    return dataframe


patient_core = parse_data2(
    "/Users/hannahdamico/Desktop/W22/BIOSTAT 821/PatientCorePopulatedTable.txt"
)

labs_core = parse_data2(
    "/Users/hannahdamico/Desktop/W22/BIOSTAT 821/LabsCorePopulatedTable.txt"
)


def num_older_than(age: float, patient_core) -> int:
    """Considers number of days old a person is."""
    days_old = age * DAYS_IN_YEAR
    count_older = 0
    for values in patient_core["PatientDateOfBirth"]:
        year, month, day = values.split()[0].split("-")
        patient_age = date.today() - date(int(year), int(month), int(day))
        if patient_age.days > days_old:
            count_older += 1
    return count_older


def sick_patients(
    lab: str, gt_lt: str, value_compare: float, labs_core: dict
) -> list[str]:
    """Return list of patient IDs after testing for."""
    sick_patient_list: list[str] = []
    check_lab_value: list = []
    Lab_Value_to_float = [float(i) for i in labs_core["LabValue"]]  # O(N)
    check_lab_value.append(Lab_Value_to_float)

    for i, lab_name in enumerate(labs_core["LabName"]):  # O(N)
        if lab == lab_name:
            if gt_lt == ">":
                if check_lab_value[0][i] > value_compare:
                    patient_id = labs_core["PatientID"][i]
                    sick_patient_list.append(patient_id)
            elif gt_lt == "<":
                if check_lab_value[0][i] < value_compare:
                    patient_id = labs_core["PatientID"][i]
                    sick_patient_list.append(patient_id)
            else:
                raise ValueError(f"Invalid label {lab}")
    return sick_patient_list
