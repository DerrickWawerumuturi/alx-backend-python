#!/usr/bin/env python3

""" import Sequence, Tuple and List from typing"""
from typing import List, Sequence, Tuple, Iterable


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """ returned a list """
    return [(i, len(i)) for i in lst]
