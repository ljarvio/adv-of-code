import logging
import pandas as pd
import numpy as np

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(message)s', 
                    datefmt='%Y-%m-%d %I:%M:%S',)

def is_horiz_vert(line):
    # line e.g. [['445', '187'], ['912', '654']]
    # vertical: 1st parameter is const (at i=0)
    vert = line[0][0] == line[1][0]
    # horizontal: 2nd parameter is const (at i=1)
    horiz = line[0][1] == line[1][1]
    return horiz or vert

def points_on_line(line):
    y1, x1 = int(line[0][0]), int(line[0][1])
    y2, x2 = int(line[1][0]), int(line[1][1])
    # length is max(dx,dy)
    length = max(abs(x2 - x1), abs(y2 - y1)) + 1
    xs = np.linspace(x1, x2, num = length)
    ys = np.linspace(y1, y2, num = length)
    return ys, xs

with open('data.txt') as f:
        data = f.read().splitlines()

# an element in lines will be e.g. ['445,187', '912,654']
lines = [d.split(" -> ") for d in data]
arrows = []
for line in lines:
    # a2b e.g. [['445', '187'], ['912', '654']]
    a2b = [e.split(',') for e in line]
    arrows.append(a2b)

df = pd.DataFrame(np.zeros((1000, 1000)))

for i, line in enumerate(arrows):
    ys, xs = points_on_line(line)
    logging.debug(f"{i}/{len(arrows)}: line = {line} ")
    # insert/mark them into df
    for y,x in zip(ys,xs):
        df[y][x] += 1

# calc how many df[y][x] >= 2
n_overlapping_locations = (df >= 2).apply(np.count_nonzero).sum()
logging.info(f"ANSWER = {n_overlapping_locations}")

