"""Production calendar for Georgia"""

from prod_dict import ProdDict

NON_WORK_DAY_DICT = ProdDict({
    2016: {1: [1, 2, 7, 19],
           2: [],
           3: [3, 8],
           4: [9, 29, 30],
           5: [2, 9, 12, 26],
           6: [],
           7: [],
           8: [28],
           9: [],
           10: [14],
           11: [23],
           12: []}
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

