#!/usr/bin/env python3
"""
Run time for four parallel comprehensions
"""
import asyncio
import time
cpr = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Function - measure_runtime

    Return:
        runtime (time)
    """
    tasks = [cpr(), cpr(), cpr(), cpr()]
    start_time = time.time()
    await asyncio.gather(*tasks)
    end_time = time.time()
    return (end_time - start_time)
