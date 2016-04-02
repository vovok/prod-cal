#!/usr/bin/env python
# -*- coding: utf-8 -*-

class ProdDict(dict):
    def is_value(self, day):
        path = self[day.year][day.month]
        if path:
            if day.day in path:
                return True
            else:
                return False
