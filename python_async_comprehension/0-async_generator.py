#!/usr/bin/python3
"""Async generator"""

import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """Yields random numbers asynchoronously"""
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
