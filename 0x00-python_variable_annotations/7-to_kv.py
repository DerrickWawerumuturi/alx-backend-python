#!/usr/bin/env python3

""" import union from typing"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """ return a tuple(k[0], v*2) """
    return (k, float(v ** 2))
