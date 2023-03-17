import logging
import pandas as pd
import numpy as np

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s %(message)s', 
                    datefmt='%Y-%m-%d %I:%M:%S',)

with open('data.txt') as f:
    data = [x.strip() for x in f.readlines()]

logging.debug(f"Input is \n{data}")

def test_signal_strength(reg):
    if len(reg) in [20, 60, 100, 140, 180, 220]:
        logging.info(f"Signal strength: reg value {reg[-1]}*{len(reg)} = {reg[-1]*len(reg)}")
        milestones.append(reg[-1]*len(reg))


reg = [1]
milestones = []
for d in data:
    # noop|addx
    c = d.split()[0]
    if c == 'noop':
        reg.append(reg[-1])
    else:
        # don't modify reg yet
        wait = True
        v = int(d.split()[1])
        while wait:
            reg.append(reg[-1])
            test_signal_strength(reg)
            # exit while loop and modify reg
            wait = False
        reg.append(reg[-1] + v)
        # is this cycle one of [20, 60, 100, 140, 180, 220] ?
        test_signal_strength(reg)
    
    logging.debug(f"reg={reg} after {d}")

answer1 = sum(milestones)
logging.info("Part 1 result is {}".format(answer1))