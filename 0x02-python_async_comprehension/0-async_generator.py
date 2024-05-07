#!/usr/bin/env python3
"""
Async Generator
"""
import asyncio
from typing import Generator
import random


async def async_generator() -> Generator[float, None, None]:
    """
    Asynchronous generator that yields random float numbers between 0 and 10.

    Yields:
        float: A random float number between 0 and 10.

    Returns:
        Generator[float, None, None]: An asynchronous generator object.

    Raises:
        None

    Examples:
        >>> async for num in async_generator():
        ...     print(num)
        4.2
        2.3
        8.9
        ...
    """
    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
