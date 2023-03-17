import logging
import string

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(message)s', 
                    datefmt='%Y-%m-%d %I:%M:%S',)

item_priorities = list(string.ascii_letters)

with open('data.txt') as f:
    lines = f.read()
    packs = [ s for s in lines.split("\n") ]

def common_item_in_groups(items):
    # items e.g. ['abc', 'cde', 'fgc']
    # [{'a', 'b', 'c'}, {'e', 'c', 'd'}, {'f', 'g', 'c'}]
    groups = [set(i) for i in items]
    common_item = set.intersection(*groups)
    return list(common_item)[0]

def priority_of_item(item):
    return item_priorities.index(item) + 1

total = 0
for i in range(0, len(packs), 3):
    # 0:3, 3:6, ..., (len-3):len
    items = list(packs[i:i+3])
    if len(items) < 3: continue #empty row
    logging.debug(f"Processing items {items}")
    common_item = common_item_in_groups(items)
    logging.debug(f"Common item is {common_item}")
    total += priority_of_item(common_item)

logging.info("Part 2 result is {}".format(total))
