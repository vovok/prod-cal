#!/usr/bin/env python
# -*- coding: utf-8 -*-

from config import LOCALE_SUPPORTING
from importlib import import_module


def check_locale(locale):
    if locale.upper() in LOCALE_SUPPORTING:
        return locale
    else:
        raise ValueError("Unnsupported/Unknown locale")


def get_prodcals(locale):
    pc = import_module('holidays.prodcals.' + locale.lower())
    return pc.NON_WORK_DAY_DICT, pc.WORK_DAY_DICT
