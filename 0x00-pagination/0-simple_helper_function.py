#!/usr/bin/env python

def index_range(page: int, page_size: int) -> tuple:
    """
        This function takes in two arguments, 
                page and page_size,
        which are used to calculate 
                the start and end indexes,
         for the range of items to return in a list. 
        The page argument represents the current page number
        while the page_size argument represents the number of items to return per page.
    """

    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return (start_index, end_index)
