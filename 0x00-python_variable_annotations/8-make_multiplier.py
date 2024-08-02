#!/usr/bin/env python3

""" import Callable from typing"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """ returns a function that multiplies a float by multiplier"""
    def multiply(value: float) -> float:
        return value * multiplier
    return multiply
