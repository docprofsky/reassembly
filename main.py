from __future__ import print_function
from subprocess import call
from sys import version_info
import curses
import curses.textpad
from time import sleep


def get_input(prompt):
    if version_info < (3, 0):
        return raw_input(prompt)
    else:
        return input(prompt)

cfile = get_input("Enter C file name: ")
afile = get_input("Enter Assembly output file name: ")

print("Compiling to Assembly...")

call(["gcc", "-S", "-O0", cfile, "-o", afile])

stdscr = curses.initscr()
curses.start_color()
curses.noecho()
curses.cbreak()
stdscr.keypad(1)

stdscr.addstr("teststr")
stdscr.refresh()

sleep(1)

curses.nocbreak()
stdscr.keypad(0)
curses.echo()
curses.endwin()
