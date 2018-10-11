import curses
import threading
import time


class Window:

    def __init__(self, array):
        self.thread_list = []
        self.cell_array = array

        threading.Thread(name="Window", target=self.wrapper_draw).start()
        threading.Thread(name="Update", target=self.wrapper_update).start()

    def wrapper_draw(self):
        self.thread_list.append(threading.current_thread())
        curses.wrapper(self.draw_window, self)

    def wrapper_update(self):
        self.thread_list.append(threading.current_thread())
        curses.wrapper(self.update_array, self)

    @staticmethod
    def draw_window(stdscr, self):
        k = 0
        cursor_x = 0
        cursor_y = 0

        # Clear and refresh the screen for a blank canvas
        stdscr.clear()
        stdscr.refresh()

        # Start colors in curses
        curses.start_color()
        curses.init_pair(1, curses.COLOR_CYAN, curses.COLOR_BLACK)
        curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
        curses.init_pair(3, curses.COLOR_BLACK, curses.COLOR_WHITE)

        # Loop where k is the last character pressed
        while k != ord('q'):
            # Initialization
            height, width = stdscr.getmaxyx()

            if k == curses.KEY_DOWN:
                cursor_y = cursor_y + 1
            elif k == curses.KEY_UP:
                cursor_y = cursor_y - 1
            elif k == curses.KEY_RIGHT:
                cursor_x = cursor_x + 1
            elif k == curses.KEY_LEFT:
                cursor_x = cursor_x - 1

            cursor_x = max(0, cursor_x)
            cursor_x = min(width - 1, cursor_x)

            cursor_y = max(0, cursor_y)
            cursor_y = min(height - 1, cursor_y)

            statusbarstr = "[q]Quit"

            # Centering calculations
            start_y = int((height // 2) - 2)

            # Rendering some text
            whstr = "Width: {}, Height: {}".format(width, height)
            stdscr.addstr(0, 0, whstr, curses.color_pair(1))

            # Render status bar
            stdscr.attron(curses.color_pair(3))
            stdscr.addstr(height - 1, 0, statusbarstr)
            stdscr.addstr(height - 1, len(statusbarstr), " " * (width - len(statusbarstr) - 1))
            stdscr.attroff(curses.color_pair(3))

            # Turning on attributes for title
            stdscr.attron(curses.color_pair(2))
            stdscr.attron(curses.A_BOLD)

            # Rendering title

            # Turning off attributes for title
            stdscr.attroff(curses.color_pair(2))
            stdscr.attroff(curses.A_BOLD)

            # Print rest of text
            stdscr.move(cursor_y, cursor_x)

            # Refresh the screen
            stdscr.refresh()

            # Wait for next input
            k = stdscr.getch()

    @staticmethod
    def update_array(stdscr, self):
        while self.thread_list[0].is_alive():
            stdscr.addstr(1, 2, "coucou", curses.color_pair(1))
            time.sleep(0.05)
