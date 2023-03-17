import time
start_time = time.process_time()
from functools import cmp_to_key
from math import prod
import logging

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s %(message)s', 
                    datefmt='%Y-%m-%d %I:%M:%S',)

data = open("data.txt").read().strip()
pairs = [list(map(eval, p.split("\n"))) for p in data.split("\n\n")]

def compare(left, right):
    logging.debug(f"Comparing packets {left} vs {right}")
    # 4 -> [4]
    left = left if isinstance(left, list) else [left]
    right = right if isinstance(right, list) else [right]
    for l, r in zip(left, right):
        # comparing elements
        logging.debug(f"Comparing items {l} vs {r}")
        if isinstance(l, list) or isinstance(r, list):
            # list elements: one or both are lists, call this func recursively
            logging.debug(f"type({l}) == {type(l)} and type({r}) == {type(r)} ")
            diff = compare(l, r)
        else:
            diff = r - l
        if diff != 0:
            # diff > 0 <=> l2 < r2 => RIGHT order
            # diff < 0 <=> l2 > r2 => WRONG order
            logging.debug(f"{l} vs {r} -> Returning {diff}")
            return diff
    # all items equal so far; func has not returned diff after completing
    # iterating left side (= left side ran out of items)
    # returning > 0 signals RIGHT order, < 0 WRONG
    # at this point, 0 would mean identical l & r (same lengths, same elements)
    diff = len(right) - len(left)
    logging.debug(f"{left} vs {right} -> Return {diff} (len(right) - len(left))")
    return diff

# this one-liner is broken down below:
# indices = [ i for i, (l, r) in enumerate(pairs, 1) if compare(l, r) > 0 ]
indices = []
for i, (l, r) in enumerate(pairs, 1):
    logging.debug("-"*60)
    # walrus := assign and evaluate at once
    if (diff := compare(l, r)) > 0:
        indices.append(i)
        logging.debug(f"Accepted pair {i} (diff = {diff}) -> indices = {indices}")
    elif diff < 0:
        logging.debug(f"Declined pair {i} (diff = {diff}) -> indices = {indices}")

print(f"Part 1: {sum(indices)}")
print(f'\nCPU execution time: {(time.process_time() - start_time) * 1000:.4f} ms')

# this one-liner is broken down below:
#packets = sorted([y for x in pairs for y in x] + [[[2]], [[6]]], key=cmp_to_key(compare), reverse=True)
packets = [[[2]], [[6]]]
# flatten the pairs -list
for x in pairs:
    for y in x:
        packets.append(y)

sorted_packets = sorted(packets, key=cmp_to_key(compare), reverse=True)
print(sorted_packets)
print(f"Part 2: {prod([n for n, sorted_packets in enumerate(sorted_packets, 1) if sorted_packets in ([[2]], [[6]])])}")

