# -*- coding: utf-8 -*-

import simple_draw as sd
import random as r

# На основе кода из практической части реализовать снегопад:
# - создать списки данных для отрисовки N снежинок
# - нарисовать падение этих N снежинок
# - создать список рандомных длинн лучей снежинок (от 10 до 100) и пусть все снежинки будут разные

N = 20
screenwidth = 1200
screenheight = 600
sd.resolution = (screenwidth, screenheight)

# Пригодятся функции
# sd.get_point()
# sd.snowflake()
# sd.sleep()
# sd.random_number()
# sd.user_want_exit()


snowflake_list = []
wind = 0


def draw_all(color):
    for _snowflake in snowflake_list:
        point = sd.get_point(_snowflake[0], _snowflake[1])
        sd.snowflake(center=point, length=_snowflake[2], color=color)


def move_all():
    for i in range(len(snowflake_list)):

        if snowflake_list[i][1] > 30:
            snowflake_list[i][0] += r.randint(-10 + wind, 10 + wind)
            snowflake_list[i][1] -= r.randint(0, 10)
        elif not snowflake_list[i][3]:
            pass
            snowflake_list[i][3] = True
            snowflake = [r.randint(0, screenwidth), screenheight, r.randint(10, 60), False]
            snowflake_list.append(snowflake)
        else:
            pass


def snowflake_init():
    for _ in range(N):
        # координаты x, y, длина луча, признак добавления новой снежинки
        snowflake = [r.randint(0, screenwidth), r.randint(0, screenheight), r.randint(10, 60), False]
        snowflake_list.append(snowflake)




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



snowflake_init()

while True:
    sd.clear_screen()
    # draw_all(sd.background_color)
    move_all()
    draw_all(sd.COLOR_WHITE)
    pass
    sd.sleep(0.1)
    if sd.user_want_exit():
        break

sd.pause()