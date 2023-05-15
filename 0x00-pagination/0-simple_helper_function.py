#!/usr/bin/env python3
""" Function `index_range`
Takes  two integer arguments page and page_size
"""


def index_range(page: int, page_size: int) -> tuple[int, int]:
    """ a function named index_range that takes
    two integer arguments page and page_size

    Args:
        page (int): page number
        page_size (int): page size

    Returns:
        tuple[int, int]: Return index of the starting page and last page
    """
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return start_index, end_index
