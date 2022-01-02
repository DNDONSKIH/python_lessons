# -*- coding: utf-8 -*-

# Умножить константу BRUCE_WILLIS на пятый элемент строки, введенный пользователем

BRUCE_WILLIS = 42

result = None
input_data = input('Если хочешь что-нибудь сделать, сделай это сам: ')

try:
    leeloo = int(input_data[4])
    result = BRUCE_WILLIS * leeloo
except ValueError as exc:
    print(f'{exc} - невозможно преобразовать к числу')
except IndexError as exc:
    print(f'{exc} - выход за границы списка')
except:
    print(f'Произошла непонятная ошибка')
else:
    print(f"- Leeloo Dallas! Multi-pass № {result}!")
finally:
    action_status = '' if result else 'не'
    print(f'{action_status} получилось умножить!')

# Ообернуть код и обработать исключительные ситуации для произвольных входных параметров
# - ValueError - невозможно преобразовать к числу
# - IndexError - выход за границы списка
# - остальные исключения
# для каждого типа исключений написать на консоль соотв. сообщение




