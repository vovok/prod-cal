#!/usr/bin/env python
# -*- coding: utf-8 -*-

from holidays import ProdCal

my_first_prod_cal = ProdCal(locale='RU')

# Проверяем праздничный день 1 мая
assert my_first_prod_cal.is_work_day(2016, 5, 1) == False
# Проверяем рабочий день
assert my_first_prod_cal.is_work_day(2016, 4, 1) == True
# Проверяем выходной день
assert my_first_prod_cal.is_work_day(2016, 4, 2) == False
# Проверяем перенос празничного дня (рабочий день)
assert my_first_prod_cal.is_work_day(2016, 2, 20) == True

