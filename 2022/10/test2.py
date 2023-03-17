import logging

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(message)s', 
                    datefmt='%Y-%m-%d %I:%M:%S',)

with open('data.txt') as f:
    data = [x.strip() for x in f.readlines()]

logging.debug(f"Input is \n{data}")

def test_signal_strength(reg):
    if len(reg) in [20, 60, 100, 140, 180, 220]:
        logging.info(f"Signal strength: reg value {reg[-1]}*{len(reg)} = {reg[-1]*len(reg)}")
        milestones.append(reg[-1]*len(reg))


reg = [1]
milestones = []
for d in data:
    # noop|addx
    c = d.split()[0]
    if c == 'noop':
        reg.append(reg[-1])
    else:
        # don't modify reg yet
        wait = True
        v = int(d.split()[1])
        while wait:
            reg.append(reg[-1])
            test_signal_strength(reg)
            # exit while loop and modify reg
            wait = False
        reg.append(reg[-1] + v)
        # is this cycle one of [20, 60, 100, 140, 180, 220] ?
        test_signal_strength(reg)
    
    #logging.debug(f"reg={reg} after {d}")


def sprite_draws(cycle, reg_value):
    sprite_inds = [reg_value-1,reg_value,reg_value+1]
    if cycle in sprite_inds:
        return '#'
    else:
        return '.'

lines = []
line = ""
# go thru register
for i, r in enumerate(reg):
    cycle = i + 1
    position = i % 40
    logging.debug(f"Cycle {cycle}: CRT draws pixel in position {position}")
    pixel = sprite_draws(position, r)
    logging.debug(f"Drawing {pixel} at cycle {cycle} when X={r}")
    line += pixel
    logging.debug(f"Line is now: {line}")
    if cycle in [40,80,120,160,200,240]: 
        lines.append(line)
        logging.debug(f"Lines are now: {lines}")
        line = ""

for i in lines: print(i)
answer2 = "RFKZCPEF"
logging.info("Part 2 result is {}".format(answer2))