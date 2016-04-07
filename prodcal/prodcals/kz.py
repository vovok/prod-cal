"""Production calendar for Kazakhstan"""

from prod_dict import ProdDict

NON_WORK_DAY_DICT = ProdDict({
    2016: {1: [1, 4],
           2: [],
           3: [8, 21, 22, 23],
           4: [],
           5: [2, 9, 10],
           6: [],
           7: [6],
           8: [30],
           9: [13],
           10: [],
           11: [],
           12: [1, 16, 19]}
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