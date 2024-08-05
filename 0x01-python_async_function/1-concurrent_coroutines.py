#!/usr/bin/env python3
'''Task 1
'''
import asyncio as pause
from typing import List


wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    ''' Execute wait random n times
    '''
    wait_times = await pause.gather(
        *tuple(map(lambda _: wait_random(max_delay), range(n)))
    )
    return sorted(wait_times)
