#!/usr/bin/env python3
"""
        This function takes in two arguments,
                page and page_size,
        which are used to calculate
                the start and end indexes,
         for the range of items to return in a list.
        The page argument represents the current page number
        the page_size:
        argument represents the number of items to return per page.
"""

from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    '''Return tuple containing pagination start index and end index.'''

    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return (start_index, end_index)
