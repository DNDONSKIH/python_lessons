# -*- coding: utf-8 -*-

import simple_draw as sd
import random as r

screenwidth = 1200
screenheight = 600
sd.resolution = (screenwidth, screenheight)


_snowflake_list = []
N = 1234

def snowflake_init(n, y_offset=0):
    for _ in range(n):
        # координата x, координата y, длина луча
        snowflake = [r.randint(0, screenwidth), r.randint(y_offset, screenheight), r.randint(10, 30)]
        _snowflake_list.append(snowflake)


def draw_all(color):
    for sf in _snowflake_list:
        point = sd.get_point(sf[0], sf[1])
        sd.snowflake(center=point, length=sf[2], color=color)


def move_all():
    for i in range(len(_snowflake_list)):
        if _snowflake_list[i][1] > 30:
            _snowflake_list[i][0] += r.randint(-10, 10)
            _snowflake_list[i][1] -= r.randint(0, 10)


def get_num_of_fallen():
    result = []
    for i in range(len(_snowflake_list)):
        if _snowflake_list[i][1] <= 30:
            result.append(i)
    return result


def remove_snowflakes(nums_to_del):
    for num in nums_to_del:
        _snowflake_list.pop(num)
