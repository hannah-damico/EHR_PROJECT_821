"""Testing EHR Analysis."""

from ehr_analysis import parse_data2, num_older_than, sick_patients


def testing_parse_data2():
    """Check parse_data2 function coverage."""
    input_file = "/Users/hannahdamico/EHR_PROJECT_821/test_data1.txt"
    data1 = {
        "key1": ["item11", "item22"],
        "key2": ["item12", "item22"],
        "key3": ["item13", "item32"],
        "key4": ["item14", "item42"],
    }
    assert parse_data2(input_file) == data1


def testing_num_older_than():
    """Check num_older_than function coverage."""
    test = parse_data2("/Users/hannahdamico/EHR_PROJECT_821/test_data2.txt")

    assert num_older_than(-99, test) == 2
    assert num_older_than(999, test) == 0
    assert num_older_than(50, test) == 1


def testing_sick_patients():
    """Check sick_patients function coverage."""
    test = parse_data2("/Users/hannahdamico/EHR_PROJECT_821/test_table.txt")
    check_label = ["HAIUFABG-4543"]
    check_operation = ["BOAET-64EG"]

    assert sick_patients("METABOLIC: GLUCOSE", ">", 1.0, test) == check_label
    assert sick_patients("CBC: PLATELET COUNT", "<", 200, test) == 0
    assert sick_patients("CBC: PLATELET COUNT", "=", 4.5, test) == ValueError
