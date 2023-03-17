import logging
import pandas as pd
import numpy as np

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s %(message)s', 
                    datefmt='%Y-%m-%d %I:%M:%S',)

with open('data.txt') as f:
    data = [x.strip() for x in f.readlines()]
    df = pd.DataFrame(data)
    df = df[0].str.split("", expand = True)
    # drop 1st and last columns as they're empty
    df = df.iloc[:, 1:-1] 
    df = df.astype(int)
    # 1...10 -> 0...9
    df.columns = range(df.shape[1])

def neighbors(j, i):
    up = None if i == 0 else df[j][i - 1]
    down = None if i == max(df.index) else df[j][i + 1]
    right = None if j == max(df.columns) else df[j + 1][i]
    left = None if j == 0 else df[j - 1][i]
    ns = [up, down, right, left]
    # drop None entries
    ns = [n for n in ns if n is not None]
    return ns

minima = []
for j in df.columns:
    for i in df.index:
        logging.debug(f"Inspecting df[{j}][{i}] = {df[j][i]}")
        adjacent = neighbors(j, i)
        logging.debug(f"adjacents: {adjacent}")
        if all(a > df[j][i] for a in adjacent):
            minima.append(df[j][i])
            logging.debug(f"Found local minimum value {df[j][i]}")

total_risk_level = sum(minima) + len(minima)
logging.info(f"Part 1: ANSWER is {total_risk_level}")