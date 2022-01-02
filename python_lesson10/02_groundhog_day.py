# -*- coding: utf-8 -*-

# День сурка
#
# Напишите функцию one_day() которая возвращает количество кармы от 1 до 7
# и может выкидывать исключения:
# - IamGodError
# - DrunkError
# - CarCrashError
# - GluttonyError
# - DepressionError
# - SuicideError
# Одно из этих исключений выбрасывается с вероятностью 1 к 13 каждый день
#
# Функцию оберните в бесконечный цикл, выход из которого возможен только при накоплении
# кармы до уровня ENLIGHTENMENT_CARMA_LEVEL. Исключения обработать и записать в лог.
# При создании собственных исключений максимально использовать функциональность
# базовых встроенных исключений.

from random import randint

ENLIGHTENMENT_CARMA_LEVEL = 777


class IamGodError(Exception):
    pass


class DrunkError(Exception):
    pass


class CarCrashError(Exception):
    pass


class GluttonyError(Exception):
    pass


class DepressionError(Exception):
    pass


class SuicideError(Exception):
    pass


def one_day():
    raise_exc_dice = randint(1, 13)
    if raise_exc_dice == 1:
        exc_dice = randint(1, 6)
        if exc_dice == 1:
            raise IamGodError('IamGodError')
        elif exc_dice == 2:
            raise DrunkError('DrunkError')
        elif exc_dice == 3:
            raise CarCrashError('CarCrashError')
        elif exc_dice == 4:
            raise GluttonyError('GluttonyError')
        elif exc_dice == 5:
            raise DepressionError('DepressionError')
        else:
            raise SuicideError('SuicideError')
    else:
        carma_dice = randint(1, 7)
        return carma_dice


with open("groundhog_day_log.txt", 'w', encoding='utf8') as file:
    current_carma = 0
    current_day = 0
    while True:
        current_day += 1
        try:
            current_carma += one_day()
        except (IamGodError, DrunkError, CarCrashError, GluttonyError, DepressionError, SuicideError) as exc:
            res = f'День {current_day:<4} {exc.args[0]}\n'
            file.write(res)

        if current_carma >= ENLIGHTENMENT_CARMA_LEVEL:
            break

print('Вышли!')

# https://goo.gl/JnsDqu
