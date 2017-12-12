from typing import Iterable
from .cell import Cell
from .world import World


class Life(object):
    def __init__(self, world: World):
        if world is None:
            raise ValueError('world does not exist.')

        self._world = world

    @property
    def world(self) -> World:
        return self._world

    def __iter__(self) -> World:
        while True:
            world = World(self.world.width, self.world.height)

            for x, y in self.world.positions():
                cell = self.world[x, y]
                neibours = self.world.get_neibours(x, y)

                world[x, y] = Life.next_cell(cell, neibours)

            self._world = world

            yield self.world

    @classmethod
    def of_world(cls, width: int, height: int):
        world = World.random(width, height)
        life = Life(world)

        return life

    @staticmethod
    def next_cell(cell: Cell, neigbours: Iterable[Cell]) -> Cell:
        neigbours_alive = sum(neigbour is not None for neigbour in neigbours)

        if cell and (neigbours_alive < 2 or 3 < neigbours_alive):
            return None

        if cell is None and neigbours_alive == 3:
            return Cell()

        return cell
