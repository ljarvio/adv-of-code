import logging
from aocd import get_data, submit
import pandas as pd

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(message)s', 
                    datefmt='%Y-%m-%d %I:%M:%S',)

aoc_session="53616c7465645f5f5f171457140ed5519a869ed9be9596206cde72df609cb9efb7abb762bb375fecb6ea50304e8a9ca05f46dd48fc3d226c2945514d6d257fc8"
def read_data_in(testing=False):
    if testing:
        stacks = pd.read_fwf('d.txt', names=range(1,4))
        with open('s.txt') as f:
            steps = [d.strip() for d in f.readlines()]
    else:
        stacks = pd.read_fwf('data.txt', names=range(1,10))
        with open('steps.txt') as f:
            steps = [d.strip() for d in f.readlines()]
    
    # make bottom of stack be the first row of data frame
    stacks = stacks.iloc[::-1]
    return stacks, steps

stacks_df, steps = read_data_in(testing=False)

logging.debug(f"Start with \n{stacks_df}")
logging.debug(f"Steps are: {steps}")

stacks = dict()
for c in stacks_df.columns:
    # list(stacks[1].dropna()) -> ['[Z]', '[N]']
    stacks[c] = list(stacks_df[c].dropna())

def move_boxes(step, model='9000'):
    n = int(step.split()[1])
    stack_from = int(step.split()[3])
    stack_to = int(step.split()[5])
    if model == '9000':
        logging.debug(f"one-at-a-time: moving {n} boxes from {stack_from} to {stack_to}")
        for _ in range(n):
            # lift box from stack
            i = stacks[stack_from].pop()
            # put it on top of another
            stacks[stack_to].append(i)
    elif model == '9001':
        logging.debug(f"many-at-a-time: moving {n} boxes from {stack_from} to {stack_to}")
        temp_stack = []
        for _ in range(n):
            # lift box from stack
            i = stacks[stack_from].pop()
            # keep order by prepending
            temp_stack.insert(0,i)
        for t in temp_stack:
            # add one at a time to avoid nested list
            stacks[stack_to].append(t)

    logging.debug(f"Moved. Stacks are now:\n{stacks}")

    return None 

for step in steps:
    move_boxes(step, model='9001')

top_boxes = [stacks[i][-1] for i in stacks]
answer = ''.join(top_boxes).replace('[','').replace(']','')
logging.info("Part 2 result is {}".format(answer))
submit_response = submit(answer, session=aoc_session, year=2022, day=5, part='2', reopen=False, quiet=True)