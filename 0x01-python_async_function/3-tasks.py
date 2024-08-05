#!/usr/bin/env python3
"""asyncio.Task
"""
import asyncio


wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay) -> asyncio.Task:
    """ returns a created task
    """
    return asyncio.create_task(wait_random(max_delay))