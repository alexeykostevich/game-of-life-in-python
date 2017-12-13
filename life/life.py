from typing import Callable, Iterable
from life.cell import Cell
from life.world import World


class Life(object):
    """Represents 'The Game of Life'."""

    def __init__(self, world: World[Cell]):
        if world is None:
            raise ValueError('world does not exist.')

        self._world = world

    @property
    def world(self) -> World[Cell]:
        """Returns the current state of the world."""
        return self._world

    def __iter__(self) -> World[Cell]:
        """Returns a new iterator that can iterate over world states."""
        while True:
            world = self.world.empty_from(self.world)

            for x, y in self.world.get_positions():
                cell = self.world[x, y]
                neibours = self.world.get_neighbours_of(x, y)

                world[x, y] = Life.simulate_for(cell, neibours)

            self._world = world

            yield self.world

    @staticmethod
    def simulate_for(cell: Cell, neigbours: Iterable[Cell]) -> Cell:
        """Returns the survivied cell, a regenerated cell or nothing for a new world."""
        neigbours_alive = sum(neigbour is not None for neigbour in neigbours)

        if cell and (neigbours_alive < 2 or 3 < neigbours_alive):
            return None

        if cell is None and neigbours_alive == 3:
            return Cell()

        return cell
