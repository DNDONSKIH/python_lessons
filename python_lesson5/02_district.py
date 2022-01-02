# -*- coding: utf-8 -*-

# Составить список всех живущих на районе и Вывести на консоль через запятую
# Формат вывода: На районе живут ...
# подсказка: для вывода элементов списка через запятую можно использовать функцию строки .join()
# https://docs.python.org/3/library/stdtypes.html#str.join

from district.central_street.house1 import room1 as c_h1_r1
from district.central_street.house1 import room2 as c_h1_r2
from district.central_street.house2 import room1 as c_h2_r1
from district.central_street.house2 import room2 as c_h2_r2

from district.soviet_street.house1 import room1 as s_h1_r1
from district.soviet_street.house1 import room2 as s_h1_r2
from district.soviet_street.house2 import room1 as s_h2_r1
from district.soviet_street.house2 import room2 as s_h2_r2

rooms = (
    c_h1_r1.folks,
    c_h1_r2.folks,
    c_h2_r1.folks,
    c_h2_r2.folks,
    s_h1_r1.folks,
    s_h1_r2.folks,
    s_h2_r1.folks,
    s_h2_r2.folks,
)

result = ""
for room in rooms:
    result += ', '.join(room) + ', '

result = result.replace(' , ', ' ')[:-2]

print(result)
