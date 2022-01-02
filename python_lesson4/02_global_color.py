# -*- coding: utf-8 -*-
import simple_draw as sd


# Добавить цвет в функции рисования геом. фигур. из упр lesson_004/01_shapes.py
# (код функций скопировать сюда и изменить)
# Запросить у пользователя цвет фигуры посредством выбора из существующих:
#   вывести список всех цветов с номерами и ждать ввода номера желаемого цвета.
# Потом нарисовать все фигуры этим цветом

# Пригодятся функции
# sd.get_point()
# sd.line()
# sd.get_vector()
# и константы COLOR_RED, COLOR_ORANGE, COLOR_YELLOW, COLOR_GREEN, COLOR_CYAN, COLOR_BLUE, COLOR_PURPLE
# Результат решения см lesson_004/results/exercise_02_global_color.jpg

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


color_dict = {1: sd.COLOR_RED,
              2: sd.COLOR_ORANGE,
              3: sd.COLOR_YELLOW,
              4: sd.COLOR_GREEN,
              5: sd.COLOR_CYAN,
              6: sd.COLOR_BLUE,
              7: sd.COLOR_PURPLE}

print("Введите номер цвета:\n"
      "1-красный\n"
      "2-оранжевый\n"
      "3-желтый\n"
      "4-зеленый\n"
      "5-синенький\n"
      "6-синий\n"
      "7-пурпурный\n")

color_num = int(input())
if 0 < color_num < 8:
    user_color = color_dict[color_num]
else:
    print("ошибка ввода, установлен цвет по умолчанию")
    user_color = sd.COLOR_RED


point_1 = sd.get_point(100, 100)
draw_shape(point_1, 0, 70, 0, user_color)
point_1 = sd.get_point(100, 200)
draw_shape(point_1, 0, 70, 1, user_color)
point_1 = sd.get_point(100, 300)
draw_shape(point_1, 0, 70, 2, user_color)
point_1 = sd.get_point(100, 400)
draw_shape(point_1, 0, 70, 3, user_color)

sd.pause()
