from typing import Any, Callable, Iterable, Generator
from .universe import Universe


def originate_from(universe: Universe[Any], regenerate: Callable[[], Any]) -> Generator[Universe[Any], None, None]:
    """
    Returns a generator iterator that can be used to iterate through universe states.
    The function can handle any universe-like object of any cells. Any cell except of 'None' is considered as alive.
    """
    while True:
        next_universe = universe.empty_copy()

        for x, y in universe.through():
            cell = universe[x, y]
            neibours = universe.neighbours_of(x, y)

            next_universe[x, y] = live(cell, neibours, regenerate)

        universe = next_universe

        yield next_universe


def live(cell: Any, neigbours: Iterable[Any], regenerate: Callable[[], Any]) -> Any:
    """
    Implements the logic of 'The Game of Life'.
    Any cell except of 'None' is considered as alive.
    Returns the existing cell if it survives, a new cell if it regenerates or 'None' if if dies.
    """
    neigbours_alive = sum(neigbour is not None for neigbour in neigbours)

    if cell is not None and (neigbours_alive < 2 or 3 < neigbours_alive):
        return None

    if cell is None and neigbours_alive == 3:
        return regenerate()

    return cell
