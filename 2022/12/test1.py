import logging
import pandas as pd
import numpy as np
import string

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(message)s', 
                    datefmt='%Y-%m-%d %I:%M:%S',)

fname = 'data' + '.txt'
with open(fname) as f:
    data = [x.strip() for x in f.readlines()]
    df = pd.DataFrame(data)
    df = df[0].str.split("", expand = True)
    # drop 1st and last columns as they're empty
    df = df.iloc[:, 1:-1] 
    df = df.astype(str)
    # 1...10 -> 0...9
    df.columns = range(df.shape[1])

logging.debug(f"Input is \n{df}")
# start and end locations
S, E = (0,0), (2,5)
#S, E = (20,0), (20,46) # data.txt
letter_to_number = {'S': 0, 'E': 25}
for v, L in enumerate(list(string.ascii_lowercase)):
    letter_to_number[L] = v
# replace 'a' -> 0, 'b' -> 1, ..., z -> 25 & S -> 'a', E -> 'z'
df2 = df.replace(letter_to_number)
logging.debug(f"Input as numbers is \n{df2}")
df2.to_csv(fname + '.csv', index=False, header=False, sep ='\t')
answer1 = -1
logging.info("Part 1 result is {}".format(answer1))