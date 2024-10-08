#!/usr/bin/env python3
"""
Simple helper function for pagination
"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Return a tuple of start and end indexes for a given page and page size.

    Args:
    page (int): The page number (1-indexed)
    page_size (int): The number of items per page

    Returns:
    Tuple[int, int]: A tuple containing the start index and end index
    """
    start_idx = (page - 1) * page_size
    end_idx = start_idx + page_size
    return (start_idx, end_idx)
