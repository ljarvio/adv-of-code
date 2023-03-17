import logging
import numpy as np

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s %(message)s', 
                    datefmt='%Y-%m-%d %I:%M:%S',)

test_monkeys = {
            0: {
                "items": [63, 84, 80, 83, 84, 53, 88, 72],
                "operation": lambda x: x*11,
                "test": {"mod": 13, "t": 4, "f": 7},
                "inspected": 0
                },
            1: {
                "items": [67, 56, 92, 88, 84],
                "operation": lambda x: x + 4,
                "test": {"mod": 11, "t": 5, "f": 3},
                "inspected": 0
                },
            2: {
                "items": [52],
                "operation": lambda x: x*x,
                "test": {"mod": 2, "t": 3, "f": 1},
                "inspected": 0
                },
            3: {
                "items": [59, 53, 60, 92, 69, 72],
                "operation": lambda x: x + 2,
                "test": {"mod": 5, "t": 5, "f": 6},
                "inspected": 0
                },
            4: {
                "items": [61, 52, 55, 61],
                "operation": lambda x: x + 3,
                "test": {"mod": 7, "t": 7, "f": 2},
                "inspected": 0
                },
            5: {
                "items": [79, 53],
                "operation": lambda x: x + 1,
                "test": {"mod": 3, "t": 0, "f": 6},
                "inspected": 0
                },
            6: {
                "items": [59, 86, 67, 95, 92, 77, 91],
                "operation": lambda x: x + 5,
                "test": {"mod": 19, "t": 4, "f": 0},
                "inspected": 0
                },
            7: {
                "items": [58, 83, 89],
                "operation": lambda x: x*19,
                "test": {"mod": 17, "t": 2, "f": 1},
                "inspected": 0
                }
            }

#logging.debug(f"Input is \n{test_monkeys}")
#def m0(x):
#    return x * 11
#def m1(x):
#    return x + 4
#def m2(x):
#    return x * x
#def m3(x):
#    return x + 2
#def m4(x):
#    return x + 3
#def m5(x):
#    return x + 1
#def m6(x):
#    return x + 5
#def m7(x):
#    return x * 19

modulo = np.prod([m["test"]["mod"] for m in test_monkeys.values()])

n_rounds = 10_000
logging.info(f"#rounds {n_rounds}:")
for round in range(1, n_rounds+1): 
    if not round % 1000: 
        logging.info(f"Starting round {round}")
        pass
    for x, m in test_monkeys.items():
        # if monkey has no items, goto next monkey
        while m["items"]:
            logging.debug(f"Monkey {x} is inspecting:")
            m["inspected"] += 1
            # take out 1st item on list
            i = m["items"].pop(0)
            i = m["operation"](i)
            # the modulo trick to keep i < modulo
            i = i % modulo
            if i % m["test"]["mod"] == 0:
                x2 = m["test"]["t"]
            else:
                x2 = m["test"]["f"]
            test_monkeys[x2]["items"].append(i)
            logging.debug(f"Item with worry level {i} is thrown to monkey {x2}...")
            logging.debug(f"... Monkey {x2} has now items {test_monkeys[x2]['items']}")


inspected_list = [ x['inspected'] for i, x in test_monkeys.items() ]
# multiply top two monkeys' inspected -counts
answer1 = np.prod(sorted(inspected_list)[-2:])

logging.info(f"Inspected by monkey: {inspected_list}")
logging.info(f"Part 1 result is {answer1}")