# -*- coding: utf-8 -*-

# (цикл while)

# Ежемесячная стипендия студента составляет educational_grant руб., а расходы на проживание превышают стипендию
# и составляют expenses руб. в месяц. Рост цен ежемесячно увеличивает расходы на 3%, кроме первого месяца
# Составьте программу расчета суммы денег, которую необходимо единовременно попросить у родителей,
# чтобы можно было прожить учебный год (10 месяцев), используя только эти деньги и стипендию.
# Формат вывода:
#   Студенту надо попросить ХХХ.ХХ рублей

educational_grant, expenses = 10000, 12000

total_money_need = 0
month_count = 10
total_grant_value = educational_grant * month_count
while month_count > 0:
    month_count -= 1
    total_money_need += expenses
    expenses *= 1.03

need_money = total_money_need - total_grant_value
need_money = round(need_money, 2)
print(f"Студенту надо попросить {need_money} рублей")
