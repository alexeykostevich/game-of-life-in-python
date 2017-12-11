from typing import Callable, Generic, Type, TypeVar, Tuple


T = TypeVar('T')


class Grid(Generic[T]):
    def __init__(self, width: int, height: int):
        if width <= 0:
            raise ValueError('width is zero or a negative number.')

        if height <= 0:
            raise ValueError('height is zero or a negative number.')

        self._data = [[None for y in range(height)] for x in range(width)]

    @property
    def width(self) -> int:
        return len(self._data)

    @property
    def height(self) -> int:
        return len(self._data[0])

    def __iter__(self) -> Tuple[int, int]:
        for y in range(self.height):
            for x in range(self.width):
                yield (x, y)

    def __getitem__(self, position: Tuple[int, int]) -> T:
        x, y = position

        if 0 > x >= self.width or 0 > y >= self.height:
            raise IndexError()

        return self._data[x][y]

    def __setitem__(self, position: Tuple[int, int], value: T):
        x, y = position

        if 0 > x >= self.width or 0 > y >= self.height:
            raise IndexError()

        self._data[x][y] = value

    def __str__(self) -> str:
        result = ''

        for y in range(self.height):
            for x in range(self.width):
                result += '{:5}'.format(self[x, y])

            result += '\n'

        return result

    @classmethod
    def random(cls, width: int, height: int, random: Callable[[int, int], T]):
        grid = cls(width, height)

        for x, y in grid:
            grid[x, y] = random(x, y)

        return grid
