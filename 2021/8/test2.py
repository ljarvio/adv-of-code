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

def decode_unique_length_signals(signal):
    # sort keys first afceg -> acefg
    signal = [''.join(sorted(s)) for s in signal]
    mapping = dict.fromkeys(signal)
    mapping[[s for s in signal if len(s) == 2][0]] = '1'
    mapping[[s for s in signal if len(s) == 4][0]] = '4'
    mapping[[s for s in signal if len(s) == 3][0]] = '7'
    mapping[[s for s in signal if len(s) == 7][0]] = '8'
    return mapping

def signal_from_mapping(mapping, character):
    # convenience function
    # e.g gives you 'cfbegad' when you ask '8'
    for sig, char in mapping.items():
        if char == character: 
            return sig

def decode_output(output, mapping):
    # arg output e.g. ['fdgacbe', 'cefdb', 'cefbgd', 'gcbe']
    # returns number NNNN based on known mapping
    digits = ""
    output = [''.join(sorted(o)) for o in output]
    for o in output:
        digits += mapping[o]
    
    return int(digits)

def decode_by_deduction(mapping):
    #  what single [abcdefg] drops that is also in '1'?
    eight = signal_from_mapping(mapping, '8')
    one = signal_from_mapping(mapping, '1')
    four = signal_from_mapping(mapping, '4')
    # candidates for 6,9,0
    c690 = [s for s in mapping.keys() if len(s) == 6]
    logging.debug(f"candidates 690 {c690}")
    while len(c690) > 0:
        c = c690[0]
        diff = list(set(eight) - set(c))
        logging.debug(f"difference from eight ({eight})to candidate ({c}) is {diff}")
        if diff[0] in one:
            mapping[c] = '6'
            logging.debug(f"deducing {c} as 6 ")
        elif diff[0] in four:
            mapping[c] = '0'
            logging.debug(f"deducing {c} as 0")
        else:
            # the only candidate left with len==6 must be nine
            mapping[c] = '9'
            logging.debug(f"deducing {c} as 9")

        c690.remove(c)
    
    # candidates for 2,3,5
    c235 = [s for s in mapping.keys() if len(s) == 5]
    # NINE is known at this point by virtue of c690
    nine = signal_from_mapping(mapping, '9')
    logging.debug(f"candidates 235 {c235}")
    while len(c235) > 0:
        c = c235[0]
        diff = set(nine) - set(c)
        logging.debug(f"difference from nine ({nine}) to candidate ({c}) is {diff}")
        # common segments between three and one is one itself
        if (set(c) & set(one)) == set(one):
            mapping[c] = '3'
            logging.debug(f"deducing {c} as 3 ")

        # NINE and FIVE differ by one segment only that is also in ONE
        elif len(diff) == 1 and (set(one) & diff):
            mapping[c] = '5'
            logging.debug(f"deducing {c} as 5 ")
        else:
            # the only candidate left with len==5 must be two
            mapping[c] = '2'
            logging.debug(f"deducing {c} as 2")

        c235.remove(c)

    return mapping

def character_decode(signals):
    mapping = decode_unique_length_signals(signals)
    mapping = decode_by_deduction(mapping)
    return mapping

numbers = []
# signals (to be deciphered) and outputs share same indexing
for i, s in enumerate(signals):
    mapping = character_decode(signals[i])
    number = decode_output(outputs[i], mapping)
    numbers.append(number)
    logging.debug(f"Mapping is: \n {mapping}")
    logging.debug(f"Output {outputs[i]} can be decoded to be: {number}")

logging.info(f"Part 2: numbers are {numbers} and their sum is {sum(numbers)}")