import logging
from aocd import get_data, submit

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s %(message)s', 
                    datefmt='%Y-%m-%d %I:%M:%S',)

aoc_session="53616c7465645f5f5f171457140ed5519a869ed9be9596206cde72df609cb9efb7abb762bb375fecb6ea50304e8a9ca05f46dd48fc3d226c2945514d6d257fc8"
lines = get_data(session=aoc_session, year=2022, day=4).splitlines()

n_overlaps = 0
for line in lines:
    a, b = line.split(',')
    a1, a2 = a.split('-')
    b1, b2 = b.split('-')
    a_set = set(range(int(a1),int(a2)+1))
    b_set = set(range(int(b1),int(b2)+1))
    if len(a_set.intersection(b_set)):
        n_overlaps += 1
        logging.debug(f"Found: {a_set} & {b_set}")

logging.info("Part 2 result is {}".format(n_overlaps))
#submit_response = submit(n_overlaps, session=aoc_session, year=2022, day=4, part='2', reopen=False, quiet=True)
