# -*- coding: utf-8 -*-

import simple_draw as sd
import random as r

screenwidth = 1200
screenheight = 600
sd.resolution = (screenwidth, screenheight)


# Шаг 1: Реализовать падение снежинки через класс. Внести в методы:
#  - создание снежинки с нужными параметрами
#  - отработку изменений координат
#  - отрисовку


class Snowflake:
    def __init__(self, x, y, length):
        self._x = x
        self._y = y
        self._length = length

    def clear_previous_picture(self):
        point = sd.get_point(self._x, self._y)
        sd.snowflake(center=point, length=self._length, color=sd.background_color)

    def draw(self):
        point = sd.get_point(self._x, self._y)
        if self._y >= 0:
            sd.snowflake(center=point, length=self._length, color=sd.COLOR_WHITE)

    def can_fall(self):
        if self._y < 0:
            return False
        else:
            return True

    def move(self):
        self._x += r.randint(-10, 10)
        self._y -= r.randint(0, 10)

    # flake = Snowflake(r.randint(0, screenwidth), screenheight, r.randint(10, 30))
    #
    # while True:
    #     flake.clear_previous_picture()
    #     flake.move()
    #     flake.draw()
    #     if not flake.can_fall():
    #         break
    #     sd.sleep(0.1)
    #     if sd.user_want_exit():
    #         break


def get_flakes(count):
    result = []
    for _ in range(count):
        result.append(Snowflake(r.randint(0, screenwidth), r.randint(0, screenheight), r.randint(10, 30)))
    return result


# шаг 2: создать снегопад - список объектов Снежинка в отдельном списке, обработку примерно так:
flakes = get_flakes(count=30)  # создать список снежинок


def get_fallen_flakes():
    count = 0
    for flk in flakes:
        if not flk.can_fall():
            count += 1
            flakes.remove(flk)
    return count


def append_flakes(count):
    for _ in range(count):
        flakes.append(Snowflake(r.randint(0, screenwidth), screenheight, r.randint(10, 30)))


while True:
    for flake in flakes:
        flake.clear_previous_picture()
        flake.move()
        flake.draw()
    fallen_flakes = get_fallen_flakes()  # подчитать сколько снежинок уже упало
    if fallen_flakes:
        append_flakes(count=fallen_flakes)  # добавить еще сверху
    sd.sleep(0.1)
    if sd.user_want_exit():
        break

sd.pause()
