"""Production calendar for Belarus"""

from prod_dict import ProdDict

NON_WORK_DAY_DICT = ProdDict({
    2016: {1: [1, 7, 8],
           2: [],
           3: [7, 8],
           4: [],
           5: [9, 10],
           6: [],
           7: [],
           8: [],
           9: [],
           10: [],
           11: [7],
           12: []}
})

WORK_DAY_DICT = ProdDict({
    2016: {1: [16],
           2: [],
           3: [5],
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

