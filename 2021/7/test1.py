import logging
import pandas as pd
import numpy as np

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s %(message)s', 
                    datefmt='%Y-%m-%d %I:%M:%S',)

with open('data.txt') as f:
        data = f.read().split(',')
        data = [int(d) for d in data]

def cost1(data, x):
    cost = 0
    for d in data:
        cost += abs(d - x)
    return cost

def cost2(data, x):
    cost = 0
    for d in data:
        distance = abs(d - x)
        cost += distance*(distance + 1) / 2
    return cost

def calc_cost(data, cost_function):
    costs = np.zeros(max(data))
    for i, x in enumerate(horizontal_positions):
        costs[i] = cost_function(data, x)
        logging.debug(f"x,cost = {x},{costs[i]}")    
    return costs

horizontal_positions = range(0, max(data))
costs1 = calc_cost(data, cost1)
costs2 = calc_cost(data, cost2)
logging.info(f"Part 1 minimum cost at x={np.argmin(costs1)}: {min(costs1)}")
logging.info(f"Part 2 minimum cost at x={np.argmin(costs2)}: {min(costs2)}")