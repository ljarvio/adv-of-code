import logging
import ast

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(message)s', 
                    datefmt='%Y-%m-%d %I:%M:%S',)

with open('data.txt') as f:
    lines = f.read()
    # -> ['1000\n2000\n3000', '4000', ...
    pairs = [ s for s in lines.split("\n\n") ]
    # -> [['1000', '2000', '3000'], ['4000'] ...
    items = [ p.split('\n') for p in pairs ]
    data = []
    for item in items:
        #logging.debug(f"item {item}")
        data.append([ ast.literal_eval(j) for j in item ])

# pair indices in which they were in right order
indices = []

for i, d in enumerate(data):
    left_packet, right_packet = d[0], d[1]
    #if not types_are_compatible(left_packet, right_packet):
    #    logging.debug(f"Do type conversion for pair {d}")
    #    #TODO
    #    #continue

    logging.debug(f"Comparing packets {left_packet} vs {right_packet}")
    try:
        # try easy way out, if both are already lists
        if left_packet > right_packet:
            logging.debug(f"Violation: {left_packet} > {right_packet}")
            logging.debug(f"pair {i+1} was NOT in right order")
            continue
        elif left_packet < right_packet:
            logging.debug(f"pair {i+1} was in right order")
            indices.append(i+1)
            logging.debug(f"Pairs {indices} were so far in right order")

            continue
    except TypeError as e:
        logging.debug(f"{repr(e)} -> needs element-wise comparison")

    for left_i, left in enumerate(left_packet):
        right = right_packet[left_i]
        logging.debug(f"Comparing {left} vs {right}")
        # if either is int, convert to list by a -> [a]
        # comparing lists seems to work as required in the task
        if isinstance(left, int): 
            left = [left]
        if isinstance(right, int): 
            right = [right]

        if left > right: 
            logging.debug(f"Violation: {left} > {right}")
            logging.debug(f"pair {i+1} was NOT in right order")
            break
        elif left == right:
            if left_i == len(left_packet) - 1:
                logging.debug(f"Left side ran out of items; pair {i+1} was in right order")
                indices.append(i+1)
                logging.debug(f"Pairs {indices} were so far in right order")
                break
            logging.debug(f"{left} == {right} -> next item")
            continue
        else:
            logging.debug(f"{left} < {right}")
            logging.debug(f"pair {i+1} was in right order")
            indices.append(i+1)
            logging.debug(f"Pairs {indices} were so far in right order")
            break

answer1 = sum(indices)

logging.info(f"Part 1 result is {answer1}")
