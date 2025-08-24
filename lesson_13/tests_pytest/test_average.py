import pytest
from lesson_13.homeworks import average

@pytest.mark.parametrize(
    "input_list, expected",
    [
        ([3.1, 5.2, 4.3, 1.4, 5.6], 3.92),
        ([2, 2, 2], 2.0),
        ([1, 2], 1.5),
        ([10], 10.0),
        ([0, 0, 0], 0.0)
    ],
    ids=[
        "average_value_mixed",
        "average_value_all_int",
        "average_value_small_list",
        "average_value_single_value",
        "average_value_all_zeros"
    ]
)
def test_average_parametrized(input_list, expected):
    assert average(input_list) == pytest.approx(expected)

@pytest.mark.parametrize(
    "input_list",
    [
        [1.0, 2.5, 3.0],
        [4],
        [0, 0, 0],
        [10, 20, 30]
    ],
    ids=[
        "average_type_mixed",
        "average_type_1_value",
        "average_type_all_zeros",
        "average_type_all_int",
    ]
)
def test_average_type(input_list):
    avg = average(input_list)
    assert isinstance(avg, float)

def test_average_with_empty_list():
    with pytest.raises(ZeroDivisionError):
        average([])