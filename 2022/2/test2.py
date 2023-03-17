import logging

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s %(message)s', 
                    datefmt='%Y-%m-%d %I:%M:%S',)

opp = {'A': 'rock', 'B': 'paper', 'C': 'scissors'}
me = {'X': 'rock', 'Y': 'paper', 'Z': 'scissors'}
rules = {'scissors': 'paper', 'paper': 'rock', 'rock': 'scissors'}
inv_rules = {v: k for k, v in rules.items()}

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

def sign_to_play(opponent_sign, my_hint):
    # e.g. scissors <- 'C' 
    opponent_hand = opp[opponent_sign]
    rigged = {'X': 'lose', 'Y': 'draw', 'Z': 'win'}
    # e.g. 'win' <- 'Z'
    desired_result = rigged[my_hint]
    if desired_result == 'draw':
        # 'scissors' <- 'scissors'
        hand_to_play = opponent_hand
    elif desired_result == 'lose':
        # 'paper' <- 'scissors'
        hand_to_play = rules[opponent_hand]
    else:
        # choose winning hand 'rock'
        hand_to_play = inv_rules[opponent_hand]
    
    # if I need to play e.g. 'scissors', I need to sign 'Z'
    my_sign = [i for i in me if me[i] == hand_to_play][0]
    return my_sign

total = 0
for p in plays:
    my_sign = sign_to_play(p[0], p[1])
    points = points_from_play(p[0], my_sign)
    logging.debug(f"Scoring {p}: {points} points")
    total += points

logging.info("Part 2 result is {}".format(total))
