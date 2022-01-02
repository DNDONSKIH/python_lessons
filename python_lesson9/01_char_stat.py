# -*- coding: utf-8 -*-

# Подсчитать статистику по буквам в романе Война и Мир.
# Входные параметры: файл для сканирования
# Статистику считать только для букв алфавита (см функцию .isalpha() для строк)
#
# Вывести на консоль упорядоченную статистику в виде
# +---------+----------+
# |  буква  | частота  |
# +---------+----------+
# |    А    |   77777  |
# |    Б    |   55555  |
# |   ...   |   .....  |
# |    a    |   33333  |
# |    б    |   11111  |
# |   ...   |   .....  |
# +---------+----------+
# |  итого  | 9999999  |
# +---------+----------+
#
# Упорядочивание по частоте - по убыванию. Ширину таблицы подберите по своему вкусу
# Требования к коду: он должен быть готовым к расширению функциональности. Делать сразу на классах.


# import os
# import os.path
# import zipfile
#
# def unzip(file_name):
#     zfile = zipfile.ZipFile(file_name, 'r')
#     for filename in zfile.namelist():
#         zfile.extract(filename)
#     return filename
#
#
# _file_name = os.path.join(os.path.dirname(__file__), 'python_snippets', 'voyna-i-mir.txt.zip')
# res_path = unzip(_file_name)

from abc import ABCMeta, abstractmethod


class Stat_collector(metaclass=ABCMeta):

    def __init__(self, file_name):
        self._stats = {}
        self._sorted_stats = []
        self._filename = file_name
        self._total_char_count = 0

    def _collect_stat(self):
        self._stats = {}
        total_char_count = 0
        with open(self._filename, 'r', encoding='cp1251') as file:
            for line in file:
                for char in line:
                    if char.isalpha():
                        if char in self._stats:
                            self._stats[char] += 1
                        else:
                            self._stats[char] = 1
        for key in self._stats:
            total_char_count += self._stats[key]
        self._total_char_count = total_char_count

    @abstractmethod
    def _sort_stats(self):
        pass

    def _print_result(self):
        print('+---------+----------+')
        print('|  буква  | частота  |')
        print('+---------+----------+')
        for val in self._sorted_stats:
            print('|{:^9}|{:^10}|'.format(val[0], val[1]))
        print('+---------+----------+')
        print('|  итого  |{:^10}|'.format(self._total_char_count))
        print('+---------+----------+')

    def sort(self):
        self._collect_stat()
        self._sort_stats()
        self._print_result()


class Sc_sort_by_key_up(Stat_collector):
    def _sort_stats(self):
        self._sorted_stats = sorted(self._stats.items(), key=lambda x: x[0])


class Sc_sort_by_key_down(Stat_collector):
    def _sort_stats(self):
        self._sorted_stats = sorted(self._stats.items(), key=lambda x: x[0], reverse=True)


class Sc_sort_by_value_up(Stat_collector):
    def _sort_stats(self):
        self._sorted_stats = sorted(self._stats.items(), key=lambda x: x[1])


class Sc_sort_by_value_down(Stat_collector):
    def _sort_stats(self):
        self._sorted_stats = sorted(self._stats.items(), key=lambda x: x[1], reverse=True)


# После выполнения первого этапа нужно сделать упорядочивание статистики
#  - по частоте по возрастанию
#  - по алфавиту по возрастанию
#  - по алфавиту по убыванию
# Для этого пригодится шаблон проектирование "Шаблонный метод" см https://goo.gl/Vz4828


# sc = Sc_sort_by_key_up('voyna-i-mir.txt')
# sc = Sc_sort_by_key_down('voyna-i-mir.txt')
# sc = Sc_sort_by_value_up('voyna-i-mir.txt')
sc = Sc_sort_by_value_down('voyna-i-mir.txt')
sc.sort()
