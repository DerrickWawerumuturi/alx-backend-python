#!/usr/bin/env python3
""" Task 0
"""
import asyncio as pause
import random


async def wait_random(max_delay: int = 10):
    """ Waits for a random delay between 0 and the number given. """
    delay = random.uniform(0, max_delay)
    await pause.sleep(delay)
    return delay
