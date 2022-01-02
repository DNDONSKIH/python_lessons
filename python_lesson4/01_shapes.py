# -*- coding: utf-8 -*-

import simple_draw as sd


# Часть 1.
# Написать функции рисования равносторонних геометрических фигур:
# - треугольника
# - квадрата
# - пятиугольника
# - шестиугольника
# Все функции должны принимать 3 параметра:
# - точка начала рисования
# - угол наклона
# - длина стороны
#
# Использование копи-пасты - обязательно! Даже тем кто уже знает про её пагубность. Для тренировки.
# Как работает копипаста:
#   - одну функцию написали,
#   - копипастим её, меняем название, чуть подправляем код,
#   - копипастим её, меняем название, чуть подправляем код,
#   - и так далее.
# В итоге должен получиться ПОЧТИ одинаковый код в каждой функции

# Пригодятся функции
# sd.get_point()
# sd.get_vector()
# sd.line()
# Результат решения см lesson_004/results/exercise_01_shapes.jpg

sd.resolution = (700, 700)

def draw_triangle(point, angle, side_len):
    v1 = sd.get_vector(start_point=point, angle=angle, length=side_len, width=1)
    v2 = sd.get_vector(start_point=v1.end_point, angle=angle + 120, length=side_len, width=1)
    v3 = sd.get_vector(start_point=v2.end_point, angle=angle + 240, length=side_len, width=1)

    v1.draw()
    v2.draw()
    v3.draw()


def draw_rectangle(point, angle, side_len):
    v1 = sd.get_vector(start_point=point, angle=angle, length=side_len, width=1)
    v2 = sd.get_vector(start_point=v1.end_point, angle=angle + 90, length=side_len, width=1)
    v3 = sd.get_vector(start_point=v2.end_point, angle=angle + 180, length=side_len, width=1)
    v4 = sd.get_vector(start_point=v3.end_point, angle=angle + 270, length=side_len, width=1)
    v1.draw()
    v2.draw()
    v3.draw()
    v4.draw()


def draw_pentagon(point, angle, side_len):
    v1 = sd.get_vector(start_point=point, angle=angle, length=side_len, width=1)
    v2 = sd.get_vector(start_point=v1.end_point, angle=angle + 72 * 1, length=side_len, width=1)
    v3 = sd.get_vector(start_point=v2.end_point, angle=angle + 72 * 2, length=side_len, width=1)
    v4 = sd.get_vector(start_point=v3.end_point, angle=angle + 72 * 3, length=side_len, width=1)
    v1.draw()
    v2.draw()
    v3.draw()
    v4.draw()
    sd.line(start_point=v4.end_point, end_point=v1.start_point, width=1)


def draw_octagon(point, angle, side_len):
    v1 = sd.get_vector(start_point=point, angle=angle, length=side_len, width=1)
    v2 = sd.get_vector(start_point=v1.end_point, angle=angle + 60 * 1, length=side_len, width=1)
    v3 = sd.get_vector(start_point=v2.end_point, angle=angle + 60 * 2, length=side_len, width=1)
    v4 = sd.get_vector(start_point=v3.end_point, angle=angle + 60 * 3, length=side_len, width=1)
    v5 = sd.get_vector(start_point=v4.end_point, angle=angle + 60 * 4, length=side_len, width=1)
    v1.draw()
    v2.draw()
    v3.draw()
    v4.draw()
    v5.draw()
    sd.line(start_point=v5.end_point, end_point=v1.start_point, width=1)


point_0 = sd.get_point(100, 100)
draw_triangle(point_0, 0, 50)

point_0 = sd.get_point(200, 200)
draw_rectangle(point_0, 0, 50)

point_0 = sd.get_point(300, 300)
draw_pentagon(point_0, 0, 50)

point_0 = sd.get_point(400, 400)
draw_octagon(point_0, 0, 50)


# Часть 1-бис.
# Попробуйте прикинуть обьем работы, если нужно будет внести изменения в этот код.
# Скажем, связывать точки не линиями, а дугами. Или двойными линиями. Или рисовать круги в угловых точках. Или...
# А если таких функций не 4, а 44?

# Часть 2 (делается после зачета первой части)
#
# Надо сформировать функцию, параметризированную в местах где была "небольшая правка".
# Это называется "Выделить общую часть алгоритма в отдельную функцию"
# Потом надо изменить функции рисования конкретных фигур - вызывать общую функцию вместо "почти" одинакового кода.
#
# В итоге должно получиться:
#   - одна общая функция со множеством параметров,
#   - все функции отрисовки треугольника/квадрата/етс берут 3 параметра и внутри себя ВЫЗЫВАЮТ общую функцию.
#
# Не забудте в этой общей функции придумать, как устранить разрыв
#   в начальной/конечной точках рисуемой фигуры (если он есть)

# Часть 2-бис.
# А теперь - сколько надо работы что бы внести изменения в код? Выгода на лицо :)
# Поэтому среди программистов есть принцип D.R.Y. https://clck.ru/GEsA9
# Будьте ленивыми, не используйте копи-пасту!
def draw_lines(*args):
    for arg in args:
        sd.line(start_point=arg[0], end_point=arg[1], width=1)


def draw_shape(point, angle, side_len, shape_type):
    """shape_type == 0 - треугольник
       shape_type == 1 - квадрат
       shape_type == 2 - пятиугольник
       shape_type == 3 - шестиугольник
    """
    if not 0 <= shape_type <= 3:
        print("Invalid shape type")
        return

    angle_dict = {0: 120, 1: 90, 2: 72, 3: 60}
    iter_count = shape_type + 3
    list_of_coords = []

    _point = point
    _angle = angle
    for _ in range(iter_count):
        v = sd.get_vector(start_point=_point, angle=_angle, length=side_len, width=1)
        _point = v.end_point
        _angle += angle_dict[shape_type]
        list_of_coords.append([v.start_point, v.end_point])

    list_of_coords[-1][1] = list_of_coords[0][0] #замыкаем линию

    draw_lines(*list_of_coords)


point_1 = sd.get_point(100, 200)
draw_shape(point_1, 0, 70, 0)
point_1 = sd.get_point(100, 300)
draw_shape(point_1, 0, 70, 1)
point_1 = sd.get_point(100, 400)
draw_shape(point_1, 0, 70, 2)
point_1 = sd.get_point(100, 500)
draw_shape(point_1, 0, 70, 3)

sd.pause()
