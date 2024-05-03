#!/usr/bin/env python3
"""
100-safe_first_element.py
"""
from typing import Sequence, Any, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """
    Returns the first element of the given list if it is not
     empty, otherwise returns None.

    :param lst: A sequence of elements.
    :type lst: Sequence[Any]
    :return: The first element of the list if it is not empty, otherwise None.
    :rtype: Union[Any, None]
    """
    if lst:
        return lst[0]
    else:
        return None
