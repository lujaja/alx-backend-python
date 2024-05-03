#!/usr/bin/env python3
"""
Complex types - mixed list
"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Function - sum_mixed_list

    Attribute:
        mxd_lst (list): parameter
    Return:
        sum (float)
    """
    return (sum(mxd_lst))
