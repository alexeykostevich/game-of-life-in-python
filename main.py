import curses
import time
from game_of_life import Life


def main(screen):
    width = screen.getmaxyx()[1] // 2
    height = screen.getmaxyx()[0]

    for world in Life.of_world(width, height):
        screen.addstr(0, 0, str(world), curses.color_pair(1))
        screen.refresh()
        time.sleep(.25)


if __name__ == '__main__':
    try:
        screen = curses.initscr()
        curses.curs_set(0)
        curses.start_color()
        curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)

        main(screen)
    except KeyboardInterrupt:
        curses.endwin()
