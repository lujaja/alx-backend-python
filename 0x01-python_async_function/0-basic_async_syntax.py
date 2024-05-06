#!/usr/bin/env python3
"""
The basic of asynchronous function
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
    delay: float = random.uniform(0.0, max_delay)
    await asyncio.sleep(delay)
    return delay
