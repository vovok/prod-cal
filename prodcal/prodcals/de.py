"""Production calendar for Germany"""

from prod_dict import ProdDict

NON_WORK_DAY_DICT = ProdDict({
    2016: {1: [1],
           2: [10],
           3: [28],
           4: [],
           5: [5, 16],
           6: [],
           7: [],
           8: [],
           9: [],
           10: [3],
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


