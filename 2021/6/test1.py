import logging
import pandas as pd
import numpy as np

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s %(message)s', 
                    datefmt='%Y-%m-%d %I:%M:%S',)

with open('data.txt') as f:
        data = f.read()
        data = data.split(',')
        data = [int(d) for d in data]

def update_timer(current_timer):
    if current_timer == 0: 
        return adult_timer_start
    else:
        return current_timer - 1

MAX_DAYS = 80
newborn_timer_start = 8
adult_timer_start = 6
days = 0
logging.info(f"Starting to simulate...")

while days < MAX_DAYS:
    logging.info(f"{len(data)} fish after {days} days")
    n_new_fish = 0
    days += 1
    for i, f in enumerate(data):
        timer_prev = f
        timer = update_timer(f)
        data[i] = timer
        if timer == adult_timer_start and timer_prev == 0:
            #logging.debug(f"timer: {timer} for fish {f} at {i}")
            n_new_fish += 1
    if n_new_fish: data += [newborn_timer_start]*n_new_fish
    logging.debug(f"new: {n_new_fish} | {days} days: {data}")

logging.info(f"ANSWER = {len(data)}")

