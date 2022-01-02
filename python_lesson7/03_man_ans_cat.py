# -*- coding: utf-8 -*-


# Доработать практическую часть урока lesson_007/python_snippets/08_practice.py

# Необходимо создать класс кота. У кота есть аттрибуты - сытость и дом (в котором он живет).
# Кот живет с человеком в доме.
# Для кота дом характеризируется - миской для еды и грязью.
# Изначально в доме нет еды для кота и нет грязи.

# Доработать класс человека, добавив методы
# подобрать кота - у кота появляется дом.
# купить коту еды - кошачья еда в доме увеличивается на 50, деньги уменьшаются на 50.
# убраться в доме - степень грязи в доме уменьшается на 100, сытость у человека уменьшается на 20.
# Увеличить кол-во зарабатываемых человеком денег до 150 (он выучил пайтон и устроился на хорошую работу :)

# Кот может есть, спать и драть обои - необходимо реализовать соответствующие методы.
# Когда кот спит - сытость уменьшается на 10
# Когда кот ест - сытость увеличивается на 20, кошачья еда в доме уменьшается на 10.
# Когда кот дерет обои - сытость уменьшается на 10, степень грязи в доме увеличивается на 5
# Если степень сытости < 0, кот умирает.
# Так же надо реализовать метод "действуй" для кота, в котором он принимает решение
# что будет делать сегодня

# Человеку и коту надо вместе прожить 365 дней.

# -*- coding: utf-8 -*-

from random import randint
from termcolor import cprint


class Cat:

    def __init__(self, name):
        self.name = name
        self.fullness = 50
        self.house = None

    def __str__(self):
        return f'Я - {self.name}, сытость {self.fullness}'

    def eat(self):
        if self.house.cat_food >= 10:
            cprint(f'{self.name} поел', color='yellow')
            self.fullness += 20
            self.house.cat_food -= 10
        else:
            cprint(f'{self.name} нет еды', color='red')

    def tear_wallpaper(self):
        self.fullness -= 10
        self.house.dirt += 5
        cprint(f'{self.name} дерет обои', color='yellow')

    def sleep(self):
        self.fullness -= 10
        cprint(f'{self.name} спит', color='yellow')

    def act(self):
        if self.fullness <= 0:
            cprint(f'{self.name} умер...', color='red')
            return
        dice = randint(1, 6)
        if self.fullness < 20:
            self.eat()
        elif dice == 1:
            self.tear_wallpaper()
        else:
            self.sleep()


class Man:

    def __init__(self, name):
        self.name = name
        self.fullness = 50
        self.house = None

    def __str__(self):
        return f'Я - {self.name}, сытость {self.fullness}'

    def eat(self):
        if self.house.food >= 10:
            cprint(f'{self.name} поел', color='yellow')
            self.fullness += 10
            self.house.food -= 10
        else:
            cprint(f'{self.name} нет еды', color='red')

    def work(self):
        cprint(f'{self.name} сходил на работу', color='blue')
        self.house.money += 150
        self.fullness -= 10

    def watch_tv(self):
        cprint(f'{self.name} смотрел TV целый день', color='green')
        self.fullness -= 10

    def shopping(self):
        if self.house.money >= 50:
            cprint(f'{self.name} сходил в магазин за едой', color='magenta')
            self.house.money -= 50
            self.house.food += 50
        else:
            cprint(f'{self.name} деньги кончились!', color='red')

    def cat_shopping(self):
        if self.house.money >= 50:
            cprint(f'{self.name} сходил в магазин за кормом для кота', color='magenta')
            self.house.money -= 50
            self.house.cat_food += 50
        else:
            cprint(f'{self.name} деньги кончились!', color='red')

    def go_to_the_house(self, house):
        self.house = house
        self.fullness -= 10
        cprint(f'{self.name} Вьехал в дом', color='cyan')

    def get_a_cat(self, cat):
        cat.house = self.house
        self.fullness -= 10
        cprint(f'{self.name} Завел кота {cat.name}', color='cyan')

    def clean(self):
        self.house.dirt -= 100
        self.fullness -= 20
        cprint(f'{self.name} Сделал уборку', color='cyan')

    def act(self):
        if self.fullness <= 0:
            cprint(f'{self.name} умер...', color='red')
            return
        dice = randint(1, 6)
        if self.fullness < 20:
            self.eat()
        elif self.house.food < 10:
            self.shopping()
        elif self.house.money < 50:
            self.work()
        elif self.house.cat_food < 10:
            self.cat_shopping()
        elif self.house.dirt >= 100 and self.fullness > 20:
            self.clean()
        elif dice == 1:
            self.work()
        elif dice in (2, 3):
            self.eat()
        else:
            self.watch_tv()


class House:

    def __init__(self):
        self.food = 50
        self.money = 0
        self.cat_food = 0
        self.dirt = 0

    def __str__(self):
        return f'В доме осталось {self.food} еды, {self.cat_food} кошачьей еды, ' \
               f'денег осталось {self.money}, грязи {self.dirt} единиц'


# my_sweet_home = House()
# man = Man(name='Василий')
# kitty = Cat(name="Васька")
# man.go_to_the_house(house=my_sweet_home)
# man.get_a_cat(cat=kitty)

# for day in range(1, 366):
#     print(f'================ день {day} ==================')
#     man.act()
#     kitty.act()
#     print('--- в конце дня ---')
#     print(man)
#     print(kitty)
#     print(my_sweet_home)

# Усложненное задание (делать по желанию)
# Создать несколько (2-3) котов и подселить их в дом к человеку.
# Им всем вместе так же надо прожить 365 дней.

# (Можно определить критическое количество котов, которое может прокормить человек...)

my_sweet_home = House()
man = Man(name='Василий')
kittys = [
    Cat(name="Кот Васька"),
    Cat(name="Кот Рыжик"),
    Cat(name="Кот Барсик"),
]
man.go_to_the_house(house=my_sweet_home)
for kitty in kittys:
    man.get_a_cat(cat=kitty)

for day in range(1, 366):
    print(f'================ день {day} ==================')
    man.act()
    for kitty in kittys:
        kitty.act()
    print('--- в конце дня ---')
    print(man)
    for kitty in kittys:
        print(kitty)
    print(my_sweet_home)