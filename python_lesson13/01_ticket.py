# -*- coding: utf-8 -*-


# Заполнить все поля в билете на самолет.
# Создать функцию, принимающую параметры: ФИО, откуда, куда, дата вылета,
# и заполняющую ими шаблон билета Skillbox Airline.
# Шаблон взять в файле lesson_013/images/ticket_template.png
# Пример заполнения lesson_013/images/ticket_sample.png
# Подходящий шрифт искать на сайте ofont.ru
import os
from PIL import Image, ImageDraw, ImageFont, ImageColor
import argparse

font_path = os.path.normpath('./fonts/arial.ttf')
template_path = os.path.normpath('./images/ticket_template.png')
result_path = os.path.normpath('./images/result.png')


def make_ticket(fio, from_, to, date, save_to):
    im = Image.open(template_path)
    draw = ImageDraw.Draw(im)
    font = ImageFont.truetype(font_path, size=17)
    draw.text((45, 120), fio, font=font, fill=ImageColor.colormap['black'])
    draw.text((45, 190), from_, font=font, fill=ImageColor.colormap['black'])
    draw.text((45, 255), to, font=font, fill=ImageColor.colormap['black'])
    draw.text((290, 255), date, font=font, fill=ImageColor.colormap['black'])
    im.show()
    out_path = save_to if save_to else result_path
    im.save(out_path)


# Усложненное задание (делать по желанию).
# Написать консольный скрипт c помощью встроенного python-модуля agrparse.
# Скрипт должен принимать параметры:
#   --fio - обязательный, фамилия.
#   --from - обязательный, откуда летим.
#   --to - обязательный, куда летим.
#   --date - обязательный, когда летим.
#   --save_to - необязательный, путь для сохранения заполненнего билета.
# и заполнять билет.


if __name__ == '__main__':
    arg_parser = argparse.ArgumentParser(description='Формирователь билетов')
    arg_parser.add_argument('--fio', type=str, help='ФИО')
    arg_parser.add_argument('--From', type=str, help='Откуда')
    arg_parser.add_argument('--to', type=str, help='Куда')
    arg_parser.add_argument('--date', type=str, help='Дата')
    arg_parser.add_argument('--save_to', type=str, default='', help='выходной путь')
    args = arg_parser.parse_args()
    if args:
        make_ticket(fio=args.fio, from_=args.From, to=args.to, date=args.date, save_to=args.save_to)
