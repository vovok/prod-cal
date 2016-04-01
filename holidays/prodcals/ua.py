#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Production calendar for Ukraine"""

from prod_dict import ProdDict

NON_WORK_DAY_DICT = ProdDict({
    2016: {1: [1, 7],
           2: [],
           3: [8],
           4: [],
           5: [2, 3, 9],
           6: [20, 28],
           7: [],
           8: [24],
           9: [],
           10: [14],
           11: [],
           12: []}
})


WORK_DAY_DICT = ProdDict({
    2016: {1: [16],
           2: [],
           3: [12],
           4: [],
           5: [],
           6: [],
           7: [2],
           8: [],
           9: [],
           10: [],
           11: [],
           12: []}
})
