#!/usr/bin/env python3
""" Asynchronous Generator
"""


import random
import asyncio
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """ function loops 10 times each time, then wait 1 sec
    then return a random num between 0-10
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.random() * 10
