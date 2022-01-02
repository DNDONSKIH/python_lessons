# -*- coding: utf-8 -*-

# Создать пакет, в который скопировать функции отрисовки из предыдущего урока
#  - радуги
#  - стены
#  - дерева
#  - смайлика
#  - снежинок
# Функции по модулям разместить по тематике. Название пакета и модулей - по смыслу.
# Создать модуль с функцией отрисовки кирпичного дома с широким окном и крышей.

# С помощью созданного пакета нарисовать эпохальное полотно "Утро в деревне".
# На картине должны быть:
#  - кирпичный дом, в окошке - смайлик.
#  - слева от дома - сугроб (предположим что это ранняя весна)
#  - справа от дома - дерево (можно несколько)
#  - справа в небе - радуга, слева - солнце (весна же!)
# пример см. lesson_005/results/04_painting.jpg
# Приправить своей фантазией по вкусу (коты? коровы? люди? трактор? что придумается)

import simple_draw as sd
from my_drawing.draw_tree import draw_branches as d_tree
from my_drawing.draw_wall import draw_wall as d_wall
from my_drawing.draw_roof import draw_roof as d_roof
from my_drawing.draw_face import draw_face as d_face
from my_drawing.draw_snow import draw_snow as d_snow
from my_drawing.draw_sun import draw_sun as d_sun
from my_drawing.draw_rainbow import draw_rainbow as d_rbow

sd.resolution = (1200, 600)

d_tree(point=sd.get_point(1000, 30), angle=90, length=70)

d_wall(400, 10, 400, 100)
d_wall(400, 110, 50, 200)
d_wall(750, 110, 50, 200)
d_wall(400, 310, 400, 100)
d_roof(400, 410)
d_face(600, 200)
d_snow()
d_sun()
d_rbow()


# Усложненное задание (делать по желанию)
# Анимировать картину.
# Пусть слева идет снегопад, радуга переливается цветами, смайлик моргает, солнце крутит лучами, етс.
# Задержку в анимировании все равно надо ставить, пусть даже 0.01 сек - так библиотека устойчивей работает.

while True:
    d_rbow()
    sd.sleep(0.1)
    if sd.user_want_exit():
        break


sd.pause()
