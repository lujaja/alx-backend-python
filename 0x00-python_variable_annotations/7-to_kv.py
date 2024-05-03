#!/usr/bin/env python3
"""
Complex types - string and int/float to tuple
"""
from typing import Tuple,  Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Function - to_kv

    Attribute:
        k (str): parameter
        v (int/float): paramter

    Return:
        tuple

    """
    return (k, float(v ** 2))
