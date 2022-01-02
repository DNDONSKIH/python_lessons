# -*- coding: utf-8 -*-

# (цикл for)

import simple_draw as sd

rainbow_colors = (sd.COLOR_RED, sd.COLOR_ORANGE, sd.COLOR_YELLOW, sd.COLOR_GREEN,
                  sd.COLOR_CYAN, sd.COLOR_BLUE, sd.COLOR_PURPLE)

# Нарисовать радугу: 7 линий разного цвета толщиной 4 с шагом 5 из точки (50, 50) в точку (350, 450)

coord_from = [50, 50]
coord_to = [350, 450]
for i in range(7):
    point_from = sd.get_point(coord_from[0], coord_from[1])
    point_to = sd.get_point(coord_to[0], coord_to[1])
    coord_from[1] += 5
    coord_to[1] += 5
    sd.line(point_from, point_to, rainbow_colors[i], 4)

# Усложненное задание, делать по желанию.
# Нарисовать радугу дугами от окружности (cсм sd.circle) за нижним краем экрана,
# поэкспериментировать с параметрами, что бы было красиво

coord = [500, -100]

for i in range(7):
    point = sd.get_point(coord[0], coord[1])
    coord[1] += 20
    sd.circle(point, 200, rainbow_colors[i], 15)

sd.pause()
