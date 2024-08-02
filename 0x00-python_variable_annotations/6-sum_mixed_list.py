#!/usr/bin/env python3

""" import list and union from typing """
from typing import List, Union


def sum_mixed_list(mxd_list: List[Union[int, float]]) -> float:
    """ return a float of the sum """
    return sum(mxd_list)
