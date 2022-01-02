# -*- coding: utf-8 -*-


# Описание предметной области:
#
# При торгах на бирже совершаются сделки - один купил, второй продал.
# Покупают и продают ценные бумаги (акции, облигации, фьючерсы, етс). Ценные бумаги - это по сути долговые расписки.
# Ценные бумаги выпускаются партиями, от десятка до несколько миллионов штук.
# Каждая такая партия (выпуск) имеет свой торговый код на бирже - тикер - https://goo.gl/MJQ5Lq
# Все бумаги из этой партии (выпуска) одинаковы в цене, поэтому говорят о цене одной бумаги.
# У разных выпусков бумаг - разные цены, которые могут отличаться в сотни и тысячи раз.
# Каждая биржевая сделка характеризуется:
#   тикер ценнной бумаги
#   время сделки
#   цена сделки
#   обьем сделки (сколько ценных бумаг было куплено)
#
# В ходе торгов цены сделок могут со временем расти и понижаться. Величина изменения цен называтея волатильностью.
# Например, если бумага №1 торговалась с ценами 11, 11, 12, 11, 12, 11, 11, 11 - то она мало волатильна.
# А если у бумаги №2 цены сделок были: 20, 15, 23, 56, 100, 50, 3, 10 - то такая бумага имеет большую волатильность.
# Волатильность можно считать разными способами, мы будем считать сильно упрощенным способом -
# отклонение в процентах от средней цены за торговую сессию:
#   средняя цена = (максимальная цена + минимальная цена) / 2
#   волатильность = ((максимальная цена - минимальная цена) / средняя цена) * 100%
# Например для бумаги №1:
#   average_price = (12 + 11) / 2 = 11.5
#   volatility = ((12 - 11) / average_price) * 100 = 8.7%
# Для бумаги №2:
#   average_price = (100 + 3) / 2 = 51.5
#   volatility = ((100 - 3) / average_price) * 100 = 188.34%
#
# В реальности волатильность рассчитывается так: https://goo.gl/VJNmmY
#
# Задача: вычислить 3 тикера с максимальной и 3 тикера с минимальной волатильностью.
# Бумаги с нулевой волатильностью вывести отдельно.
# Результаты вывести на консоль в виде:
#   Максимальная волатильность:
#       ТИКЕР1 - ХХХ.ХХ %
#       ТИКЕР2 - ХХХ.ХХ %
#       ТИКЕР3 - ХХХ.ХХ %
#   Минимальная волатильность:
#       ТИКЕР4 - ХХХ.ХХ %
#       ТИКЕР5 - ХХХ.ХХ %
#       ТИКЕР6 - ХХХ.ХХ %
#   Нулевая волатильность:
#       ТИКЕР7, ТИКЕР8, ТИКЕР9, ТИКЕР10, ТИКЕР11, ТИКЕР12
# Волатильности указывать в порядке убывания. Тикеры с нулевой волатильностью упорядочить по имени.
#
# Подготовка исходных данных
# 1. Скачать файл https://drive.google.com/file/d/1l5sia-9c-t91iIPiGyBc1s9mQ8RgTNqb/view?usp=sharing
#       (обратите внимание на значок скачивания в правом верхнем углу,
#       см https://drive.google.com/file/d/1M6mW1jI2RdZhdSCEmlbFi5eoAXOR3u6G/view?usp=sharing)
# 2. Раззиповать средствами операционной системы содержимое архива
#       в папку python_base_source/lesson_012/trades
# 3. В каждом файле в папке trades содержится данные по сделакам по одному тикеру, разделенные запятыми.
#   Первая строка - название колонок:
#       SECID - тикер
#       TRADETIME - время сделки
#       PRICE - цена сделки
#       QUANTITY - количество бумаг в этой сделке
#   Все последующие строки в файле - данные о сделках
#
# Подсказка: нужно последовательно открывать каждый файл, вычитывать данные, высчитывать волатильность и запоминать.
# Вывод на консоль можно сделать только после обработки всех файлов.
#
# Для плавного перехода к мультипоточности, код оформить в обьектном стиле, используя следующий каркас
#
# class <Название класса>:
#
#     def __init__(self, <параметры>):
#         <сохранение параметров>
#
#     def run(self):
#         <обработка данных>

import os, sys, time

zero_volatile = []
min_volatile = []
max_volatile = []


def time_track(func):
    def surrogate(*args, **kwargs):
        started_at = time.time()

        result = func(*args, **kwargs)

        ended_at = time.time()
        elapsed = round(ended_at - started_at, 5)
        print(f'Функция работала {elapsed} секунд(ы)')
        return result

    return surrogate


class Volatile_calculator:

    def __init__(self, filename):
        self.filename = filename
        self.ticker = None
        self.max_price = sys.float_info.min
        self.min_price = sys.float_info.max
        self.aver_price = 0.0
        self.volatile = 0.0

    def _parse_line(self, line):
        try:
            secid, tradetime, price, quantity = line.split(',')
            price_of_one = float(price)  # / float(quantity)
            return secid, price_of_one
        except:
            return None

    @time_track
    def run(self):
        with open(self.filename, 'r', encoding='utf8') as file:
            for line in file:
                result = self._parse_line(line)
                if result:
                    ticker, price = result
                    if self.ticker is None:
                        self.ticker = ticker
                    self.max_price = max(self.max_price, price)
                    self.min_price = min(self.min_price, price)
        self.aver_price = (self.max_price + self.min_price) / 2
        self.volatile = ((self.max_price - self.min_price) / self.aver_price) * 100
        #   средняя цена = (максимальная цена + минимальная цена) / 2
        #   волатильность = ((максимальная цена - минимальная цена) / средняя цена) * 100%


@time_track
def calc_tickers():
    filepath = os.path.normpath('./trades')
    ticker_dict = {}
    global zero_volatile, min_volatile, max_volatile

    for dirpath, dirnames, filenames in os.walk(filepath):
        if filenames:
            for file in filenames:
                full_file_path = os.path.join(dirpath, file)
                vc = Volatile_calculator(full_file_path)
                vc.run()
                # print(f'ticker: {vc.ticker}  volatile - {vc.volatile:.2f} %')
                ticker_dict[vc.ticker] = vc.volatile
    ticker_list = sorted(ticker_dict.items(), key=lambda x: x[1])
    print('Итого:')
    for item in ticker_list:
        volatile = item[1]
        if volatile == 0.0:
            zero_volatile.append(item)
        else:
            min_volatile.append(item)
            if len(min_volatile) == 3:
                break
    max_volatile.extend(ticker_list[-3:])


calc_tickers()

print('Максимальная волатильность:')
print(f'\t\t{max_volatile[2][0]} - {max_volatile[2][1]:.2f} %')
print(f'\t\t{max_volatile[1][0]} - {max_volatile[1][1]:.2f} %')
print(f'\t\t{max_volatile[0][0]} - {max_volatile[0][1]:.2f} %')
print('Минимальная волатильность:')
print(f'\t\t{min_volatile[0][0]} - {min_volatile[0][1]:.2f} %')
print(f'\t\t{min_volatile[1][0]} - {min_volatile[1][1]:.2f} %')
print(f'\t\t{min_volatile[2][0]} - {min_volatile[2][1]:.2f} %')
print('Нулевая волатильность:')
print(f"\t\t{' '.join([x[0] for x in zero_volatile])}")
