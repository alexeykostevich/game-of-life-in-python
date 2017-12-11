from typing import Callable, Generic, TypeVar, Tuple


T = TypeVar('T')


class SparseGrid(Generic[T]):
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
        return self._width

    @property
    def height(self) -> int:
        return self._height

    def __iter__(self) -> Tuple[int, int]:
        for y in range(self.height):
            for x in range(self.width):
                yield (x, y)

    def __getitem__(self, position: Tuple[int, int]) -> T:
        x, y = position

        if 0 > x >= self.width or 0 > y >= self.height:
            raise IndexError()

        return self._data.get(position, None)

    def __setitem__(self, position: Tuple[int, int], value: T):
        x, y = position

        if 0 > x >= self.width or 0 > y >= self.height:
            raise IndexError()

        self._data[position] = value

    def __str__(self) -> str:
        result = ''

        for y in range(self.height):
            items = [str(self[x, y]) for x in range(self.width)]
            result += ' '.join(items) + '\n'

        return result

    @classmethod
    def random(cls, width: int, height: int, random: Callable[[int, int], T]):
        grid = cls(width, height)

        for x, y in grid:
            grid[x, y] = random(x, y)

        return grid
