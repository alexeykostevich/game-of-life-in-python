import curses
import time
from life import Cell, ClosedWorld, Life


def main(screen):
    """Simulates 'The Game of Life' in a terminal using curses."""
    curses.curs_set(0)
    curses.start_color()
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)

    width, height = screen.getmaxyx()[1] // 2, screen.getmaxyx()[0]

    world = ClosedWorld.random(width, height, Cell.likely)
    life = Life(world)

    for world in life:
        screen.addstr(0, 0, str(world), curses.color_pair(1))
        screen.refresh()
        time.sleep(.25)


if __name__ == '__main__':
    print(curses.wrapper(main))
