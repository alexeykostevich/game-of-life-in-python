from abc import ABCMeta, abstractmethod
from typing import Callable, Iterable, List, TypeVar, Tuple
from life.world import World


T = TypeVar('T')


class BaseWorld(World[T]):
    """Represents a base class for worlds for 'The Game of Life'."""

    __metaclass__ = ABCMeta

    def __init__(self, width: int, height: int):
        if width <= 0:
            raise ValueError('width is zero or a negative number.')

        if height <= 0:
            raise ValueError('height is zero or a negative number.')

        self._width = width
        self._height = height
        self._data = dict()

    @property
    def width(self) -> int:
        """Returns world width."""
        return self._width

    @property
    def height(self) -> int:
        """Returns world height."""
        return self._height

    @abstractmethod
    def adjust_position(self, x: int, y: int) -> Tuple[int, int]:
        """Returns the world position."""
        pass

    @abstractmethod
    def is_position_in_range(self, x: int, y: int) -> bool:
        """Indicates whether the specified position is within the world boundaries."""
        pass

    @abstractmethod
    def empty(self) -> 'World[T]':
        """Returns a new empty world of the same dimensions."""
        pass

    def through(self) -> Tuple[int, int]:
        """Returns a new iterator that can iterate over world positions."""
        return ((x, y) for y in range(self.height)
                       for x in range(self.width))

    def neighbours_of(self, x: int, y: int) -> Iterable[T]:
        """Returns a new iterator that can iterate over neighbours around the specified position."""
        positions = [
            (x - 1, y - 1),  # NE
            (x, y - 1),      # N
            (x + 1, y - 1),  # NW
            (x + 1, y),      # W
            (x + 1, y + 1),  # SW
            (x, y + 1),      # S
            (x - 1, y + 1),  # SE
            (x - 1, y)       # E
        ]

        return (self[position] for position in positions if self.is_position_in_range(*position))

    def __getitem__(self, position: Tuple[int, int]) -> T:
        """Returns a value for the specified position using self[x, y]."""
        adjusted_position = self.adjust_position(*position)
        item = self._data.get(adjusted_position, None)

        return item

    def __setitem__(self, position: Tuple[int, int], value: T):
        """Sets the value for the specified position using self[x, y]."""
        adjusted_position = self.adjust_position(*position)

        if value is None:
            return

        self._data[adjusted_position] = value

    def __str__(self) -> str:
        """Returns a string representation of the world."""
        def to_str(i): return str(i or ' ')

        rows = ((to_str(self[x, y]) for x in range(self.width))
                                    for y in range(self.height))

        result = '\n'.join((''.join(row) for row in rows))

        return result

    def __eq__(self, other: 'BaseWorld[T]') -> bool:
        """Indicates whether the world equals to another world."""
        eq = self._data.items() == other._data.items()

        return eq

    @classmethod
    def from_data(cls, *kargs: List[T]) -> 'World[T]':
        """Creates a world from a 2-deminsiomal list."""
        world = cls(len(kargs[0]), len(kargs))

        for x, y in world.through():
            world[x, y] = kargs[y][x] if x < len(kargs[y]) else None

        return world

    @classmethod
    def random(cls, width: int, height: int, get_random: Callable[[], T]) -> 'World[T]':
        """Creates a random world of the specified dimensions."""
        world = cls(width, height)

        for x, y in world.through():
            world[x, y] = get_random()

        return world
