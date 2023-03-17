import logging
import pandas as pd
import numpy as np

logging.basicConfig(level = logging.INFO,
                    format = '%(asctime)s %(message)s', 
                    datefmt = '%Y-%m-%d %I:%M:%S',)

with open('data.txt') as f:
        data = f.read()
        data = data.split(',')
        data = [int(d) for d in data]
data = np.array(data)

def reproduce(initial,days):
    # list of len=9: how many fish have timer==1, etc
    # init as [0,0,0,0,0,0,0,0,0]
    fishes = np.zeros(9)
    # read in initial state
    for i in range(fishes.shape[0]):
        fishes[i] = len(np.where(initial == i)[0])
    logging.info(f"Read initial state as {fishes}")

    for d in range(days):
        logging.debug(f"Day {d}: {fishes} totals {sum(fishes)}")
        zeroTo6 = fishes[:7]
        seven8 = fishes[7:]
        newFish = zeroTo6[0]
        # [1,2,3] -> [2,3,1*] ; *) to be updated next
        zeroTo6 = np.roll(zeroTo6,-1)
        # timer==6 for those which were at timer=0 or timer=7
        zeroTo6[-1] += seven8[0]
        # [5,6] -> [6,5*] ; *) to be updated next
        seven8 = np.roll(seven8,-1)
        seven8[-1] = newFish
        fishes = np.concatenate((zeroTo6,seven8))
    return fishes

logging.info("Part 2 result {}".format(np.sum(reproduce(data, 256))))

