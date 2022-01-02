# -*- coding: utf-8 -*-

from termcolor import cprint
from random import randint


######################################################## Часть первая
#
# Создать модель жизни небольшой семьи.
#
# Каждый день участники жизни могут делать только одно действие.
# Все вместе они должны прожить год и не умереть.
#
# Муж может:
#   есть,
#   играть в WoT,
#   ходить на работу,
# Жена может:
#   есть,
#   покупать продукты,
#   покупать шубу,
#   убираться в доме,

# Все они живут в одном доме, дом характеризуется:
#   кол-во денег в тумбочке (в начале - 100)
#   кол-во еды в холодильнике (в начале - 50)
#   кол-во грязи (в начале - 0)
#
# У людей есть имя, степень сытости (в начале - 30) и степень счастья (в начале - 100).
#
# Любое действие, кроме "есть", приводит к уменьшению степени сытости на 10 пунктов
# Кушают взрослые максимум по 30 единиц еды, степень сытости растет на 1 пункт за 1 пункт еды.
# Степень сытости не должна падать ниже 0, иначе чел умрет от голода.
#
# Деньги в тумбочку добавляет муж, после работы - 150 единиц за раз.
# Еда стоит 10 денег 10 единиц еды. Шуба стоит 350 единиц.
#
# Грязь добавляется каждый день по 5 пунктов, за одну уборку жена может убирать до 100 единиц грязи.
# Если в доме грязи больше 90 - у людей падает степень счастья каждый день на 10 пунктов,
# Степень счастья растет: у мужа от игры в WoT (на 20), у жены от покупки шубы (на 60, но шуба дорогая)
# Степень счастья не должна падать ниже 10, иначе чел умрает от депресии.
#
# Подвести итоги жизни за год: сколько было заработано денег, сколько сьедено еды, сколько куплено шуб.


class House:

    def __init__(self):
        self.money = 100
        self.human_food = 50
        self.cat_food = 30
        self.dirt = 0
        self.cat = None

    def __str__(self):
        return f'Денег дома - {self.money}, еда в холодильнике - {self.human_food}, ' \
               f'кошачья еда - {self.cat_food}, грязь - {self.dirt}'

    def increase_dirt(self):
        self.dirt += 5


class Animal:

    def __init__(self):
        self.fullness = 30
        self.happiness = 100
        self.isAlive = True


class Man(Animal):
    human_food_spent = 0
    money_earned = 0
    fur_coat_purchased = 0

    def __init__(self, name, house):
        super().__init__()
        self.name = name
        self.home = house

    def __str__(self):
        if self.isAlive:
            return f'Я - {self.name}, сытость {self.fullness}, счастье {self.happiness}'
        else:
            return f'{self.name} помер :('

    def eat(self):
        if self.home.human_food >= 10:
            food_volume = min((30, self.home.human_food))
            self.home.human_food -= food_volume
            Man.human_food_spent += food_volume
            self.fullness += food_volume
            eat_word = 'а' if isinstance(self, Wife) else ''
            cprint(f'{self.name} - поел{eat_word}, сытость - {self.fullness}', color='green')
        else:
            self.fullness -= 10
            cprint(f'{self.name} - нет еды!', color='red')

    def act(self):
        if self.isAlive:
            if self.fullness <= 0:
                cprint(f'{self.name} помер от голода', color='red')
                self.isAlive = False
            elif self.happiness <= 10:
                cprint(f'{self.name} совершил суицид на фоне депрессии', color='red')
                self.isAlive = False
            elif self.home.dirt > 90:
                self.happiness -= 10

    def pet_the_cat(self):
        self.fullness -= 10
        self.happiness = min(100, self.happiness + 5)
        cprint(f'{self.name} - гладит кота {self.home.cat.name}', color='green')


class Husband(Man):

    def act(self):
        super().act()
        if self.isAlive:
            dice = randint(1, 6)
            if self.fullness < 30:
                self.eat()
            elif self.happiness < 20:
                self.gaming()
            elif self.home.money < 450:
                self.work()
            elif dice == 1:
                self.eat()
            elif dice == 2:
                self.work()
            elif dice == 3:
                self.gaming()
            else:
                self.pet_the_cat()

    def work(self):
        self.fullness -= 10
        self.home.money += 150
        Man.money_earned += 150
        cprint(f'{self.name} на работе', color='green')

    def gaming(self):
        self.fullness -= 10
        self.happiness = min(100, self.happiness + 20)
        cprint(f'{self.name} играет в танки', color='green')


class Wife(Man):

    def act(self):
        super().act()
        if self.isAlive:
            dice = randint(1, 6)
            if self.fullness < 30:
                self.eat()
            elif self.home.human_food < 60:
                self.shopping()
            elif self.happiness < 40:
                self.buy_fur_coat()
            elif self.home.cat_food < 50:
                self.cat_shopping()
            elif self.home.dirt > 90:
                self.clean_house()
            elif dice == 1:
                self.eat()
            elif dice == 2:
                self.buy_fur_coat()
            elif dice == 3:
                self.clean_house()
            else:
                self.pet_the_cat()

    def shopping(self):
        self.fullness -= 10
        if self.home.money > 100:
            self.home.human_food += 100
            self.home.money -= 100
            cprint(f'{self.name} купила еды', color='green')
        else:
            cprint(f'{self.name} нет денег на еду', color='red')

    def cat_shopping(self):
        self.fullness -= 10
        if self.home.money > 100:
            self.home.cat_food += 100
            self.home.money -= 100
            cprint(f'{self.name} купила еды коту', color='green')
        else:
            cprint(f'{self.name} нет денег на еду для кота', color='red')

    def buy_fur_coat(self):
        self.fullness -= 10
        if self.home.money > 350:
            self.happiness = min(100, self.happiness + 60)
            self.home.money -= 350
            Man.fur_coat_purchased += 1
            cprint(f'{self.name} купила шубу', color='green')
        else:
            cprint(f'{self.name} нет денег на шубу!', color='red')

    def clean_house(self):
        self.fullness -= 10
        self.home.dirt = max(0, self.home.dirt - 100)
        cprint(f'{self.name} сделала уборку', color='green')


