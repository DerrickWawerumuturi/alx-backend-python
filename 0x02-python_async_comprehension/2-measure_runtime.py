#!/usr/bin/env python3
"""Run time for 4 parallel comprehensions
"""


async_comprehension = __import__('1-async_comprehension').async_comprehension


import asyncio
import time


async def measure_runtime():
    """ function executes async_comp.. 4 times
    """
    start_time = time.perf_counter()
    await asyncio.gather(
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
        async_comprehension()
    )
    end_time = time.perf_counter()
    return end_time - start_time
