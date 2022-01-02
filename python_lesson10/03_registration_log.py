# -*- coding: utf-8 -*-

# Есть файл с протоколом регистраций пользователей на сайте - registrations.txt
# Каждая строка содержит: ИМЯ ЕМЕЙЛ ВОЗРАСТ, разделенные пробелами
# Например:
# Василий test@test.ru 27
#
# Надо проверить данные из файла, для каждой строки:
# - присутсвуют все три поля
# - поле имени содержит только буквы
# - поле емейл содержит @ и .
# - поле возраст является числом от 10 до 99
#
# В результате проверки нужно сформировать два файла
# - registrations_good.log для правильных данных, записывать строки как есть
# - registrations_bad.log для ошибочных, записывать строку и вид ошибки.
#
# Для валидации строки данных написать метод, который может выкидывать исключения:
# - НЕ присутсвуют все три поля: ValueError
# - поле имени содержит НЕ только буквы: NotNameError (кастомное исключение)
# - поле емейл НЕ содержит @ и .(точку): NotEmailError (кастомное исключение)
# - поле возраст НЕ является числом от 10 до 99: ValueError
# Вызов метода обернуть в try-except.

class NotNameError(Exception):
    pass


class NotEmailError(Exception):
    pass


def calc(line):
    name, email, age = line.split(' ')
    if not name.isalpha():
        raise NotNameError("invalid name")
    elif not (('@' in email) and ('.' in email)):
        raise NotEmailError("invalid email")
    elif not 10 <= int(age) <= 99:
        raise ValueError("invalid age")
    else:
        return line


with open('registrations_good_log.txt', 'w', encoding='utf8') as out_file_good, open('registrations_bad_log.txt', 'w', encoding='utf8') as out_file_bad:
        with open('registrations.txt', 'r', encoding='utf8') as in_file:
            for _line in in_file:
                try:
                    res = calc(_line)
                    out_file_good.write(res)
                except (ValueError, NotNameError, NotEmailError) as exc:
                    res = f'line\t\t{_line[:-1]:40} error {exc.args[0]}\n'
                    out_file_bad.write(res)
