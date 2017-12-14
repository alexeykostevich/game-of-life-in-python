import curses
import time
from life import Cell, ClosedWorld, Life


def main(screen):
    """Simulates 'The Game of Life' in a terminal using curses."""
    curses.curs_set(0)
    curses.start_color()
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)

    height, width,  = screen.getmaxyx()

    world = ClosedWorld.random(width - 1, height, Cell.likely)
    life = Life.originate_from(world, Cell)

    for world in life:
        screen.addstr(0, 0, str(world), curses.color_pair(1))
        screen.refresh()
        time.sleep(.25)


if __name__ == '__main__':
    print(curses.wrapper(main))
