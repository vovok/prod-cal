"""Production calendar for Estonia"""

from prod_dict import ProdDict

NON_WORK_DAY_DICT = ProdDict({
    2016: {1: [1],
           2: [24],
           3: [25],
           4: [],
           5: [],
           6: [23, 24],
           7: [],
           8: [],
           9: [],
           10: [],
           11: [],
           12: [26]}
})

WORK_DAY_DICT = ProdDict({
    2016: {1: [],
           2: [],
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
})
