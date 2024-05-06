#!/usr/bin/env python3
"""
asynchronous coroutine that takes in an integer argument
(max_delay, with a default value of 10) named wait_random
that waits for a random delay between 0 and max_delay
(included and float value) seconds and eventually returns it.

Use the random module.
"""


import asyncio
import random


async def wait_random(max_delay: float = 10.0) -> float:
    """
    Function - wait_random

    Attributes:
        max_delay (float): default value 10.0

    Return (float): the delay waited
    """
    delay: float = random.random() * max_delay
    await asyncio.sleep(delay)
    return delay
