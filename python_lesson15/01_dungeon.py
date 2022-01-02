# -*- coding: utf-8 -*-

# С помощью JSON файла rpg.json задана "карта" подземелья.
# Подземелье было выкопано монстрами и они всё ещё скрываются где-то в его глубинах,
# планируя набеги на близлежащие поселения.
# Само подземелье состоит из двух главных разветвлений и нескольких развилок,
# и лишь один из путей приведёт вас к главному Боссу
# и позволит предотвратить набеги и спасти мирных жителей.

# Напишите игру, в которой пользователь, с помощью консоли,
# сможет:
# 1) исследовать это подземелье:
#   -- передвижение должно осуществляться присваиванием переменной и только в одну сторону
#   -- перемещаясь из одной локации в другую, пользователь теряет время, указанное в конце названия каждой локации
# Так, перейдя в локацию Location_1_tm500 - вам необходимо будет списать со счёта 500 секунд.
# Тег, в названии локации, указывающий на время - 'tm'.
#
# 2) сражаться с монстрами:
#   -- сражение имитируется списанием со счета персонажа N-количества времени и получением N-количества опыта
#   -- опыт и время указаны в названиях монстров (после exp указано значение опыта и после tm указано время)
# Так, если в локации вы обнаружили монстра Mob_exp10_tm20 (или Boss_exp10_tm20)
# необходимо списать со счета 20 секунд и добавить 10 очков опыта.
# Теги указывающие на опыт и время - 'exp' и 'tm'.
# После того, как игра будет готова, сыграйте в неё и наберите 280 очков при положительном остатке времени.

# По мере продвижения вам так же необходимо вести журнал,
# в котором должна содержаться следующая информация:
# -- текущее положение
# -- текущее количество опыта
# -- текущая дата (отсчёт вести с первой локации с помощью datetime)
# После прохождения лабиринта, набора 280 очков опыта и проверки на остаток времени (remaining_time > 0),
# журнал необходимо записать в csv файл (назвать dungeon.csv, названия столбцов взять из field_names).

# Пример лога игры:
# Вы находитесь в Location_0_tm0
# У вас 0 опыта и осталось 1234567890.0987654321 секунд
# Прошло уже 0:00:00
# Внутри вы видите:
# -- Монстра Mob_exp10_tm0
# -- Вход в локацию: Location_1_tm10400000
# -- Вход в локацию: Location_2_tm333000000
# Выберите действие:
# 1.Атаковать монстра
# 2.Перейти в другую локацию
# 3.Выход
import csv
import datetime
import json
import os
import re
import time
from decimal import Decimal
from pprint import pprint


