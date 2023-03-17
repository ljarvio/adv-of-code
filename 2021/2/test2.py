
import unittest
import logging

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s %(message)s', 
                    datefmt='%Y-%m-%d %I:%M:%S',)

class TestTrackSubmarine(unittest.TestCase):
    logging.info('Running tests')
    def test_track_submarine(self):
        # example from https://adventofcode.com/2021/day/2
        commands = ['forward 5', 'down 5', 'forward 8', 'up 3', 'down 8', 'forward 2']
        self.assertEqual(track_submarine(commands), {'x': 15, 'y': 60, 'a': 10})

def track_submarine(commands: list) -> dict:
    # bookkeeping
    d = {'x': 0, 'y': 0, 'a': 0}
    
    for c in commands:
        logging.debug(f"About to process command: {c}")
        logging.debug(f"Prior state of dict is {d}")
        cmd_type = c.split(' ')[0]
        X = int(c.split(' ')[1])
        if cmd_type == 'forward':
            d['x'] += X
            d['y'] += d['a'] * X
        if cmd_type == 'up':
            d['a'] -= X
        if cmd_type == 'down':
            d['a'] += X
        logging.debug(f"Post state of dict is {d}")
    return d

if __name__ == '__main__':
    unittest.main()
    with open('data.txt') as f:
        commands = f.read().splitlines()
    d = track_submarine(commands)
    print(f"ANSWER = {d['x']*d['y']}")