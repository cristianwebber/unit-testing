"""Example of a test module."""
import pytest

from src.total import total


@pytest.mark.parametrize(
    "xs, total_value", [
        ([], 0.0),
        ([0.0], 0.0), 
        ([1.0, 2.0], 3.0),
        ([2.5, 9.0], 11.5),
        ([2.1, 2.2], 4.3),
        ([2.11, 2.28], 4.39),
        ([2.132, 2.222], 4.354),
    ]
)
def test_total(xs, total_value) -> None:
    assert total(xs) == total_value

def test_if_not_a_list_is_passed():
    with pytest.raises(TypeError):
        total("Error")

def test_if_a_single_value_is_passed():
    with pytest.raises(ValueError):
        total(5)