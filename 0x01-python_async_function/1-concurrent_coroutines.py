#!/usr/bin/env python3
"""
 Let's execute multiple coroutines at the same time with async
"""
import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Function - wait_n.

    Attrubutes:
        n (int): parameter 1
        max_delay (int): paramter 2

    Return:
        list of all delays
    """
    delays: dict[float, None] = {}
    tasks = [asyncio.create_task(wait_random(max_delay)) for _ in range(n)]
    for task in asyncio.as_completed(tasks):
        delay = await task
        delays[delay] = None
    return list(delays.keys())
