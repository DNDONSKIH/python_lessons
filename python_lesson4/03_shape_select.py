# -*- coding: utf-8 -*-

import simple_draw as sd


# Запросить у пользователя желаемую фигуру посредством выбора из существующих
#   вывести список всех фигур с номерами и ждать ввода номера желаемой фигуры.
# и нарисовать эту фигуру в центре экрана

# Код функций из упр lesson_004/02_global_color.py скопировать сюда
# Результат решения см lesson_004/results/exercise_03_shape_select.jpg


def draw_lines(col=sd.COLOR_RED, *args):
    for arg in args:
        sd.line(start_point=arg[0], end_point=arg[1], width=1, color=col)


def draw_shape(point, angle, side_len, shape_type, color):
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

    list_of_coords[-1][1] = list_of_coords[0][0]  # замыкаем линию
    draw_lines(color, *list_of_coords)


print("Введите номер фигуры:\n"
      "1-треугольник\n"
      "2-квадрат\n"
      "3-пятиугольник\n"
      "4-шестиугольник\n"
      )

shape_num = int(input())
if not 0 <= shape_num < 5:
    print("ошибка ввода, установлена фигура по умолчанию")
    shape_num = 0

point_1 = sd.get_point(300, 300)
draw_shape(point_1, 0, 70, shape_num, sd.COLOR_RED)

sd.pause()
