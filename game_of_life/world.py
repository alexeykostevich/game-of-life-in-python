from .cell import Cell
from .sparse_grid import InfiniteSparseGrid


class World(InfiniteSparseGrid[Cell]):
    def __init__(self, width: int, height: int):
        if width <= 3:
            raise ValueError('width is less than 3.')

        if height <= 3:
            raise ValueError('height is less than 3.')

        super().__init__(width, height)

    @classmethod
    def random(cls, width: int, height: int):
        world = cls(width, height)

        for x, y in world.positions():
            world[x, y] = Cell.likely()

        return world
