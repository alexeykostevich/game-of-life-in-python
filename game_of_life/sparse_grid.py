from typing import Generic, Iterable, TypeVar, Tuple


T = TypeVar('T')


class SparseGrid(Generic[T]):
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
        return self._width

    @property
    def height(self) -> int:
        return self._height

    def positions(self) -> Tuple[int, int]:
        for y in range(self.height):
            for x in range(self.width):
                yield (x, y)

    def get_neibours(self, x: int, y: int) -> Iterable[T]:
        yield self[x - 1, y + 1]
        yield self[x, y + 1]
        yield self[x + 1, y + 1]
        yield self[x + 1, y]
        yield self[x + 1, y - 1]
        yield self[x, y - 1]
        yield self[x - 1, y - 1]
        yield self[x - 1, y]

    def rows(self) -> Iterable[Iterable[T]]:
        yield from ((self[x, y] for x in range(self.width)) for y in range(self.height))

    def columns(self) -> Iterable[Iterable[T]]:
        yield from ((self[x, y] for y in range(self.height)) for x in range(self.width))

    def adjust_position(self, x: int, y: int) -> Tuple[int, int]:
        if 0 > x >= self.width or 0 > y >= self.height:
            raise IndexError()

        return x, y

    def __getitem__(self, position: Tuple[int, int]) -> T:
        adjusted_position = self.adjust_position(*position)

        return self._data.get(adjusted_position, None)

    def __setitem__(self, position: Tuple[int, int], value: T):
        if value is None:
            return

        adjusted_position = self.adjust_position(*position)

        self._data[adjusted_position] = value

    def __str__(self) -> str:
        result = '\n'.join(
            ' '.join(str(item or ' ').rjust(self._justify) for item in row) for row in self.rows()
        )

        return result


class ClosedSparseGrid(SparseGrid[T]):
    def adjust_position(self, x: int, y: int) -> Tuple[int, int]:
        return x % self.width, y % self.height
