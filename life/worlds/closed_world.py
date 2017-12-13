from typing import TypeVar, Tuple
from life.worlds.base_world import BaseWorld


T = TypeVar('T')


class ClosedWorld(BaseWorld[T]):
    """Represents a closed world without boundaries for 'The Game of Life'."""

    def adjust_position(self, x: int, y: int) -> Tuple[int, int]:
        """Returns an adjusted position for the closed world."""
        adjusted_position = x % self.width, y % self.height

        return adjusted_position

    def is_position_in_range(self, x: int, y: int) -> bool:
        """Always returns true since the world is closed."""
        return True

    def empty(self) -> 'BoundedWorld[T]':
        """Returns a new empty world of the same dimensions."""
        return ClosedWorld(self.width, self.height)
