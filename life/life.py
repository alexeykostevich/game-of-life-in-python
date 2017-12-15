from typing import Any, Callable, Iterable, Generator
from life.universe import Universe


def originate_from(universe: Universe[Any], regenerate: Callable[[], Any]) -> Generator[Universe[Any], None, None]:
    """
    Returns a generator iterator that can be used to iterate through universe states.
    Any universe-like object with cells of any type can be passed.
    Cell values other than 'None' are considered as alive.
    """
    while True:
        next_universe = universe.empty()

        for x, y in universe.through():
            cell = universe[x, y]
            neibours = universe.neighbours_of(x, y)

            next_universe[x, y] = live(cell, neibours, regenerate)

        universe = next_universe

        yield next_universe


def live(cell: Any, neigbours: Iterable[Any], regenerate: Callable[[], Any]) -> Any:
    """
    Implements the logic of 'The Game of Life'.
    Cell values other than 'None' are considered as alive.
    Returns
    - the existing cell if survives
    - a new cell if regenerates
    - 'None' if dies
    """
    neigbours_alive = sum(neigbour is not None for neigbour in neigbours)

    if cell and (neigbours_alive < 2 or 3 < neigbours_alive):
        return None

    if cell is None and neigbours_alive == 3:
        return regenerate()

    return cell
