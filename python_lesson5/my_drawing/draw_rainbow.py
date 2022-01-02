# -*- coding: utf-8 -*-


import simple_draw as sd
import random as r


def draw_rainbow():
    rainbow_colors = (sd.COLOR_RED, sd.COLOR_ORANGE, sd.COLOR_YELLOW, sd.COLOR_GREEN,
                      sd.COLOR_CYAN, sd.COLOR_BLUE, sd.COLOR_PURPLE,
                      sd.COLOR_RED, sd.COLOR_ORANGE, sd.COLOR_YELLOW, sd.COLOR_GREEN,
                      sd.COLOR_CYAN, sd.COLOR_BLUE, sd.COLOR_PURPLE,
                      )

    radius = 800
    point = sd.get_point(450, 0)
    shift = r.randint(0, 7)
    for i in range(7):
        radius += 15
        sd.circle(point, radius, rainbow_colors[shift + i], 15)
