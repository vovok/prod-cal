#!/usr/bin/env python
# -*- coding: utf-8 -*-

from calendar import weekday

LOCALE = "RU"

class ProdDict(dict):
    def is_value(self, year, month, day):
        path = self[LOCALE][year][month]
        if path:
            if day in path:
                return True
            else:
                return False

NON_WORK_DAY_DICT = ProdDict({"RU":{
    2016: {1: [1, 4, 5, 6, 7, 8],
           2: [22, 23],
           3: [7, 8],
           4: [],
           5: [1, 2, 3, 9],
           6: [13],
           7: [],
           8: [],
           9: [],
           10: [],
           11: [4],
           12: []}
}})

WORK_DAY_DICT = ProdDict({"RU":{
    2016: {1: [],
           2: [20],
           3: [],
           4: [],
           5: [],
           6: [],
           7: [],
           8: [],
           9: [],
           10: [],
           11: [],
           12: []}
}})


def is_work_day(year, month, day):
    """Проверяем рабочий ли сегодня день"""
    if WORK_DAY_DICT.is_value(year, month, day):
        return True

    if NON_WORK_DAY_DICT.is_value(year, month, day) or weekday(year, month, day) in [5, 6]:
        return False

    return True


