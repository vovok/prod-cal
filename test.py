#!/usr/bin/env python
# -*- coding: utf-8 -*-

from holidays import is_work_day

# Проверяем праздничный день 1 мая
assert is_work_day(2016, 5, 1) == False
# Проверяем рабочий день
assert is_work_day(2016, 4, 1) == True
# Проверяем выходной день
assert is_work_day(2016, 4, 2) == False
# Проверяем перенос празничного дня (рабочий день)
assert is_work_day(2016, 2, 20) == True
