#!/usr/bin/env python
# -*- coding: utf-8 -*-

from calendar import weekday
from service import check_locale, get_prodcals
from config import DEFAULT_LOCALE
from datetime import date, timedelta

class ProdCal(object):
    def __init__(self, **kwargs):
        self.locale = check_locale(kwargs['locale']) if 'locale' in kwargs else DEFAULT_LOCALE
        self.non_work_days, self.work_days = get_prodcals(self.locale)

    def is_work_day(self, *day):
        """Проверяем рабочий ли сегодня день"""
        if len(day) != 1:
            day = date(*day)
        else:
            day = day[0]

        if self.work_days.is_value(day):
            return True

        if self.non_work_days.is_value(day) or weekday(day.year, day.month, day.day) in [5, 6]:
            return False

        return True

    def count_work_days(self, start_date, end_date):
        """Подсчёт количества рабочих дней в интервале"""
        if not (isinstance(start_date, date) and isinstance(end_date, date)):
            start_date, end_date = date(*start_date), date(*end_date)

        tm_delta = end_date - start_date
        work_days = 0
        for day in range(tm_delta.days+1):
            curr_date = start_date+timedelta(days=day)
            work_days += 1 if self.is_work_day(curr_date) else 0
        return work_days

    def count_holidays(self, start_date, end_date):
        """Подсчёт количества выходных дней в интервале"""
        if not (isinstance(start_date, date) and isinstance(end_date, date)):
            start_date, end_date = date(*start_date), date(*end_date)

        tm_delta = end_date - start_date
        holidays = 0
        for day in range(tm_delta.days+1):
            curr_date = start_date+timedelta(days=day)
            holidays += 1 if not self.is_work_day(curr_date) else 0
        return holidays
