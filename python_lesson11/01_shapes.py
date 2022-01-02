# -*- coding: utf-8 -*-

import simple_draw as sd

# На основе вашего кода из решения lesson_004/01_shapes.py сделать функцию-фабрику,
# которая возвращает функции рисования треугольника, четырехугольника, пятиугольника и т.д.
#
# Функция рисования должна принимать параметры
# - точка начала рисования
# - угол наклона
# - длина стороны
#
# Функция-фабрика должна принимать параметр n - количество сторон.


def get_polygon(n):
    def draw_shape(point, angle, length):
        vectors = []
        current_angle = angle
        prev_vector = sd.get_vector(start_point=point, angle=angle, length=length, width=1)
        for _ in range(n - 1):
            vectors.append(prev_vector)
            current_angle += (360 / n)
            prev_vector = sd.get_vector(start_point=prev_vector.end_point, angle=current_angle, length=length,
                                        width=1)
        for vector in vectors:
            vector.draw()
        sd.line(start_point=vectors[-1].end_point, end_point=vectors[0].start_point, width=1)

    return draw_shape


draw_triangle = get_polygon(n=3)
draw_triangle(point=sd.get_point(200, 200), angle=13, length=100)

draw_rectangle = get_polygon(n=4)
draw_rectangle(point=sd.get_point(300, 300), angle=13, length=100)


sd.pause()
