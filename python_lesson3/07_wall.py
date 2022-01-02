# -*- coding: utf-8 -*-

# (цикл for)
import simple_draw as sd

# Нарисовать стену из кирпичей. Размер кирпича - 100х50
# Использовать вложенные циклы for

window_width = 1000
window_height = 500
brick_width = 100
brick_height = 50
sd.resolution = (window_width, window_height)
sd.background_color = sd.COLOR_ORANGE

coord_from = [0, 0]
coord_to = [window_width, 0]

coord_short_side_from = [0, 0]
coord_short_side_to = [0, brick_height]

for i in range(10):
    point_from = sd.get_point(coord_from[0], coord_from[1])
    point_to = sd.get_point(coord_to[0], coord_to[1])
    sd.line(point_from, point_to, sd.COLOR_BLACK, 2)
    coord_from[1] += brick_height
    coord_to[1] += brick_height

    for j in range(10):
        point_from = sd.get_point(coord_short_side_from[0], coord_short_side_from[1])
        point_to = sd.get_point(coord_short_side_to[0], coord_short_side_to[1])
        coord_short_side_from[0] += brick_width
        coord_short_side_to[0] += brick_width
        sd.line(point_from, point_to, sd.COLOR_BLACK, 2)

    coord_short_side_from[1] += brick_height
    coord_short_side_to[1] += brick_height

    if i % 2 != 0:
        coord_short_side_from[0] = 0
        coord_short_side_to[0] = 0
    else:
        coord_short_side_from[0] = int(brick_width/2)
        coord_short_side_to[0] = int(brick_width/2)


sd.pause()
