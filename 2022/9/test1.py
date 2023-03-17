import logging
import pandas as pd
import numpy as np

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s %(message)s', 
                    datefmt='%Y-%m-%d %I:%M:%S',)

with open('data.txt') as f:
    moves = [x.strip() for x in f.readlines()]

logging.debug(f"Input is \n{moves}")

H = { "curr_loc": [0,0], "prev_loc": [0,0] }
T = { "curr_loc": [0,0], "prev_loc": [0,0] }

logging.debug(f"Initially: H={H} & T={T}")

def move(m):
    """
    Make H move as instructed, e.g. 'R 4'
    Make T follow H if needed
    """
    dir = m.split(' ')[0]
    n = int(m.split(' ')[1])

    for i in range(n):
        logging.debug(f"Before round {i+1}/{n} of {m}, status H={H} & T={T}")
        # use list() constructor to avoid creating references instead of assigning values
        H['prev_loc'] = list(H['curr_loc'])
        T['prev_loc'] = list(T['curr_loc'])
        match dir:
            case 'R':
                H['curr_loc'][0] += 1
            case 'L':
                H['curr_loc'][0] -= 1
            case 'U':
                H['curr_loc'][1] += 1
            case 'D':
                H['curr_loc'][1] -= 1

        if not neighbors(H['curr_loc'], T['curr_loc']):
            # put T where H was in previous round
            logging.debug(f"Drifting apart, moving T: {T['curr_loc']} -> {H['prev_loc']}")
            T['curr_loc'] = list(H['prev_loc'])
            t_loci.append(tuple(T['curr_loc']))

    return None

def neighbors(x1, x2) -> bool:
    """
    Are two points neighbors, either adjacent or diagonally
    """
    horiz_dist = abs(x2[0] - x1[0])
    vert_dist = abs(x2[1] - x1[1])
    are_neighbors = horiz_dist < 2 and vert_dist < 2
    return are_neighbors

t_loci = [(0,0)]

for m in moves:
    logging.debug(f"Before {m}: H={H} & T={T}")
    move(m)
    logging.debug(f"After {m}: H={H} & T={T}")

answer1 = len(set(t_loci))
answer2=-1
logging.info("Part 1 result is {}".format(answer1))
logging.info("Part 2 result is {}".format(answer2))