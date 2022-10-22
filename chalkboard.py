# Author: Xiaoxuan
# Date: 4/20/2021
# Purpose: simulate chalkboard

from CS1.cs1lib import *

old_x = None
old_y = None
curr_x = None
curr_y = None
mpressed = False
setup = False


def my_mmove(mx, my):
    global curr_x, curr_y
    curr_x = mx
    curr_y = my


def my_mpress(mx, my):
    global  mpressed
    mpressed = True


def my_mrelease(mx, my):
    global  mpressed
    mpressed = False


def set_background_black():
    set_clear_color(0, 0, 0)  # black
    clear()


def set_stroke_white():
    set_stroke_color(1, 1, 1)  # white


def my_kpress(value):
    if value.lower() == 'r':
        set_stroke_color(1, 0, 0)  # red
    if value.lower() == 'b':
        set_stroke_color(0, 0, 1)  # blue
    if value.lower() == 'g':
        set_stroke_color(0, 1, 0)  # green
    if value.lower() == 'y':
        set_stroke_color(1, 1, 0)  # yellow


def main_draw():
    global setup, old_x, old_y
    if not setup:
        set_background_black()
        set_stroke_white()
        set_stroke_width(2)
        setup = True
    if mpressed:
        draw_line(old_x, old_y, curr_x, curr_y)
    old_x = curr_x
    old_y = curr_y


start_graphics(main_draw, key_press=my_kpress, mouse_move=my_mmove, mouse_press=my_mpress, mouse_release=my_mrelease)
