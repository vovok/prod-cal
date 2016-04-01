#!/usr/bin/env python
# -*- coding: utf-8 -*-

class ProdDict(dict):
    def is_value(self, year, month, day):
        path = self[year][month]
        if path:
            if day in path:
                return True
            else:
                return False
