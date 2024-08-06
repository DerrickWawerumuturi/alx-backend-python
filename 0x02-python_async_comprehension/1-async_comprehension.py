#!/usr/bin/env python3
""" Asynchronous comprehension
"""

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension():
    """ Collect 10 random numbers
    """
    numbers = [number async for number in async_generator()]
    return numbers
