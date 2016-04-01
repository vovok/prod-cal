#!/usr/bin/env python
# -*- coding: utf-8 -*-

from config import LOCALE_SUPPORTING

def check_locale(locale):
    if locale.upper() in LOCALE_SUPPORTING:
        return locale
    else:
        raise ValueError("Unnsupported/Unknown locale")