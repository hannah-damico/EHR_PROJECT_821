"""Testing EHR Analysis."""
import pytest
from datetime import datetime
from ehr_analysis import (
    parse_data,
    num_older_than,
    sick_patients,
    first_admission_age,
    Patient,
    Lab,
)


def testing_parse_data():
    """Check parse_data2 function coverage."""
    simple_test_data = "simple_test_data.txt"

    check_simple_test_data = {
        "key1": ["item11", "item21"],
        "key2": ["item12", "item22"],
        "key3": ["item13", "item23"],
        "key4": ["item14", "item24"],
    }

    assert parse_data(simple_test_data) == check_simple_test_data


def testing_class_Patient_method():
    """Check first_admission_age method in class Patient."""
    patient_core = parse_data("patient_core_test_data.txt")

    # assert


def testing_num_older_than():
    """Check num_older_than function coverage."""
    patient_core_test_data = parse_data("patient_core_test_data.txt")

    assert num_older_than(-99, patient_core_test_data) == 2
    assert num_older_than(999, patient_core_test_data) == 0
    assert num_older_than(50, patient_core_test_data) == 1


def testing_sick_patients():
    """Check sick_patients function coverage."""
    labs_core_test_data = parse_data("labs_core_test_data.txt")
    check_label = set(["HAIUFABG-4543"])
    check_operation = set(["BOAET-64EG"])

    assert (
        sick_patients("METABOLIC: GLUCOSE", ">", 1.0, labs_core_test_data)
        == check_label
    )
    assert (
        sick_patients("CBC: PLATELET COUNT", "<", 300, labs_core_test_data)
        == check_operation
    )
    assert sick_patients("CBC: PLATELET COUNT", "<", 200, labs_core_test_data) == set()
    with pytest.raises(ValueError):
        sick_patients("CBC: PLATELET COUNT", "=", 4.5, labs_core_test_data)


def testing_first_admission_age():
    """Check first_admission_age function coverage."""
    patient_core_test_data = parse_data("patient_core_test_data.txt")
    labs_core_test_data = parse_data("labs_core_test_data.txt")
    check_patient_id1 = "HAIUFABG-4543"
    check_patient_id2 = "BOAET-64EG"

    assert (
        first_admission_age(
            check_patient_id1, patient_core_test_data, labs_core_test_data
        )
        == 27
    )
    assert (
        first_admission_age(
            check_patient_id2, patient_core_test_data, labs_core_test_data
        )
        == 4
    )


lab1 = Lab(
    patID="HAIUFABG-4543",
    label="METABOLIC: GLUCOSE",
    value=2.52,
    units="mg/dl",
    LabDateTime=datetime.strptime("1992-06-30 09:35:57.150", "%Y-%m-%d %H:%M:%S.%f"),
)
