# -*- coding: utf-8 -*-

import simple_draw as sd


def draw_face(x_pos, y_pos):
    color = sd.COLOR_WHITE
    point = sd.get_point(x_pos, y_pos)
    sd.circle(point, 30, color, 2)

    point_1 = sd.get_point(x_pos - 10, y_pos + 10)
    point_2 = sd.get_point(x_pos + 10, y_pos + 10)
    sd.circle(point_1, 5, color, 2)
    sd.circle(point_2, 5, color, 2)

    point_3 = sd.get_point(x_pos - 15, y_pos - 10)
    point_4 = sd.get_point(x_pos + 15, y_pos - 10)

    sd.line(point_3, point_4, color, 2)
