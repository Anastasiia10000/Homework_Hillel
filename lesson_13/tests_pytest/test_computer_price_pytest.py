from Homework_Hillel.lesson_13.homeworks import computer_price
import pytest

@pytest.mark.positive
def test_computer_price_correct_result():
    assert computer_price(18, 1179) == 21222

@pytest.mark.positive
def test_return_type():
    assert isinstance(computer_price(18, 1179), int)

@pytest.mark.positive
def test_zero_payment():
    assert computer_price(18, 0) == 0

@pytest.mark.positive
def test_zero_period():
    assert computer_price(0, 1179) == 0

@pytest.mark.negative
def test_negative_values():
    assert computer_price(-1, 1179) < 0
    assert computer_price(18, -100) < 0