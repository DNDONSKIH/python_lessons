# -*- coding: utf-8 -*-

import simple_draw as sd

sd.resolution = (1200, 600)

# Нарисовать пузырек - три вложенных окружностей с шагом 5 пикселей
point = sd.get_point(100, 100)
sd.circle(point, 5)
sd.circle(point, 10)
sd.circle(point, 15)


# Написать функцию рисования пузырька, принммающую 2 (или более) параметра: точка рисовании и шаг
def draw_bubble(point, step):
    radius = 20
    sd.circle(point, radius + step)
    sd.circle(point, radius + step * 2)
    sd.circle(point, radius + step * 3)


def draw_bubble_and_set_color(point, step, color):
    radius = 20
    sd.circle(point, radius + step, color)
    sd.circle(point, radius + step * 2, color)
    sd.circle(point, radius + step * 3, color)


# Нарисовать 10 пузырьков в ряд
for i in range(1, 11):
    point = sd.get_point(100*i, 100)
    draw_bubble(point, 3)

# Нарисовать три ряда по 10 пузырьков
for j in range(1, 4):
    for i in range(1, 11):
        point = sd.get_point(100*i, 200+100*j)
        draw_bubble(point, 3)

# Нарисовать 100 пузырьков в произвольных местах экрана случайными цветами
for _ in range(100):
    point = sd.random_point()
    color = sd.random_color()
    draw_bubble_and_set_color(point, 1, color)


sd.pause()
