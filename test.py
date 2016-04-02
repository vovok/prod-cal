#!/usr/bin/env python
# -*- coding: utf-8 -*-

from holidays import ProdCal
from datetime import date

my_first_prod_cal = ProdCal(locale='RU')

# Проверяем праздничный день 1 мая
assert my_first_prod_cal.is_work_day(2016, 5, 1) == False
# Проверяем рабочий день
assert my_first_prod_cal.is_work_day(2016, 4, 1) == True
# Проверяем выходной день
assert my_first_prod_cal.is_work_day(2016, 4, 2) == False
# Проверяем перенос празничного дня (рабочий день)
assert my_first_prod_cal.is_work_day(2016, 2, 20) == True

# Передаём сразу объект даты
assert my_first_prod_cal.is_work_day(date(2016, 5, 1)) == False
# Передаём сразу объект даты
assert my_first_prod_cal.is_work_day(date(2016, 4, 1)) == True

# Проверяем количество рабочих дней в различных месяцах
assert my_first_prod_cal.count_work_days([2016, 4, 1], [2016, 4, 30]) == 21
assert my_first_prod_cal.count_work_days([2016, 5, 1], [2016, 5, 31]) == 19
assert my_first_prod_cal.count_work_days([2016, 6, 1], [2016, 6, 30]) == 21

# Передаём сразу в формате даты и времени
assert my_first_prod_cal.count_work_days(date(2016, 4, 1), date(2016, 4, 30)) == 21
assert my_first_prod_cal.count_work_days(date(2016, 5, 1), date(2016, 5, 31)) == 19
assert my_first_prod_cal.count_work_days(date(2016, 6, 1), date(2016, 6, 30)) == 21

# Проверяем выходных дней в различных месяцах
assert my_first_prod_cal.count_holidays([2016, 4, 1], [2016, 4, 30]) == 9
assert my_first_prod_cal.count_holidays([2016, 5, 1], [2016, 5, 31]) == 12
assert my_first_prod_cal.count_holidays([2016, 6, 1], [2016, 6, 30]) == 9

# Передаём сразу в формате даты и времени
assert my_first_prod_cal.count_holidays(date(2016, 4, 1), date(2016, 4, 30)) == 9
assert my_first_prod_cal.count_holidays(date(2016, 5, 1), date(2016, 5, 31)) == 12
assert my_first_prod_cal.count_holidays(date(2016, 6, 1), date(2016, 6, 30)) == 9
