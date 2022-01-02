# -*- coding: utf-8 -*-

# Имеется файл events.txt вида:
#
# [2018-05-17 01:55:52.665804] NOK
# [2018-05-17 01:56:23.665804] OK
# [2018-05-17 01:56:55.665804] OK
# [2018-05-17 01:57:16.665804] NOK
# [2018-05-17 01:57:58.665804] OK
# ...
#
# Напишите программу, которая считывает файл
# и выводит число событий NOK за каждую минуту в другой файл в формате
#
# [2018-05-17 01:57] 1234
# [2018-05-17 01:58] 4321
# ...
#
# Входные параметры: файл для анализа, файл результата
# Требования к коду: он должен быть готовым к расширению функциональности. Делать сразу на классах.

from abc import ABCMeta, abstractmethod


class Abstract_log_parser(metaclass=ABCMeta):

    def __init__(self, filename):
        self._filename = filename
        self._events = {}
        self._events_sorted = []
        self._group_key_len = 0

    @abstractmethod
    def _setup_group_param(self):
        pass

    def _group(self):
        with open(self._filename, 'r', encoding='utf8') as file:
            for line in file:
                op_result = line[29:-1]
                key = line[1:self._group_key_len]
                if op_result == 'NOK':
                    if key in self._events:
                        self._events[key] += 1
                    else:
                        self._events[key] = 1
                else:
                    if key in self._events:
                        self._events[key] += 0
                    else:
                        self._events[key] = 0

    def return_result(self, path):
        self._setup_group_param()
        self._group()
        _events_sorted = sorted(self._events.items(), key=lambda x: x[0])
        with open(path, 'w', encoding='utf8') as file:
            for event in _events_sorted:
                current_event = f'[{event[0]}] {event[1]}\n'
                file.write(current_event)


class Log_parse_by_minute(Abstract_log_parser):
    def _setup_group_param(self):
        self._group_key_len = 17


class Log_parse_by_hour(Abstract_log_parser):
    def _setup_group_param(self):
        self._group_key_len = 14


class Log_parse_by_month(Abstract_log_parser):
    def _setup_group_param(self):
        self._group_key_len = 8


class Log_parse_by_year(Abstract_log_parser):
    def _setup_group_param(self):
        self._group_key_len = 5


# После выполнения первого этапа нужно сделать группировку событий
#  - по часам
#  - по месяцу
#  - по году
# Для этого пригодится шаблон проектирование "Шаблонный метод" см https://goo.gl/Vz4828

parser = Log_parse_by_minute('events.txt')
# parser = Log_parse_by_hour('events.txt')
# parser = Log_parse_by_month('events.txt')
# parser = Log_parse_by_year('events.txt')
parser.return_result('events_out.txt')
