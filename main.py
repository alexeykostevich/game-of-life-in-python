import curses
import time
from game_of_life import Life, World


def main(screen):
    height, width = screen.getmaxyx()

    for world in Life.of_world(width // 2, height):
        render(world, screen)
        time.sleep(.25)


def render(world: World, screen):
    screen.addstr(0, 0, str(world), curses.color_pair(1))
    screen.refresh()


if __name__ == '__main__':
    try:
        screen = curses.initscr()
        curses.curs_set(0)
        curses.start_color()
        curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)

        main(screen)
    except KeyboardInterrupt:
        curses.endwin()
