from config import LOCALE_SUPPORTING
from importlib import import_module
from datetime import datetime, timedelta, date

def check_locale(locale):
    if locale.upper() in LOCALE_SUPPORTING:
        return locale
    else:
        raise ValueError("Unnsupported/Unknown locale")

def get_prodcals(locale):
    pc = import_module('prodcal.prodcals.' + locale.lower())
    return pc.NON_WORK_DAY_DICT, pc.WORK_DAY_DICT

def get_date_today(day):
    today = datetime.today().date()
    if u'today' == day:
        return today
    elif u'yesterday' == day:
        return today - timedelta(days=1)
    elif u'tomorrow' == day:
        return today + timedelta(days=1)
    raise ValueError('Unknown string format', day)

def calc_days_by_int(start_date, days_int):
    return start_date + timedelta(days=days_int)

def cast(start_date, end_date):
    if isinstance(start_date, (tuple, list)) and isinstance(end_date, (tuple, list)):
        start_date, end_date = date(*start_date), date(*end_date)

    if isinstance(start_date, str):
        start_date = get_date_today(start_date)
    elif isinstance(start_date, (tuple, list)):
        start_date = date(*start_date)

    if isinstance(end_date, (tuple, list)):
        end_date = date(*end_date)
    elif isinstance(end_date, int):
        end_date = calc_days_by_int(start_date, end_date)

    if isinstance(start_date, date) and isinstance(end_date, date):
        pass
    else:
        raise ValueError("Unknown format for parse")

    return start_date, end_date

def cast_single_date(args):
    if isinstance(args, (str, date, unicode)):
        if isinstance(args, str):
            return get_date_today(args)
        elif isinstance(args, date):
            return args
    elif isinstance(args, (tuple, list)):
        if isinstance(args[0], (str, unicode)):
            return get_date_today(args[0])
        elif isinstance(args[0], int):
            return date(*args)
        elif isinstance(args[0], date):
            return args[0]