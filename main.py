import curses
import time
from game_of_life import Life


def main(screen):
    """Simulates The Game of Life in a terminal using curses."""
    curses.curs_set(0)
    curses.start_color()
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)

    width, height = screen.getmaxyx()[1] // 2, screen.getmaxyx()[0]

    for world in Life.of_random_world(width, height):
        screen.addstr(0, 0, str(world), curses.color_pair(1))
        screen.refresh()
        time.sleep(.25)


if __name__ == '__main__':
    print(curses.wrapper(main))
