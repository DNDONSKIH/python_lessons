# -*- coding: utf-8 -*-

import os, time, shutil


# Нужно написать скрипт для упорядочивания фотографий (вообще любых файлов)
# Скрипт должен разложить файлы из одной папки по годам и месяцам в другую.
# Например, так:
#   исходная папка
#       icons/cat.jpg
#       icons/man.jpg
#       icons/new_year_01.jpg
#   результирующая папка
#       icons_by_year/2018/05/cat.jpg
#       icons_by_year/2018/05/man.jpg
#       icons_by_year/2017/12/new_year_01.jpg
#
# Входные параметры основной функции: папка для сканирования, целевая папка.
# Имена файлов в процессе работы скрипта не менять, год и месяц взять из времени создания файла.
# Обработчик файлов делать в обьектном стиле - на классах.
#
# Файлы для работы взять из архива icons.zip - раззиповать проводником в папку icons перед написанием кода.
# Имя целевой папки - icons_by_year (тогда она не попадет в коммит)
#
# Пригодятся функции:
#   os.walk
#   os.path.dirname
#   os.path.join
#   os.path.normpath
#   os.path.getmtime
#   time.gmtime
#   os.makedirs
#   shutil.copy2
#
# Чтение документации/гугла по функциям - приветствуется. Как и поиск альтернативных вариантов :)
# Требования к коду: он должен быть готовым к расширению функциональности. Делать сразу на классах.

class File_replacer:

    def __init__(self):
        self._input_path = ''
        self._output_path = ''
        self._sub_paths = {}

    def act(self, input_path, output_path):
        self._input_path = os.path.join(os.path.dirname(__file__), input_path)
        self._output_path = os.path.join(os.path.dirname(__file__), output_path)
        self._sub_paths = {}

        for dirpath, dirnames, filenames in os.walk(self._input_path):
            if filenames:
                for file in filenames:
                    full_file_path = os.path.join(dirpath, file)
                    secs = os.path.getmtime(full_file_path)
                    file_time = time.gmtime(secs)
                    sub_path = os.path.normpath(f'{file_time.tm_year}/{file_time.tm_mon}')
                    new_dir_path = os.path.join(output_path, sub_path)
                    new_dir_full_file_path = os.path.join(new_dir_path, file)
                    if sub_path in self._sub_paths:
                        shutil.copy2(full_file_path, new_dir_full_file_path)
                    else:
                        self._sub_paths[sub_path] = True
                        os.makedirs(new_dir_path)
                        shutil.copy2(full_file_path, new_dir_full_file_path)


f = File_replacer()
f.act('icons', 'icons_by_year')

# Усложненное задание (делать по желанию)
# Нужно обрабатывать zip-файл, содержащий фотографии, без предварительного извлечения файлов в папку.
# Основная функция должна брать параметром имя zip-файла и имя целевой папки.
# Для этого пригодится шаблон проектирование "Шаблонный метод" см https://goo.gl/Vz4828
