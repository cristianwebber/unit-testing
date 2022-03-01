"""An example Python module."""

from typing import List


def total(xs: List[float]) -> float:
    """Total sum of xs.

    Args:
        xs (List[float]): list of x values

    Returns:
        float: sum of xs values rounded by 1
    """
    return round(sum(xs), 4)
