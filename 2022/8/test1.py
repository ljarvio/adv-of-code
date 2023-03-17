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

logging.debug(f"Input is \n{df}")

def visible(i, j, direction) -> bool:
    """
    Checks if tree at (i,j) is visible from outside the forest
    """
    t = df[j][i]
    logging.debug(f"Looking at tree of height {t}")
    match direction:
        case 'up': slice = df.loc[:i-1,j]
        case 'down': slice = df.loc[i+1:,j]
        case 'right': slice = df.loc[i,j+1:]
        case 'left': slice = df.loc[i,:j-1]
    logging.debug(f"Looking at slice {list(slice)}")
    blocked = any(x >= t for x in list(slice))
    logging.debug(f"Deducing: blocked={blocked}")
    return not blocked

def scenic_score(i, j, direction) -> int:
    """
    Calculates scenic score (=how many trees are visible) for tree at (i,j) in given direction
    """
    t = df[j][i]
    logging.debug(f"Looking {direction} from tree of height {t}")
    match direction:
        case 'up': slice = df.loc[:i-1,j]
        case 'down': slice = df.loc[i+1:,j]
        case 'right': slice = df.loc[i,j+1:]
        case 'left': slice = df.loc[i,:j-1]

    score = viz_score(slice, t, direction)
    logging.debug(f"Looking at slice {list(slice)}: score={score}")
    return score

def viz_score(slice, t, direction) -> int:
    """
    Helper for scenic_score() to calculate scenic score
    """
    slice = list(slice)
    z = 0
    # iterate the right direction; away from t (tree of interest)
    if direction in ['up', 'left']: slice.reverse()
    for i in slice:
        z += 1
        if i >= t: 
            break
    return z

# part 1
visible_trees = 0
for j in df.columns:
    for i in df.index:
        # boolean array whether tree is visible from different directions
        viz = [ visible(j,i,direction='up'),
                visible(j,i,direction='down'),
                visible(j,i,direction='right'),
                visible(j,i,direction='left')
              ]
        if any(viz): 
            # this tree is visible from at least one direction
            logging.debug(f"d({j},{i}) is visible: {viz}")
            visible_trees += 1

# part 2
max_score = 0
for j in df.columns:
    for i in df.index:
        # calculate score for all directions
        viz = [ scenic_score(j,i,direction='up'),
                scenic_score(j,i,direction='down'),
                scenic_score(j,i,direction='right'),
                scenic_score(j,i,direction='left')
              ]
        logging.debug(f"d({j},{i}) has score array: {viz}")
        s = np.prod(viz)
        # check if we have a new top scorer tree
        if s > max_score: max_score = s

logging.info("Part 1 result is {}".format(visible_trees))
logging.info("Part 2 result is {}".format(max_score))