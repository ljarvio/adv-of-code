import logging
import pandas as pd
import numpy as np

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(message)s', 
                    datefmt='%Y-%m-%d %I:%M:%S',)

with open('data.txt') as f:
    data = [d.strip() for d in f.readlines()]

points_from_char = {")": 3, "]": 57, "}": 1197, ">": 25137}
pairs = {"(": ")", "[": "]", "{": "}", "<": ">"}

def corrupt_or_incomplete(line):
    # returns either 1st illegal character encountered OR
    # the sequence that would complete the line (=expect)
    logging.debug(f"Processing {line}")
    # "<>" -> ['<','>']
    chars = list(line)
    expect = []
    for c in chars:
        # closing char encountered
        if len(expect) and c == expect[0]:
            expect.pop(0)
            #logging.debug(f"{c}: expected list is now {expect}")
        # a new opening char
        elif c in pairs.keys():
            expect.insert(0, pairs[c])
            #logging.debug(f"{c}: expected list is now {expect}")
        else:
            #logging.debug(f"{c}: illegal character; expected {expect[0]}")
            return c

    return expect

def score_string(line):
    logging.debug(f"Processing {line}")
    # "<>" -> ['<','>']
    chars = list(line)
    scoring_table = {")": 1, "]": 2, "}": 3, ">": 4}
    score = 0
    for c in chars:
        score = 5*score + scoring_table[c]
    return score

testline = '<{([([[(<>()){}]>(<<{{'
total_points = 0
total_points_completion = []
for d in data:
    feedback = corrupt_or_incomplete(d)
    # line was corrupt
    if type(feedback) is str:
        #logging.debug(f"Line {d} was corrupted by {feedback}")
        total_points += points_from_char[feedback]
    # line is incomplete
    elif type(feedback) is list:
        total_points_completion.append(score_string(feedback))
        logging.debug(f"Line {d} was incomplete: total_points is now {total_points_completion}")

    
logging.info(f"Part 1: total points = {total_points}")
logging.info(f"Part 2: total points = {np.median(total_points_completion)}")
