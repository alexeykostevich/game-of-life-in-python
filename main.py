import curses
import time
from game_of_life import Life


def main(screen):
    curses.curs_set(0)
    curses.start_color()
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)

    height, width = screen.getmaxyx()

    for world in Life.of_world(width // 2, height):
        screen.addstr(0, 0, str(world), curses.color_pair(1))
        screen.refresh()
        time.sleep(.25)


if __name__ == '__main__':
    print(curses.wrapper(main))
