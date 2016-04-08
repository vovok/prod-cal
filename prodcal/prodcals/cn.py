"""Production calendar for China"""

from prod_dict import ProdDict

NON_WORK_DAY_DICT = ProdDict({
    2016: {1: [1],
           2: [8, 9, 12],
           3: [],
           4: [],
           5: [2],
           6: [9, 10],
           7: [],
           8: [],
           9: [15, 16],
           10: [3, 7],
           11: [],
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


