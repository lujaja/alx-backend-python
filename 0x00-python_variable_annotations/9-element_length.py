#!/usr/bin/env python3"
"""
Basic annotation - element_length
"""
from typing import Iterable, Sequence, Tuple, List


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Calculate the length of each element in the input list.

    Args:
        lst (Iterable[Sequence]): The input list of sequences.

    Returns:
        List[Tuple[Sequence, int]]:
        A list of tuples where each tuple contains an element
          from the input list and its length.
    """
    return [(x, len(x)) for x in lst]
    return list(map(lambda x: (x, len(x)), lst))
