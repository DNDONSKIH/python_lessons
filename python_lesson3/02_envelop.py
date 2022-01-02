# -*- coding: utf-8 -*-

from pprint import pprint

# (if/elif/else)

# Заданы размеры envelop_x, envelop_y - размеры конверта и paper_x, paper_y листа бумаги
#
# Определить, поместится ли бумага в конверте (стороны листа параллельны сторонам конверта)
#
# Результат проверки вывести на консоль (ДА/НЕТ)
# Использовать только операторы if/elif/else, можно вложенные

envelop_x, envelop_y = 10, 7
paper_x, paper_y = 8, 9

# проверить для
# paper_x, paper_y = 9, 8
# paper_x, paper_y = 6, 8
# paper_x, paper_y = 8, 6
# paper_x, paper_y = 3, 4
# paper_x, paper_y = 11, 9
# paper_x, paper_y = 9, 11
# (просто раскоментировать нужную строку и проверить свой код)

paper_sizes = (
    (9, 8),
    (6, 8),
    (8, 6),
    (3, 4),
    (11, 9),
    (9, 11)
)

for paper_size in paper_sizes:
    x = paper_size[0]
    y = paper_size[1]

    print(f'Поместится ли бумага размером х = {x}, y = {y} в конверт размером '
          f'х = {envelop_x}, y = {envelop_y}? ', end='')

    if x <= envelop_x:
        if y <= envelop_y:
            print('ДА')
        elif y <= envelop_x:
            if x <= envelop_y:
                print('ДА, если повернуть!')
            else:
                print('НЕТ')
        else:
            print('НЕТ')
    else:
        print('НЕТ')


print('\n\n')
# Усложненное задание, решать по желанию.
# Заданы размеры hole_x, hole_y прямоугольного отверстия и размеры brick_х, brick_у, brick_z кирпича (все размеры
# могут быть в диапазоне от 1 до 1000)
#
# Определить, пройдет ли кирпич через отверстие (грани кирпича параллельны сторонам отверстия)

hole_x, hole_y = 8, 9
# brick_x, brick_y, brick_z = 11, 10, 2
# brick_x, brick_y, brick_z = 11, 2, 10
# brick_x, brick_y, brick_z = 10, 11, 2
# brick_x, brick_y, brick_z = 10, 2, 11
# brick_x, brick_y, brick_z = 2, 10, 11
# brick_x, brick_y, brick_z = 2, 11, 10
# brick_x, brick_y, brick_z = 3, 5, 6
# brick_x, brick_y, brick_z = 3, 6, 5
# brick_x, brick_y, brick_z = 6, 3, 5
# brick_x, brick_y, brick_z = 6, 5, 3
# brick_x, brick_y, brick_z = 5, 6, 3
# brick_x, brick_y, brick_z = 5, 3, 6
# brick_x, brick_y, brick_z = 11, 3, 6
# brick_x, brick_y, brick_z = 11, 6, 3
# brick_x, brick_y, brick_z = 6, 11, 3
# brick_x, brick_y, brick_z = 6, 3, 11
# brick_x, brick_y, brick_z = 3, 6, 11
# brick_x, brick_y, brick_z = 3, 11, 6
# (просто раскоментировать нужную строку и проверить свой код)

bricks = [
    [11, 10, 2],
    [11, 2, 10],
    [10, 11, 2],
    [10, 2, 11],
    [2, 10, 11],
    [2, 11, 10],
    [3, 5, 6],
    [3, 6, 5],
    [6, 3, 5],
    [6, 5, 3],
    [5, 6, 3],
    [5, 3, 6],
    [11, 3, 6],
    [11, 6, 3],
    [6, 11, 3],
    [6, 3, 11],
    [3, 6, 11],
    [3, 11, 6],
]


for brick in bricks:
    tmp = sorted(brick)
    hole = sorted([hole_x, hole_y])
    way_for_1_side = False
    way_for_2_side = False

    for size in tmp:
        if size <= hole[0]:
            tmp.remove(size)
            way_for_1_side = True
            break

    for size in tmp:
        if size <= hole[1]:
            tmp.remove(size)
            way_for_2_side = True
            break

    if way_for_1_side and way_for_2_side:
        print(f'кирпич с размерами x = {brick[0]}, y = {brick[1]}, z = {brick[2]} '
              f'можно просунуть в дырку размером x = {hole_x}, y = {hole_y}')
    else:
        print(f'кирпич с размерами x = {brick[0]}, y = {brick[1]}, z = {brick[2]} '
              f'нельзя просунуть в дырку размером x = {hole_x}, y = {hole_y}')