######################################################## Часть вторая
#
# После подтверждения учителем первой части надо
# отщепить ветку develop и в ней начать добавлять котов в модель семьи
#
# Кот может:
#   есть,
#   спать,
#   драть обои
#
# Люди могут:
#   гладить кота (растет степень счастья на 5 пунктов)
#
# В доме добавляется:
#   еда для кота (в начале - 30)
#
# У кота есть имя и степень сытости (в начале - 30)
# Любое действие кота, кроме "есть", приводит к уменьшению степени сытости на 10 пунктов
# Еда для кота покупается за деньги: за 10 денег 10 еды.
# Кушает кот максимум по 10 единиц еды, степень сытости растет на 2 пункта за 1 пункт еды.
# Степень сытости не должна падать ниже 0, иначе кот умрет от голода.
#
# Если кот дерет обои, то грязи становится больше на 5 пунктов


class Cat(Animal):

    def __init__(self, name, house):
        super().__init__()
        self.name = name
        self.home = house

    def __str__(self):
        if self.isAlive:
            return f'Я - {self.name}, сытость {self.fullness}'
        else:
            return f'{self.name} помер :('

    def act(self):
        if self.isAlive:
            if self.fullness <= 0:
                cprint(f'{self.name} помер от голода', color='red')
                self.isAlive = False
                return
            elif self.happiness <= 10:
                cprint(f'{self.name} совершил суицид на фоне депрессии', color='red')
                self.isAlive = False
                return
            dice = randint(1, 6)
            if self.fullness < 30:
                self.eat()
            elif dice == 1:
                self.eat()
            elif dice == 2:
                self.soil()
            else:
                self.sleep()

    def eat(self):
        if self.home.cat_food >= 10:
            self.home.cat_food -= 10
            self.fullness += 20
            cprint(f'{self.name} - поел, сытость - {self.fullness}', color='green')
        else:
            self.fullness -= 10
            cprint(f'{self.name} - нет еды!', color='red')

    def sleep(self):
        self.fullness -= 10
        cprint(f'{self.name} спит', color='green')

    def soil(self):
        self.fullness -= 10
        self.home.dirt += 5
        cprint(f'{self.name} дерет обои', color='green')


######################################################## Часть вторая бис
#
# После реализации первой части надо в ветке мастер продолжить работу над семьей - добавить ребенка
#
# Ребенок может:
#   есть,
#   спать,
#
# отличия от взрослых - кушает максимум 10 единиц еды,
# степень счастья  - не меняется, всегда ==100 ;)

class Child(Man):

    def act(self):
        super().act()
        self.happiness = 100
        if self.isAlive:
            dice = randint(1, 6)
            if self.fullness < 30:
                self.eat()
            elif dice == 1:
                self.eat()
            else:
                self.sleep()

    def eat(self):
        if self.home.human_food > 10:
            food_volume = 10
            self.home.human_food -= 10
            Man.human_food_spent += food_volume
            self.fullness += food_volume
            cprint(f'{self.name} - поел, сытость - {self.fullness}', color='green')
        else:
            self.fullness -= 10
            cprint(f'{self.name} - нет еды!', color='red')

    def sleep(self):
        self.fullness -= 10
        cprint(f'{self.name} спит', color='green')


######################################################## Часть третья
#
# после подтверждения учителем второй части (обоих веток)
# влить в мастер все коммиты из ветки develop и разрешить все конфликты
# отправить на проверку учителем.


home = House()
serge = Husband(name='Сережа', house=home)
masha = Wife(name='Маша', house=home)
kolya = Child(name='Коля', house=home)
murzik = Cat(name='Мурзик', house=home)
home.cat = murzik
objects = [serge, masha, kolya, murzik]

for day in range(1, 366):
    cprint(f'================== День {day} ==================', color='blue')
    for obj in objects:
        obj.act()
        cprint(obj, color='cyan')
    cprint(home, color='cyan')
    home.increase_dirt()

cprint(f'Итого еды съели {Man.human_food_spent}', color='yellow')
cprint(f'Итого денег заработано {Man.money_earned}', color='yellow')
cprint(f'Итого шуб купили {Man.fur_coat_purchased}', color='yellow')

# Усложненное задание (делать по желанию)
#
# Сделать из семьи любителей котов - пусть котов будет 3, или даже 5-10.
# Коты должны выжить вместе с семьей!
#
# Определить максимальное число котов, которое может прокормить эта семья при значениях зарплаты от 50 до 400.
# Для сглаживание случайностей моделирование за год делать 3 раза, если 2 из 3х выжили - считаем что выжили.
#
# Дополнительно вносить некий хаос в жизнь семьи
# - N раз в год вдруг пропадает половина еды из холодильника (коты?)
# - K раз в год пропадает половина денег из тумбочки (муж? жена? коты?!?!)
# Промоделировать - как часто могут случаться фейлы что бы это не повлияло на жизнь героев?
#   (N от 1 до 5, K от 1 до 5 - нужно вычислит максимумы N и K при котором семья гарантированно выживает)
#
# в итоге должен получится приблизительно такой код экспериментов
# for food_incidents in range(6):
#   for money_incidents in range(6):
#       life = Simulation(money_incidents, food_incidents)
#       for salary in range(50, 401, 50):
#           max_cats = life.experiment(salary)
#           print(f'При зарплате {salary} максимально можно прокормить {max_cats} котов')