class RpgGame:
    _REMAINING_TIME = '1234567890.0987654321'
    _FIELD_NAMES = ['current_location', 'current_experience', 'current_date']

    def __init__(self):
        self.exp = Decimal(0)
        self.time_to_end = Decimal(RpgGame._REMAINING_TIME)
        self.time_elapsed = Decimal(0)
        self.date = 0
        self.time_str_for_log = None
        self.mobs = None
        self.sub_dungeons = None
        self.journal = [["Location_0_tm0", '0', '0'], ]
        self.current_location = 'Location_0_tm0'
        self.prev_location = None
        self.rpg_map = {}
        with open("rpg.json", "r") as read_file:
            self.rpg_map = json.load(read_file)

    def _look_around_dungeon(self, location, dungeon):
        """
        Возвращает содержимое комнаты location
        """
        for _key in dungeon:
            if _key == location:
                return dungeon[_key]
            else:
                search_objects = dungeon[_key]
                for item in search_objects:
                    if isinstance(item, dict):
                        deep_search = self._look_around_dungeon(location, item)
                        if deep_search:
                            return deep_search
                    else:
                        continue
        return []

    def _kill_monster_in_dungeon(self, monster_name, location, dungeon):
        """
        удаляет монстра monster_name из комнаты location
        """
        for _key in dungeon:
            if _key == location:
                if monster_name in dungeon[_key]:
                    dungeon[_key].remove(monster_name)
                    print(monster_name, 'повержен!')
            else:
                search_objects = dungeon[_key]
                for item in search_objects:
                    if isinstance(item, dict):
                        deep_search = self._look_around_dungeon(location, item)
                        if deep_search:
                            if monster_name in deep_search:
                                deep_search.remove(monster_name)
                                print(monster_name, 'повержен!')
                    else:
                        continue

    def _look_around(self, location):
        return self._look_around_dungeon(location, self.rpg_map)

    def _kill_monster(self, monster_name, location):
        return self._kill_monster_in_dungeon(monster_name, location, self.rpg_map)

    def _user_output(self):
        print('Вы находитесь в локации: ', self.current_location)
        print(f'У вас {self.exp} опыта и осталось {self.time_to_end - self.time_elapsed} секунд')
        spent_time = time.gmtime(float(self.time_elapsed))
        time_spent = datetime.time(hour=spent_time.tm_hour, minute=spent_time.tm_min, second=spent_time.tm_sec)
        self.time_str_for_log = time_spent.strftime("%H:%M:%S")
        print(f'Прошло уже {self.time_str_for_log}')
        obj_around = self._look_around(self.current_location)
        self.mobs = [x for x in obj_around if isinstance(x, str)]
        self.sub_dungeons = [x for x in obj_around if isinstance(x, dict)]
        print('Вы видите монстров:', ''.join([f'#{x[0]} : {x[1]} ' for x in enumerate(self.mobs)]))
        print('Вы видите другие комнаты:',
              ''.join([f'#{x[0]} {y} ' for x in enumerate(self.sub_dungeons) for y in x[1]]))

    def _user_input(self):
        while True:
            input_data = input('Для продолжения введите код команды:')
            matched_attack = re.match(r'a\s*[0-9]', input_data)
            matched_walk = re.match(r'w\s*[0-9]', input_data)
            matched_quit = re.match(r'q', input_data)
            events = (matched_attack, matched_walk, matched_quit)
            if any(events):
                event = list(filter(lambda x: True if x else False, events)).pop()
                return event[0][0], int(event[0][1:]) if len(event[0]) > 1 else None

    def _check_game_result(self):
        self.journal.append([self.current_location, str(self.exp), self.time_str_for_log])
        if (self.time_to_end - self.time_elapsed) <= 0:
            print('Время вышло!')
            return True
        elif self.exp >= 200:
            print('Ура, победа!')
            with open('rpg_log.csv', 'w', newline='') as out_csv:
                writer = csv.writer(out_csv)
                writer.writerows(self.journal)
            return True
        else:
            return False

    def _update_game_state(self, user_input):
        os.system('cls' if os.name == 'nt' else 'clear')
        if user_input[0] == 'a':
            mob_num = user_input[1]
            if mob_num < len(self.mobs):
                mob_name = self.mobs[mob_num]
                add_exp = Decimal(re.search(r'exp(\d+)_tm', mob_name)[1])
                time_spent_for_battle = Decimal(re.search(r'tm(\d+)', mob_name)[1])
                self.time_elapsed += time_spent_for_battle
                self.exp += add_exp
                self._kill_monster(mob_name, self.current_location)
            else:
                print('нет тут такого монстра!')
        elif user_input[0] == 'w':
            location_num = user_input[1]
            if location_num < len(self.sub_dungeons):
                location_name = list(self.sub_dungeons[location_num].keys())[0]
                self.prev_location = self.current_location
                self.current_location = location_name
                time_spent_for_travel = Decimal(re.search(r'tm(\d+\.?\d+)', location_name)[1])
                self.time_elapsed += time_spent_for_travel
            else:
                print('нет тут такой комнаты!')
        elif user_input[0] == 'q':
            if self.prev_location:
                time_spent_for_travel = Decimal(re.search(r'tm(\d+\.?\d+)', self.current_location)[1])
                self.time_elapsed += time_spent_for_travel
                self.current_location, self.prev_location = self.prev_location, self.current_location
            else:
                print('Вход завалило камнями, выйти не получится!')
        else:
            raise ValueError()

    def main_loop(self):
        print('Правила игры:\n'
              'Для совершения действия введите команду:\n'
              'Атака:                     "a номер монстра"\n'
              'Переход в другую комнату:  "w номер комнаты"\n'
              'Возврат в прошлую комнату: "q"\n')
        while True:
            self._user_output()
            self._update_game_state(self._user_input())
            is_game_over = self._check_game_result()
            if is_game_over:
                print('Конец игры!')
                break


if __name__ == '__main__':
    game = RpgGame()
    game.main_loop()

    # print(game._look_around('Location_10_tm551000000'))

# Учитывая время и опыт, не забывайте о точности вычислений!
