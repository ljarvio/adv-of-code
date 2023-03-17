import logging

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(message)s', 
                    datefmt='%Y-%m-%d %I:%M:%S',)

with open('data.txt') as f:
    lines = f.read().split('\n')

n_subsets = 0
for line in lines:
    a, b = line.split(',')
    a1, a2 = a.split('-')
    b1, b2 = b.split('-')
    a_set = set(range(int(a1),int(a2)+1))
    b_set = set(range(int(b1),int(b2)+1))
    if set(a_set).issubset(b_set) or set(b_set).issubset(a_set):
        n_subsets += 1
        logging.debug(f"Found: {a_set} & {b_set}")

logging.info("Part 1 result is {}".format(n_subsets))
