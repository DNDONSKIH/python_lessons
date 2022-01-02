# -*- coding: utf-8 -*-


# Есть функция генерации списка простых чисел


# def get_prime_numbers(n):
#     prime_numbers = []
#     for number in range(2, n + 1):
#         for prime in prime_numbers:
#             if number % prime == 0:
#                 break
#         else:
#             prime_numbers.append(number)
#     return prime_numbers


# Часть 1
# На основе алгоритма get_prime_numbers создать класс итерируемых обьектов,
# который выдает последовательность простых чисел до n
#
# Распечатать все простые числа до 10000 в столбик


class PrimeNumbers:
    def __init__(self, n):
        self.prime_numbers = []
        self.i = 1
        self.n = n

    def __iter__(self):
        self.prime_numbers = []
        self.i = 1
        return self

    def __next__(self):
        while True:
            self.i += 1
            if self.i >= self.n:
                raise StopIteration()
            for prime in self.prime_numbers:
                if self.i % prime == 0:
                    break
            else:
                self.prime_numbers.append(self.i)
                return self.i


print("iterator:")

prime_number_iterator = PrimeNumbers(n=10000)
for number in prime_number_iterator:
    print(number, end=" ")


# Часть 2
# Теперь нужно создать генератор, который выдает последовательность простых чисел до n
# Распечатать все простые числа до 10000 в столбик


def prime_numbers_generator(n):
    prime_numbers = []
    for number in range(2, n + 1):
        for prime in prime_numbers:
            if number % prime == 0:
                break
        else:
            prime_numbers.append(number)
            yield number


print("\ngenerator:")
for num in prime_numbers_generator(n=10000):
    print(num, end=" ")


# Часть 3
# Написать несколько функций-фильтров, которые выдает True, если число:
# 1) "счастливое" в обыденном пониманиии - сумма первых цифр равна сумме последних
#       Если число имеет нечетное число цифр (например 727 или 92083),
#       то для вычисления "счастливости" брать равное количество цифр с начала и конца:
#           727 -> 7(2)7 -> 7 == 7 -> True
#           92083 -> 92(0)83 -> 9+2 == 8+3 -> True
# 2) "палиндромное" - одинаково читающееся в обоих направлениях. Например 723327 и 101
# 3) придумать свою (https://clck.ru/GB5Fc в помощь)
#
# Подумать, как можно применить функции-фильтры к полученной последовательности простых чисел
# для получения, к примеру: простых счастливых чисел, простых палиндромных чисел,
# простых счастливых палиндромных чисел и так далее. Придумать не менее 2х способов.
#
# Подсказка: возможно, нужно будет добавить параметр в итератор/генератор.


def is_happy_number(n):
    if num < 10:
        return False
    else:
        num_in_string = str(n)
        substr_len = len(num_in_string) // 2
        left_substring = num_in_string[:substr_len]
        right_substr = num_in_string[-substr_len:]
        sum_in_left, sum_in_right = 0, 0
        for char in left_substring:
            sum_in_left += int(char)
        for char in right_substr:
            sum_in_right += int(char)
        if sum_in_left == sum_in_right:
            return True
        else:
            return False


def is_palindrome_number(n):
    if n < 0:
        return False
    num_in_string = str(n)
    num_in_string_reversed = str(n)[::-1]
    if num_in_string == num_in_string_reversed:
        return True
    else:
        return False


def pow_of_2_generator(max_val=100500):
    n = 0
    while True:
        result = 2 ** n
        yield result
        n += 1
        if result > max_val:
            break


def is_pow_of_2(n):
    if n in pow_of_2_generator(n):
        return True
    else:
        return False


print("\nPrime and happy:")
for num in filter(is_happy_number, prime_numbers_generator(n=10000)):
    print(num, end=" ")

print("\nPrime and palindrome:")
for num in filter(is_palindrome_number, prime_numbers_generator(n=10000)):
    print(num, end=" ")

print("\nPow of 2")
for num in pow_of_2_generator():
    print(num, end=" ")

print("\nPrime and pow of 2:")
for num in filter(is_pow_of_2, prime_numbers_generator(n=10000)):
    print(num, end=" ")
