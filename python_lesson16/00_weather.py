# -*- coding: utf-8 -*-

# Создать модуль-движок с классом WeatherMaker, необходимым для получения и формирования предсказаний.
# В нём должен быть метод, получающий прогноз с выбранного вами сайта (парсинг + re) за некоторый диапазон дат,
# а затем, получив данные, сформировать их в словарь {погода: Облачная, температура: 10, дата:datetime...}

# Добавить класс ImageMaker.
# Снабдить его методом рисования открытки
# (использовать OpenCV, в качестве заготовки брать lesson_016/python_snippets/external_data/probe.jpg):
#   С текстом, состоящим из полученных данных (пригодится cv2.putText)
#   С изображением, соответствующим типу погоды
# (хранятся в lesson_016/python_snippets/external_data/weather_img ,но можно нарисовать/добавить свои)
#   В качестве фона добавить градиент цвета, отражающего тип погоды
# Солнечно - от желтого к белому
# Дождь - от синего к белому
# Снег - от голубого к белому
# Облачно - от серого к белому

# Добавить класс DatabaseUpdater с методами:
#   Получающим данные из базы данных за указанный диапазон дат.
#   Сохраняющим прогнозы в базу данных (использовать peewee)

# Сделать программу с консольным интерфейсом, постаравшись все выполняемые действия вынести в отдельные функции.
# Среди действий, доступных пользователю должны быть:
#   Добавление прогнозов за диапазон дат в базу данных
#   Получение прогнозов за диапазон дат из базы
#   Создание открыток из полученных прогнозов
#   Выведение полученных прогнозов на консоль
# При старте консольная утилита должна загружать прогнозы за прошедшую неделю.

# Рекомендации:
# Можно создать отдельный модуль для инициализирования базы данных.
# Как далее использовать эту базу данных в движке:
# Передавать DatabaseUpdater url-путь
# https://peewee.readthedocs.io/en/latest/peewee/playhouse.html#db-url
# Приконнектится по полученному url-пути к базе данных
# Инициализировать её через DatabaseProxy()
# https://peewee.readthedocs.io/en/latest/peewee/database.html#dynamically-defining-a-database
import argparse
import datetime
import os.path
import io
import peewee
import requests
import re
import cv2
import numpy as np
from PIL import Image, ImageDraw, ImageFont, ImageColor
from bs4 import BeautifulSoup


def view_image(image, name_of_window):
    cv2.namedWindow(name_of_window, cv2.WINDOW_NORMAL)
    cv2.imshow(name_of_window, image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


class WeatherMaker:
    WEATHER_URL = 'https://pogoda.mail.ru/prognoz/voronezh/14dney/'
    DATE_PATTERN = r'[1-3]?[0-9]\s(января|февраля|марта|апреля|мая|нюня|июля|августа|сентября|октября|ноября|декабря)'
    MONTH_TO_MONTH_NUM_MAP = {'января': 1, 'февраля': 2, 'марта': 3, 'апреля': 4, 'мая': 5, 'нюня': 6,
                              'июля': 7, 'августа': 8, 'сентября': 9, 'октября': 10, 'ноября': 11, 'декабря': 12, }

    def get_month_num(self, month_name):
        return WeatherMaker.MONTH_TO_MONTH_NUM_MAP[month_name]

    def get_weather(self):
        response = requests.get(WeatherMaker.WEATHER_URL)
        weather_forecast = []
        if response.status_code == 200:
            html_doc = BeautifulSoup(response.text, features='html.parser')
            list_of_values = html_doc.find_all('div', {'class': 'day__temperature'})
            list_of_descr = html_doc.find_all('div', {'class': 'day__description'})
            list_of_dates = html_doc.find_all('div', {'class': 'heading_line'})
            temp_list, descr_list, dates_list = [], [], []

            for i in range(2, len(list_of_values), 4):
                temp_list.append(list_of_values[i].text)
                descr_list.append(list_of_descr[i].text.split('\n')[1])

            for item in list_of_dates:
                var = item.text.replace('Сегодня - ', '')
                matched = re.search(WeatherMaker.DATE_PATTERN, var).group()
                date = matched.split(' ')
                _day_num = int(date[0])
                _month_num = self.get_month_num(date[1])
                now = datetime.date.today()
                _year_num = now.year
                if now.month > 1 and _month_num == 1:  # корректировка года в прогнозе на январь, запрошеном в декабре
                    _year_num += 1
                _dt = datetime.date(year=_year_num, month=_month_num, day=_day_num)
                dates_list.append(_dt)

            weather_forecast = [
                {
                    'date': dates_list[i],
                    'state': descr_list[i],
                    'temp': temp_list[i]
                }
                for i in range(len(dates_list))
            ]
        return weather_forecast


class ImageMaker:
    _CARD_COLORS = {
        'DimGrey': (105, 105, 105),
        'Yellow': (255, 255, 0),
        'Blue': (0, 0, 255),
        'Aqua': (0, 255, 255),
    }

    _WEATHER_STATE_TO_CARD_COLOR_MAP = {
        'облачно': _CARD_COLORS['DimGrey'],
        'осадки': _CARD_COLORS['Blue'],
        'дождь': _CARD_COLORS['Blue'],
        'снег': _CARD_COLORS['Aqua'],
        'метель': _CARD_COLORS['Aqua'],
        'солнечно': _CARD_COLORS['Yellow'],
    }

    _WEATHER_STATE_TO_CARD_IMAGE_MAP = {
        'облачно': './weather_img/cloud.jpg',
        'осадки': './weather_img/cloud.jpg',
        'дождь': './weather_img/rain.jpg',
        'снег': './weather_img/snow.jpg',
        'метель': './weather_img/snow.jpg',
        'солнечно': './weather_img/sun.jpg',
    }

    # https://note.nkmk.me/en/python-numpy-generate-gradation-image/
    def _get_gradient_2d(self, start, stop, width, height, is_horizontal):
        if is_horizontal:
            return np.tile(np.linspace(start, stop, width), (height, 1))
        else:
            return np.tile(np.linspace(start, stop, height), (width, 1)).T

    def _get_gradient_3d(self, width, height, start_list, stop_list, is_horizontal_list):
        result = np.zeros((height, width, len(start_list)), dtype=float)

        for i, (start, stop, is_horizontal) in enumerate(zip(start_list, stop_list, is_horizontal_list)):
            result[:, :, i] = self._get_gradient_2d(start, stop, width, height, is_horizontal)

        return result

    def get_weather_picture(self, date_text, degrees_text, weather_state):
        array = self._get_gradient_3d(512, 256, ImageMaker._WEATHER_STATE_TO_CARD_COLOR_MAP[weather_state],
                                      (255, 255, 255), (True, True, True))
        im = Image.fromarray(np.uint8(array))
        draw = ImageDraw.Draw(im)
        font_path = os.path.normpath('./font/arial.ttf')
        font = ImageFont.truetype(font_path, size=25)
        draw.text((10, 10), f'{date_text}', font=font, fill=ImageColor.colormap['black'])
        draw.text((10, 200), f'{degrees_text}', font=font, fill=ImageColor.colormap['black'])
        # im.save('background_gradient.jpg')
        background_file_like = io.BytesIO()
        im.save(background_file_like, 'jpeg')
        background_file_like.seek(0)
        # https://stackoverflow.com/questions/14063070/overlay-a-smaller-image-on-a-larger-image-python-opencv
        # l_img = cv2.imread("background_gradient.jpg")
        # https://stackoverflow.com/questions/46624449/load-bytesio-image-with-opencv
        file_bytes = np.asarray(bytearray(background_file_like.read()), dtype=np.uint8)
        l_img = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)
        s_img = cv2.imread(os.path.normpath(ImageMaker._WEATHER_STATE_TO_CARD_IMAGE_MAP[weather_state]))
        x_offset, y_offset = 400, 75
        l_img[y_offset:y_offset + s_img.shape[0], x_offset:x_offset + s_img.shape[1]] = s_img
        # viewImage(l_img, '1')
        cv2.imwrite(f"./out/forecast_{date_text}.jpg", l_img)


