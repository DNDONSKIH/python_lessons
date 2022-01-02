import random as r

_secret_num = []


def mastermind_get_number():
    result = []
    num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

    num = num_list[r.randint(0, 8)]
    num_list.remove(num)
    result.append(num)

    num = num_list[r.randint(0, 8)]
    num_list.remove(num)
    result.append(num)

    num = num_list[r.randint(0, 7)]
    num_list.remove(num)
    result.append(num)

    num = num_list[r.randint(0, 6)]
    num_list.remove(num)
    result.append(num)

    global _secret_num
    _secret_num = result


def mastermind_check_number(num):
    user_num_list = [int(x) for x in num]
    bulls = 0
    cows = 0
    for i in range(4):
        if user_num_list[i] == _secret_num[i]:
            bulls += 1
        elif user_num_list[i] in _secret_num:
            cows += 1
    result = {'bulls': bulls, 'cows': cows}
    return result


def mastermind_is_game_over(num):
    user_input = [int(x) for x in num]
    if user_input == _secret_num:
        return True
    else:
        return False


