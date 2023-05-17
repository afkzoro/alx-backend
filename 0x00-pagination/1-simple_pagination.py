#!/usr/bin/env python3
""" Implement a get_page method to get the subsets """
import csv
import math
from typing import List, Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
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
    return (start_index, end_index)


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        """__init__ method
        """
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Get the dataset from the CSV file.

        Returns:
            List[List]: The dataset containing the rows of the CSV file.

        """

        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """a method named get_page that takes two integer arguments page
        with default value 1 and page_size with default value 10

        Args:
            page (int, optional): _description_. Defaults to 1.
            page_size (int, optional): _description_. Defaults to 10.

        Returns:
            List[List]: appropriate subset of the dataset using
            the calculated indices.
        """
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        dataset = self.dataset()
        total_pages = math.ceil(len(dataset) / page_size)

        if page > total_pages:
            return []

        start_index, end_index = index_range(page, page_size)
        return dataset[start_index:end_index]
