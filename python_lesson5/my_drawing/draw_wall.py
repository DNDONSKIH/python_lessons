# -*- coding: utf-8 -*-

# (цикл for)
import simple_draw as sd


def draw_wall(x=0, y=0, width=200, height=200):
    wall_width = width
    wall_height = height
    brick_width = 100
    brick_height = 50
    brick_rows = int(wall_height / brick_height)
    brick_cols = int(wall_width / brick_width)

    horizontal_start_point = [x, y]
    vertical_start_point = [x, y]

    v0 = sd.get_vector(start_point=sd.get_point(*[x, y]), angle=90, length=wall_height, width=2)
    v0.draw()
    v0 = sd.get_vector(start_point=v0.end_point, angle=0, length=wall_width, width=2)
    v0.draw()
    v0 = sd.get_vector(start_point=v0.end_point, angle=-90, length=wall_height, width=2)
    v0.draw()

    for i in range(brick_rows):
        point = sd.get_point(*horizontal_start_point)
        v1 = sd.get_vector(start_point=point, angle=0, length=wall_width, width=2)
        v1.draw()

        vertical_start_point[1] = horizontal_start_point[1]
        if i % 2 != 0:
            vertical_start_point[0] = x + int(brick_width / 2)
        else:
            vertical_start_point[0] = x

        point = v1.start_point
        for j in range(brick_cols):
            point = sd.get_point(*vertical_start_point)
            v2 = sd.get_vector(start_point=point, angle=90, length=brick_height, width=2)
            v2.draw()
            vertical_start_point[0] += brick_width

        horizontal_start_point[1] += brick_height


# draw_wall(x=10, y=10, width=500, height=500)
# sd.pause()
