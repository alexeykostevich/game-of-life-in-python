from typing import Generic, Iterable, List, TypeVar, Tuple


T = TypeVar('T')


class SparseGrid(Generic[T]):
    """Represents a sparse grid that holds memory only for occupied positions."""

    def __init__(self, width: int, height: int, justify: int = 1):
        if width <= 0:
            raise ValueError('width is zero or a negative number.')

        if height <= 0:
            raise ValueError('height is zero or a negative number.')

        if justify < 1:
            raise ValueError('justify is a negative number.')

        self._width = width
        self._height = height
        self._justify = justify
        self._data = dict()

    @property
    def width(self) -> int:
        """Returns grid width."""
        return self._width

    @property
    def height(self) -> int:
        """Returns grid height."""
        return self._height

    def get_positions(self) -> Tuple[int, int]:
        """Returns a new iterator that can iterate over grid positions."""
        for y in range(self.height):
            for x in range(self.width):
                yield (x, y)

    def get_neighbours_positions_for(self, x: int, y: int) -> Iterable[Tuple[int, int]]:
        """Returns a new iterator that can iterate over neighbours positions around the specified position."""
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

        return (position for position in positions if self.is_position_in_range(*position))

    def get_neighbours_for(self, x: int, y: int) -> Iterable[T]:
        """Returns a new iterator that can iterate over neighbours around the specified position."""
        yield from (self[neighbour_position] for neighbour_position in self.get_neighbours_positions_for(x, y))

    def get_rows(self) -> Iterable[Iterable[T]]:
        """Returns a new iterator that can iterate over grid rows."""
        yield from ((self[x, y] for x in range(self.width)) for y in range(self.height))

    def get_columns(self) -> Iterable[Iterable[T]]:
        """Returns a new iterator that can iterate over grid columns."""
        yield from ((self[x, y] for y in range(self.height)) for x in range(self.width))

    def adjust_position(self, x: int, y: int) -> Tuple[int, int]:
        """Returns the grid position."""
        if (not self.is_position_in_range(x, y)):
            raise IndexError()

        return x, y

    def is_position_in_range(self, x: int, y: int) -> bool:
        """Indicates whether the specified position is within the grid bounds."""
        is_in_range = 0 <= x < self.width and 0 <= y < self.height

        return is_in_range

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
        """Returns a string representation of the grid."""
        def item_str(item): return str(item or ' ').ljust(self._justify)

        result = '\n'.join(
            ' '.join(item_str(item) for item in row) for row in self.get_rows()
        )

        return result

    @classmethod
    def from_data(cls, *kargs: List[T], justify: int = 1) -> 'SparseGrid[T]':
        """Creates a sparse grid from a 2-deminsiomal list."""
        grid = cls(len(kargs[0]), len(kargs), justify)

        for x, y in grid.get_positions():
            grid[x, y] = kargs[y][x] if x < len(kargs[y]) else None

        return grid


class ClosedSparseGrid(SparseGrid[T]):
    """Represents a sparse grid with connected bounds."""

    def adjust_position(self, x: int, y: int) -> Tuple[int, int]:
        """Returns an adjusted position for a closed grid."""
        adjusted_position = x % self.width, y % self.height

        return adjusted_position

    def is_position_in_range(self, x: int, y: int) -> bool:
        """Always returns true since a grid is closed."""
        return True
