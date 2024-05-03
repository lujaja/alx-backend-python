#!/usr/bin/env python3
"""
safely_get_value
"""
from typing import TypeVar, Mapping, Any, Union


T = TypeVar('T')


def safely_get_value(
        dct: Mapping,
        key: Any,
        default: Union[T, None] = None
) -> Union[Any, T]:
    """
    Safely retrieves a value from a dictionary using a given key.

    Args:
        dct (Mapping): A dictionary from which to retrieve the value.
        key (Any): The key used to retrieve the value from the dictionary.
        default (Union[T, None], optional):
            The default value to return if the key is not
             in the dictionary. Defaults to None.

    Returns:
        Union[Any, T]: The value associated with the given key
        or the default value if the key is not in the dictionary.
    """
    return dct.get(key, default)
