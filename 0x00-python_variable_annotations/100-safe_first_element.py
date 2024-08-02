#!/usr/bin/env python3

""" import Sequence, Any and Union"""
from typing import Sequence, Any, Union
""" Define a generic type variable """


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """ return the lst"""
    if lst:
        return lst[0]
    else:
        return None
