import curses
import math
import time
from life import Cell, originate_from, WrappedUniverse


def main(screen):
    """Simulates 'The Game of Life' in a terminal using curses."""
    curses.curs_set(0)
    curses.start_color()
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    screen_height, screen_width = screen.getmaxyx()

    width, height = math.ceil(screen_width / 2), screen_height

    universe = WrappedUniverse.random(width, height, Cell.likely)
    life = originate_from(universe, regenerate=Cell)

    for universe in life:
        screen.addstr(0, 0, str(universe), curses.color_pair(1))
        screen.refresh()
        time.sleep(.25)


if __name__ == '__main__':
    print(curses.wrapper(main))
