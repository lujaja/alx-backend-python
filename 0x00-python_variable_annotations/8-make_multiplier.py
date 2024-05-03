#!/usr/bin/env python3
"""
Complex types - functions
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Create a function that multiplies a given number by a multiplier.

    Args:
        multiplier (float): The value to multiply the input by.

    Returns:
        callable[[float], float]: A function that takes a float as input and returns the product of the input and the multiplier.
    """
    return lambda x: x * multiplier
