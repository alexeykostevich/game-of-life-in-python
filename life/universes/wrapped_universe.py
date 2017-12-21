from typing import TypeVar, Tuple
from ..universes.base_universe import BaseUniverse


T = TypeVar('T')


class WrappedUniverse(BaseUniverse[T]):
    """
    Represents the wrapped universe of 'The Game of Life'.
    The edges of the universe wrap around, so that the top is connected to the bottom,
    and the right is connected to the left.
    """

    def adjust_position(self, x: int, y: int) -> Tuple[int, int]:
        """Returns an adjusted position for the closed universe."""
        adjusted_position = x % self.width, y % self.height

        return adjusted_position

    def is_position_in_range(self, x: int, y: int) -> bool:
        """Always returns true since edges of the universe wrap around."""
        return True

    def empty_copy(self) -> 'WrappedUniverse[T]':
        """Returns an empty wrapped universe of the same dimensions."""
        return WrappedUniverse(self.width, self.height)
