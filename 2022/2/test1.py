import logging
import pandas as pd
import numpy as np

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(message)s', 
                    datefmt='%Y-%m-%d %I:%M:%S',)

opp = {'A': 'rock', 'B': 'paper', 'C': 'scissors'}
me = {'X': 'rock', 'Y': 'paper', 'Z': 'scissors'}
rules = {'scissors': 'paper', 'paper': 'rock', 'rock': 'scissors'}
with open('data.txt') as f:
    lines = f.read()
    plays = [ s for s in lines.split("\n") ]
    plays = [ i.split(' ') for i in plays ]

def points_from_play(opponent_sign, my_sign):
    opponent_hand = opp[opponent_sign]
    my_hand = me[my_sign]
    scoring_table = {'win': 6, 'draw': 3, 'lose': 0}
    points_from_hand_table = {'scissors': 3, 'paper': 2, 'rock': 1}
    # seed total_points
    total_points = points_from_hand_table[my_hand]
    if opponent_hand == my_hand:
        total_points += scoring_table['draw']
    elif (my_hand, opponent_hand) in rules.items():
        total_points += scoring_table['win']
    else:
        # hypothetical support for getting points also from losing
        total_points += scoring_table['lose']
    return total_points

total = 0
for p in plays:
    points = points_from_play(p[0], p[1])
    logging.debug(f"Scoring {p}: {points} points")
    total += points

logging.info("Part 1 result is {}".format(total))
