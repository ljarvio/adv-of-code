import logging
import string

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s %(message)s', 
                    datefmt='%Y-%m-%d %I:%M:%S',)

item_priorities = list(string.ascii_letters)

with open('data.txt') as f:
    lines = f.read()
    packs = [ s for s in lines.split("\n") ]

def common_item_in_groups(group_A, group_B):
    common_item = set(group_A) & set(group_B)
    return list(common_item)[0]

def priority_of_item(item):
    return item_priorities.index(item) + 1

total = 0
for p in packs:
    items = list(p)
    half = int(len(items)/2)
    if not half: continue #empty row
    logging.debug(f"Processing items {items}")
    common_item = common_item_in_groups(items[:half], items[half:])
    logging.debug(f"Common item is {common_item}")
    total += priority_of_item(common_item)

logging.info("Part 1 result is {}".format(total))
