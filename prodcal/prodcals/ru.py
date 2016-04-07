"""Production calendar for Russian Federation"""

from prod_dict import ProdDict

NON_WORK_DAY_DICT = ProdDict({
    2016: {1: [1, 4, 5, 6, 7, 8],
           2: [22, 23],
           3: [7, 8],
           4: [],
           5: [1, 2, 3, 9],
           6: [13],
           7: [],
           8: [],
           9: [],
           10: [],
           11: [4],
           12: []}
})

WORK_DAY_DICT = ProdDict({
    2016: {1: [],
           2: [20],
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