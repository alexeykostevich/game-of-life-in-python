import random
from typing import TypeVar


CellType = TypeVar('CellType', bound='Cell')


class Cell(object):
    """Represents a cell of 'The Game of Life'."""

    def __str__(self) -> str:
        """Returns a string representation of the cell."""
        return '*'

    @classmethod
    def likely(cls) -> CellType:
        """Randomly creates a new cell or nothing."""
        possible_cell = random.choice([cls(), None])

        return possible_cell
