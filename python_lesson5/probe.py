# -*- coding: utf-8 -*-

import simple_draw as sd
import random as rnd

screen_x = 1200
screen_y = 600

sd.resolution = (screen_x, screen_y)

# На основе кода из практической части реализовать снегопад:
# - создать списки данных для отрисовки N снежинок
# - нарисовать падение этих N снежинок
# - создать список рандомных длинн лучей снежинок (от 10 до 100) и пусть все снежинки будут разные

N = 20

snowflakes_list = []
for _ in range(N):
    snowflakes_list.append(
        [rnd.randint(0, screen_x), rnd.randint(screen_y - 200, screen_y + 400), rnd.randint(10, 100), True])
    #   Координата снежинки х         Координата снежинки screen_y                Длина лучиков     Снежинка падает
    #                                                                                               или уже упала


# print(snowflakes_list)


def snowflake_fall(snowflakes):
    """Лагает как тварь где-то после ~40 снежинок"""
    while True:
        sd.clear_screen()
        for snowflake in snowflakes:
            point = sd.get_point(snowflake[0], snowflake[1])
            sd.snowflake(center=point, length=snowflake[2], color=sd.COLOR_WHITE)
            if snowflake[3]:
                if snowflake[1] <= 0:
                    snowflake[1] = 0
                    snowflake[3] = False
                    snowflakes_list.append(
                        [rnd.randint(0, screen_x), rnd.randint(screen_y - 200, screen_y + 400), rnd.randint(10, 100),
                         True])
                else:
                    snowflake[1] -= 5
                    snowflake[0] += rnd.randint(-5, 5)
        sd.sleep(0.05)
        if sd.user_want_exit():
            break


snowflake_fall(snowflakes_list)
# Пригодятся функции
# sd.get_point()
# sd.snowflake()
# sd.sleep()
# sd.random_number()
# sd.user_want_exit()

# y = 500
# while y > 0:
#     sd.clear_screen()
#     point = sd.get_point(300, y)
#     sd.snowflake(center=point, length=40, color=sd.COLOR_WHITE)
#     y -= 5
#     sd.sleep(0.05)
#     if sd.user_want_exit():
#         break

sd.pause()

# подсказка! для ускорения отрисовки можно
#  - убрать clear_screen()
#  - в начале рисования всех снежинок вызвать sd.start_drawing()
#  - на старом месте снежинки отрисовать её же, но цветом sd.background_color
#  - сдвинуть снежинку
#  - отрисовать её цветом sd.COLOR_WHITE на новом месте
#  - после отрисовки всех снежинок, перед sleep(), вызвать sd.finish_drawing()


# 4) Усложненное задание (делать по желанию)
# - сделать рандомные отклонения вправо/влево при каждом шаге
# - сделать сугоб внизу экрана - если снежинка долетает до низа, оставлять её там,
#   и добавлять новую снежинку
# Результат решения см https://youtu.be/XBx0JtxHiLg