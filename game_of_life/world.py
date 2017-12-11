from typing import Tuple
from cell import Cell
from sparse_grid import InfiniteSparseGrid


class World(object):
    def __init__(self, width: int, height: int):
        if width <= 3:
            raise ValueError('width is less than 3.')

        if height <= 3:
            raise ValueError('height is less than 3.')

        self._grid = InfiniteSparseGrid(width, height)

    @property
    def width(self) -> int:
        return self._grid.width

    @property
    def height(self) -> int:
        return self._grid.height

    def positions(self) -> Tuple[int, int]:
        return self._grid.positions()

    def __getitem__(self, position: Tuple[int, int]) -> Cell:
        return self._grid[position]

    def __setitem__(self, position: Tuple[int, int], value: Cell):
        self._grid[position] = value

    def __str__(self) -> str:
        return self._grid.__str__()

    @classmethod
    def random(cls, width: int, height: int):
        world = cls(width, height)

        for x, y in world.positions():
            world[x, y] = Cell.likely()

        return world
