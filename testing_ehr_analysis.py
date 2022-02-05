"""Testing EHR Analysis."""

from ehr_analysis import parse_data2, num_older_than, sick_patients


def testing_parse_data2():
    """Check parse_data2 function coverage."""
    input_file = "/Users/hannahdamico/EHR_PROJECT_821/test_table.txt"
    under_test = parse_data2(input_file)

	assert parse_data2(input_file)
    assert isinstance(parse_data2(input_file), dict)
