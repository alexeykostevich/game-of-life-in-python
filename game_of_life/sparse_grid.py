from typing import Generic, Iterable, TypeVar, Tuple


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

    def positions(self) -> Tuple[int, int]:
        """Returns a new iterator that can iterate over grid positions."""
        for y in range(self.height):
            for x in range(self.width):
                yield (x, y)

    def get_neighbours_for(self, x: int, y: int) -> Iterable[T]:
        """Returns a new iterator that can iterate over neighbours around the specified position."""
        yield self[x - 1, y + 1]
        yield self[x, y + 1]
        yield self[x + 1, y + 1]
        yield self[x + 1, y]
        yield self[x + 1, y - 1]
        yield self[x, y - 1]
        yield self[x - 1, y - 1]
        yield self[x - 1, y]

    def get_rows(self) -> Iterable[Iterable[T]]:
        """Returns a new iterator that can iterate over grid rows."""
        yield from ((self[x, y] for x in range(self.width)) for y in range(self.height))

    def get_columns(self) -> Iterable[Iterable[T]]:
        """Returns a new iterator that can iterate over grid columns."""
        yield from ((self[x, y] for y in range(self.height)) for x in range(self.width))

    def adjust_position(self, x: int, y: int) -> Tuple[int, int]:
        """Returns the grid position."""
        if 0 > x >= self.width or 0 > y >= self.height:
            raise IndexError()

        return x, y

    def __getitem__(self, position: Tuple[int, int]) -> T:
        """Returns a value for the specified position using self[x, y]."""
        adjusted_position = self.adjust_position(*position)
        item = self._data.get(adjusted_position, None)

        return item

    def __setitem__(self, position: Tuple[int, int], value: T):
        """Sets the value for the specified position using self[x, y]."""
        if value is None:
            return

        adjusted_position = self.adjust_position(*position)

        self._data[adjusted_position] = value

    def __str__(self) -> str:
        """Returns a string representation of the grid."""
        def item_str(item): return str(item or ' ').ljust(self._justify)

        result = '\n'.join(
            ' '.join(item_str(item) for item in row) for row in self.get_rows()
        )

        return result


class ClosedSparseGrid(SparseGrid[T]):
    """Represents a sparse grid with connected borders."""

    def adjust_position(self, x: int, y: int) -> Tuple[int, int]:
        """Returns an adjusted position for a closed grid."""
        adjusted_position = x % self.width, y % self.height

        return adjusted_position
