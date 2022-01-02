# -*- coding: utf-8 -*-

# На основе своего кода из lesson_009/02_log_parser.py напишите итератор (или генератор)
# котрый читает исходный файл events.txt и выдает число событий NOK за каждую минуту
# <время> <число повторений>
#
# пример использования:
#
# grouped_events = <создание итератора/генератора>
# for group_time, event_count in grouped_events:
#     print(f'[{group_time}] {event_count}')
#
# на консоли должно появится что-то вроде
#
# [2018-05-17 01:57] 1234

from collections import defaultdict


def grouped_events_generator(filename):
    nok_events = defaultdict(lambda: 0)
    key = None

    with open(filename, 'r', encoding='utf8') as file:
        for line in file:
            op_result = line[29:-1]
            prev_key = key
            key = line[1:17]
            if op_result == 'NOK':
                nok_events[key] += 1
            else:
                nok_events[key] += 0
            if key != prev_key and prev_key is not None:
                # print(prev_key, nok_events[prev_key])
                yield prev_key, nok_events[prev_key]


grouped_events = grouped_events_generator('events.txt')


# for i in range(10):
#     print(next(grouped_events))

for group_time, event_count in grouped_events:
    print(f'[{group_time}] {event_count}')
