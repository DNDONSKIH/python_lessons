# -*- coding: utf-8 -*-


# Задача: вычислить 3 тикера с максимальной и 3 тикера с минимальной волатильностью в МНОГОПОТОЧНОМ стиле
#
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
from threading import Thread
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


class Volatile_calculator(Thread):

    def __init__(self, filename, *args, **kwargs):
        super().__init__(*args, **kwargs)
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
    threads = []

    for dirpath, dirnames, filenames in os.walk(filepath):
        if filenames:
            for file in filenames:
                full_file_path = os.path.join(dirpath, file)
                threads.append(Volatile_calculator(full_file_path))

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

    print('Итого:')

    for thread in threads:
        ticker_dict[thread.ticker] = thread.volatile

    ticker_list = sorted(ticker_dict.items(), key=lambda x: x[1])

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
