# -*- coding: utf-8 -*-

# (определение функций)
import simple_draw as sd
import random as r

rainbow_colors = (sd.COLOR_RED, sd.COLOR_ORANGE, sd.COLOR_YELLOW, sd.COLOR_GREEN,
                  sd.COLOR_CYAN, sd.COLOR_BLUE, sd.COLOR_PURPLE)
window_width = 500
window_height = 500
indent = 30
sd.resolution = (window_width, window_height)


# Написать функцию отрисовки смайлика в произвольной точке экрана
# Форма рожицы-смайлика на ваше усмотрение
# Параметры функции: кордината X, координата Y, цвет.
# Вывести 10 смайликов в произвольных точках экрана.

def draw_face(x_pos, y_pos, color):
    point = sd.get_point(x_pos, y_pos)
    sd.circle(point, 30, color, 2)

    point_1 = sd.get_point(x_pos - 10, y_pos + 10)
    point_2 = sd.get_point(x_pos + 10, y_pos + 10)
    sd.circle(point_1, 5, color, 2)
    sd.circle(point_2, 5, color, 2)

    point_3 = sd.get_point(x_pos - 15, y_pos - 10)
    point_4 = sd.get_point(x_pos + 15, y_pos - 10)
    point_5 = sd.get_point(x_pos + 10, y_pos - 20)
    point_6 = sd.get_point(x_pos - 10, y_pos - 20)

    sd.line(point_3, point_4, color, 2)
    sd.line(point_4, point_5, color, 2)
    sd.line(point_5, point_6, color, 2)
    sd.line(point_6, point_3, color, 2)


for i in range(10):
    x = r.randint(0 + indent, window_width - indent)
    y = r.randint(0 + indent, window_height - indent)
    col = rainbow_colors[i % len(rainbow_colors)]
    draw_face(x, y, col)
sd.pause()