_db = peewee.SqliteDatabase("forecast.db")


class BaseTable(peewee.Model):
    class Meta:
        database = _db


class Forecast(BaseTable):
    date = peewee.DateTimeField()
    state = peewee.CharField()
    temp = peewee.CharField()


class DatabaseUpdater:

    def __init__(self, db_instance):
        self.db = db_instance

    def init_db(self):
        self.db.create_tables([Forecast, ])

    def create_or_update_forecast(self, forecast):
        try:
            query = Forecast.get(Forecast.date == forecast['date'])
            query.delete_instance()
        except:
            pass
        finally:
            pass
            Forecast.create(date=forecast['date'], state=forecast['state'], temp=forecast['temp'])

    def get_forecast_from_db(self, date):
        response = {}
        try:
            query = Forecast.get(Forecast.date == date)
            response['date'], response['state'], response['temp'] = query.date, query.state, query.temp
        except:
            pass
        finally:
            return response


def print_forecast(forecast):
    if forecast:
        print(f"{forecast['date'].strftime('%d.%m.%Y')} : {forecast['state']} {forecast['temp']}")
    else:
        print('нет прогноза на данную дату!')


if __name__ == '__main__':
    IM = ImageMaker()
    WM = WeatherMaker()
    DU = DatabaseUpdater(_db)
    # DU.init_db()

    arg_parser = argparse.ArgumentParser(description='Генератор прогнозов')
    arg_parser.add_argument('--add_forecast', type=int, help='Добавление прогнозов за указанное'
                                                             ' количество дней в базу данных')
    arg_parser.add_argument('--print_forecast', type=int, help='Получение прогнозов за указанное '
                                                               'количество дней дат из базы')
    arg_parser.add_argument('--create_cards', type=int, help='Создание открыток из полученных прогнозов')
    args = arg_parser.parse_args()
    if any((args.add_forecast, args.print_forecast, args.create_cards)):
        if args.add_forecast:
            day_count = min(14, args.add_forecast)
            res = WM.get_weather()
            for i in range(day_count):
                DU.create_or_update_forecast(res[i])

        if args.print_forecast:
            day_count = min(14, args.print_forecast)
            for i in range(day_count):
                _today = datetime.datetime.today()
                d = datetime.date(year=_today.year, month=_today.month, day=_today.day) + datetime.timedelta(days=i)
                fc = DU.get_forecast_from_db(d)
                print_forecast(fc)

        if args.create_cards:
            day_count = min(14, args.create_cards)
            for i in range(day_count):
                _today = datetime.datetime.today()
                d = datetime.date(year=_today.year, month=_today.month, day=_today.day) + datetime.timedelta(days=i)
                fc = DU.get_forecast_from_db(d)
                if fc:
                    _date = fc['date'].strftime("%d.%m.%Y")
                    _degrees = fc['temp']
                    _state = fc['state']
                    IM.get_weather_picture(_date, _degrees, _state)

    else:
        for i in range(7):
            _today = datetime.datetime.today()
            d = datetime.date(year=_today.year, month=_today.month, day=_today.day) - datetime.timedelta(days=i)
            fc = DU.get_forecast_from_db(d)
            print_forecast(fc)
