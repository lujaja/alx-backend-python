#!/usr/bin/env python3
"""
Type Checking
"""
from typing import Tuple, List


def zoom_array(lst: Tuple[int, ...], factor: int = 2) -> List[int]:
    """
    Generate a zoomed-in version of an array by repeating each element
      a specified number of times.

    Args:
        lst (Tuple[int, ...]): The input array to be zoomed in.
        factor (int, optional): The number of times each element
          should be repeated. Defaults to 2.

    Returns:
        List[int]: The zoomed-in version of the input array.
    """
    return [item for item in lst * factor]
