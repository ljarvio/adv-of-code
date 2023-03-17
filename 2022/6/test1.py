import logging
from aocd import get_data, submit
import pandas as pd

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s %(message)s', 
                    datefmt='%Y-%m-%d %I:%M:%S',)

aoc_session="53616c7465645f5f5f171457140ed5519a869ed9be9596206cde72df609cb9efb7abb762bb375fecb6ea50304e8a9ca05f46dd48fc3d226c2945514d6d257fc8"
with open('data.txt') as f:
    data = f.readline()
    data = list(data)

logging.debug(f"Input is {data}")

def find_msg_start(data, length):
    for i, x in enumerate(data):
        start_i, end_i = i, i + length
        substring = data[start_i:end_i]
        if len(substring) == len(set(substring)):
            logging.debug(f"Found it: {substring} at index {end_i}")
            return end_i
            
answer1 = find_msg_start(data, 4)
answer2 = find_msg_start(data, 14)

logging.info("Part 1 result is {}".format(answer1))
logging.info("Part 2 result is {}".format(answer2))
submit_response = submit(answer2, session=aoc_session, year=2022, day=6, part='2', reopen=False, quiet=True)