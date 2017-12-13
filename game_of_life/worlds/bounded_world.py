from typing import TypeVar, Tuple
from .base_world import BaseWorld


T = TypeVar('T')


class BoundedWorld(BaseWorld[T]):
    """Represents a world with boundaries for 'The Game of Life'."""

    def adjust_position(self, x: int, y: int) -> Tuple[int, int]:
        """Returns the world position."""
        if (not self.is_position_in_range(x, y)):
            raise IndexError()

        return x, y

    def is_position_in_range(self, x: int, y: int) -> bool:
        """Indicates whether the specified position is within the world boundaries."""
        is_in_range = 0 <= x < self.width and 0 <= y < self.height

        return is_in_range
