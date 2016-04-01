#!/usr/bin/env python
# -*- coding: utf-8 -*-

from calendar import weekday
from service import check_locale
from config import DEFAULT_LOCALE
from importlib import import_module

class ProdCal(object):
    def __init__(self, **kwargs):
        self.locale = check_locale(kwargs['locale']) if 'locale' in kwargs else DEFAULT_LOCALE
        self.pc = import_module('holidays.prodcals.'+self.locale.lower())
        self.non_work_days, self.work_days = self.pc.NON_WORK_DAY_DICT, self.pc.WORK_DAY_DICT

    def is_work_day(self, year, month, day):
        """Проверяем рабочий ли сегодня день"""
        if self.work_days.is_value(year, month, day):
            return True

        if self.non_work_days.is_value(year, month, day) or weekday(year, month, day) in [5, 6]:
            return False

        return True
