from typing import Any, Callable, Iterable
from life.universe import Universe


class Life(object):
    """
    Represents life of 'The Game of Life'.
    The life can use any universe-like object with cells of any type.
    Any value other than 'None' is considered as alive cell.
    """

    @classmethod
    def originate_from(cls, universe: Universe[Any], regenerate: Callable[[], Any]) -> Universe[Any]:
        """Returns a new iterator that can iterate over universe states."""
        while True:
            next_universe = universe.empty()

            for x, y in universe.through():
                cell = universe[x, y]
                neibours = universe.neighbours_of(x, y)

                next_universe[x, y] = Life.next_cell(cell, neibours, regenerate)

            universe = next_universe

            yield next_universe

    @staticmethod
    def next_cell(cell, neigbours: Iterable[Any], regenerate: Callable[[], Any]) -> Any:
        """Returns the survivied cell, a regenerated cell or none for the next generation."""
        neigbours_alive = sum(neigbour is not None for neigbour in neigbours)

        if cell and (neigbours_alive < 2 or 3 < neigbours_alive):
            return None

        if cell is None and neigbours_alive == 3:
            return regenerate()

        return cell
