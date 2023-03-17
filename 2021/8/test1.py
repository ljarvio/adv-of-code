import logging
import pandas as pd
import numpy as np

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s %(message)s', 
                    datefmt='%Y-%m-%d %I:%M:%S',)

with open('data.txt') as f:
    commands = {'a': [], 'b': []}
    for line in f.readlines():
        # bgeacd dbfag bcadegf agdce dgfbce bgc bdgca aedcgf bc abec | gcdfbe cbea bc gbc
        commands['a'].append(line.split('|')[0].split())
        commands['b'].append(line.split('|')[1].split())

    signals = dict(enumerate(commands['a']))
    outputs = dict(enumerate(commands['b']))

def decode_unique_length(signal_pattern):
    chars_segments = {'1': 2, '4': 4, '7': 3, '8': 7}
    n = len(signal_pattern)
    for k, v in chars_segments.items():
        if v == len(signal_pattern): return k
    return None

unique_patterns = []
for output in outputs.values():
    # output is e.g ['fgae', 'cfgab', 'fg', 'bagce']
    sig_patt = [o for o in output if decode_unique_length(o)]
    # add as match if pattern was id'd based on length
    unique_patterns.append(sig_patt)

n_occurrences = [len(patterns) for patterns in unique_patterns]
logging.info(f"Part 1: number of [1,4,7,8]s is {sum(n_occurrences)}")