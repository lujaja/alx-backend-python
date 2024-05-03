#!/usr/bin/env python3
"""
Type Checking
"""
from typing import Tuple, List


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """
    Function that zooms an array by repeating its elements
      a certain number of times.

    Args:
        lst (Tuple): The input tuple of elements.
        factor (int): The factor by which to zoom the array.
          Default is 2.

    Returns:
        List: A list containing the elements of the input
          tuple repeated by the factor.
    """
    return [item for item in lst * factor]


array = (12, 72, 91)

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3)
