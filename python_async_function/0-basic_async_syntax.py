#!/usr/bin/env python3
"""Async function"""

import random
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    """waits for random delay and returns."""
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)

    return delay
