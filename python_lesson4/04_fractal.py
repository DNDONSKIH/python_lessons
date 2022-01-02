# -*- coding: utf-8 -*-

import simple_draw as sd
import random as r

# 1) Написать функцию draw_branches, которая должна рисовать две ветви дерева из начальной точки
# Функция должна принимать параметры:
# - точка начала рисования,
# - угол рисования,
# - длина ветвей,
# Отклонение ветвей от угла рисования принять 30 градусов,

# def draw_branches(point, angle, length):
#     v1 = sd.get_vector(start_point=point, angle=angle + 30, length=length, width=3)
#     v2 = sd.get_vector(start_point=point, angle=angle - 30, length=length, width=3)
#     v1.draw()
#     v2.draw()
#     # return v1.end_point


sd.resolution = (1200, 600)


# 2) Сделать draw_branches рекурсивной
# - добавить проверку на длину ветвей, если длина меньше 10 - не рисовать
# - вызывать саму себя 2 раза из точек-концов нарисованных ветвей,
#   с параметром "угол рисования" равным углу только что нарисованной ветви,
#   и параметром "длинна ветвей" в 0.75 меньшей чем длина только что нарисованной ветви


# def draw_branches(point, angle, length):
#     if length < 15:
#         return
#     else:
#         angle_delta = 20
#         length_delta = .75
#         angle_left = angle - angle_delta
#         angle_right = angle + angle_delta
#         v1 = sd.get_vector(start_point=point, angle=angle_left, length=length, width=1)
#         v2 = sd.get_vector(start_point=point, angle=angle_right, length=length, width=1)
#         v1.draw()
#         v2.draw()
#
#         next_point = v1.end_point
#         next_length = length * length_delta
#         next_angle = angle_left - angle_delta
#         draw_branches(point=next_point, angle=next_angle, length=next_length)
#         next_angle = angle_left + angle_delta
#         draw_branches(point=next_point, angle=next_angle, length=next_length)
#
#         next_point = v2.end_point
#         next_length = length * length_delta
#         next_angle = angle_right - angle_delta
#         draw_branches(point=next_point, angle=next_angle, length=next_length)
#         next_angle = angle_right + angle_delta
#         draw_branches(point=next_point, angle=next_angle, length=next_length)


# 3) первоначальный вызов:
# root_point = get_point(300, 30)
# draw_bunches(start_point=root_point, angle=90, length=100)

# Пригодятся функции
# sd.get_point()
# sd.get_vector()
# Возможный результат решения см lesson_004/results/exercise_04_fractal_01.jpg

# можно поиграть -шрифтами- цветами и углами отклонения


# 4) Усложненное задание (делать по желанию)
# - сделать рандомное отклонение угла ветвей в пределах 40% от 30-ти градусов
# - сделать рандомное отклонение длины ветвей в пределах 20% от коэффициента 0.75
# Возможный результат решения см lesson_004/results/exercise_04_fractal_02.jpg

# Пригодятся функции
# sd.random_number()

def draw_branches(point, angle, length):
    if length < 5:
        return
    else:

        angle_delta = r.randint(0, 25)
        length_delta = r.uniform(0.6, 0.9)
        angle_left = angle + angle_delta
        angle_right = angle - angle_delta
        v1 = sd.get_vector(start_point=point, angle=angle_left, length=length, width=1)
        v2 = sd.get_vector(start_point=point, angle=angle_right, length=length, width=1)
        v1.draw()
        v2.draw()

        length_delta = r.uniform(0.6, 0.9)
        next_point = v1.end_point
        next_length = length * length_delta
        next_angle = angle_left + r.randint(0, 20)
        draw_branches(point=next_point, angle=next_angle, length=next_length)

        length_delta = r.uniform(0.6, 0.9)
        next_point = v2.end_point
        next_length = length * length_delta
        next_angle = angle_right - r.randint(0, 20)
        draw_branches(point=next_point, angle=next_angle, length=next_length)




root_point = sd.get_point(600, 30)
draw_branches(point=root_point, angle=90, length=100)

sd.pause()
