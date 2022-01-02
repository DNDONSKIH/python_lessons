# -*- coding: utf-8 -*-

import simple_draw as sd

# На основе кода из lesson_004/05_snowfall.py
# сделать модуль snowfall.py в котором реализовать следующие функции
#  создать_снежинки(N) - создает N снежинок
#  нарисовать_снежинки_цветом(color) - отрисовывает все снежинки цветом color
#  сдвинуть_снежинки() - сдвигает снежинки на один шаг
#  номера_достигших_низа_экрана() - выдает список номеров снежинок, которые вышли за границу экрана
#  удалить_снежинки(номера) - удаляет снежинки с номерами из списка
#
# В текущем модуле реализовать главный цикл падения снежинок,
# обращаясь ТОЛЬКО к функциям модуля snowfall

from snowfall import snowflake_init, draw_all, move_all, get_num_of_fallen, remove_snowflakes
from snowfall import screenheight

N = 123
snowflake_init(20)
while True:
    draw_all(sd.background_color)
    move_all()
    draw_all(sd.COLOR_WHITE)
    fallen = get_num_of_fallen()
    if len(fallen):
        draw_all(sd.background_color)
        remove_snowflakes(fallen)
        draw_all(sd.COLOR_WHITE)
        snowflake_init(len(fallen), y_offset=screenheight - 50)  # добавим снежинку сверху
    sd.sleep(0.2)
    if sd.user_want_exit():
        break

sd.pause()
