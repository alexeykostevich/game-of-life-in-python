import curses
import time
from life import Cell, originate_from, WrappedUniverse


def main(screen):
    """Simulates 'The Game of Life' in a terminal using curses."""
    curses.curs_set(0)
    curses.start_color()
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)

    height, width = screen.getmaxyx()[0], screen.getmaxyx()[1] // 2

    universe = WrappedUniverse.random(width, height, Cell.likely)
    life = originate_from(universe, regenerate=Cell)

    for universe in life:
        screen.addstr(0, 0, str(universe), curses.color_pair(1))
        screen.refresh()
        time.sleep(.25)


if __name__ == '__main__':
    print(curses.wrapper(main))
