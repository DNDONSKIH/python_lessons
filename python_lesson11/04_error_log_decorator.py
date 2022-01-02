# -*- coding: utf-8 -*-

# Написать декоратор, который будет логировать (записывать в лог файл)
# ошибки из декорируемой функции и выбрасывать их дальше.
#
# Имя файла лога - function_errors.log
# Формат лога: <имя функции> <параметры вызова> <тип ошибки> <текст ошибки>
# Лог файл открывать каждый раз при ошибке в режиме 'a'


def log_errors(func):
    def wrapper(*args, **kwargs):
        try:
            result = func(*args, **kwargs)
            return result
        except Exception as ex:
            # print(dir(ex))
            result = f'Имя функции: {func.__name__}  ' \
                     f'параметры вызова: args: {[*args]} kwargs: {[*kwargs.items()]} ' \
                     f'тип ошибки: {ex.__class__.__name__} текст ошибки {ex}\n'
            with open('function_errors.log', 'a', encoding='utf8') as file:
                file.write(result)
            raise

    return wrapper


def log_errors_to_file(filename='function_errors.log'):
    def log_errors(func):
        def wrapper(*args, **kwargs):
            try:
                result = func(*args, **kwargs)
                return result
            except Exception as ex:
                result = f'Имя функции: {func.__name__}  ' \
                         f'параметры вызова: args: {[*args]} kwargs: {[*kwargs.items()]} ' \
                         f'тип ошибки: {ex.__class__.__name__} текст ошибки {ex}\n'
                with open(filename, 'a', encoding='utf8') as file:
                    file.write(result)
                raise

        return wrapper

    return log_errors


# Проверить работу на следующих функциях
@log_errors_to_file("function_errors_2.log")
def perky(param):
    return param / 0


@log_errors
def check_line(line):
    name, email, age = line.split(' ')
    if not name.isalpha():
        raise ValueError("it's not a name")
    if '@' not in email or '.' not in email:
        raise ValueError("it's not a email")
    if not 10 <= int(age) <= 99:
        raise ValueError('Age not in 10..99 range')


lines = [
    'Ярослав bxh@ya.ru 600',
    'Земфира tslzp@mail.ru 52',
    'Тролль nsocnzas.mail.ru 82',
    'Джигурда wqxq@gmail.com 29',
    'Земфира 86',
    'Равшан wmsuuzsxi@mail.ru 35',
]
for line in lines:
    try:
        check_line(line)
    except Exception as exc:
        print(f'Invalid format: {exc}')

try:
    perky(param=42)
except Exception as exc:
    print(f'Ошибка: {exc}')

# Усложненное задание (делать по желанию).
# Написать декоратор с параметром - именем файла
#
# @log_errors('function_errors.log')
# def func():
#     pass
