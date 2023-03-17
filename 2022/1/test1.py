import logging

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(message)s', 
                    datefmt='%Y-%m-%d %I:%M:%S',)

with open('data.txt') as f:
    lines = f.read()
    # -> ['1000\n2000\n3000', '4000', ...
    items = [ s for s in lines.split("\n\n") ]
    # -> [['1000', '2000', '3000'], ['4000'] ...
    items = [ i.split('\n') for i in items ]
    numeric_items = []
    for item in items:
        # -> [[1000, 2000, 3000], [4000]
        numeric_items.append([ int(j) for j in item ])

    logging.debug(f"Reading in items: {numeric_items}")

# sort sums in ascending order
calorie_sums = sorted([ sum(i) for i in numeric_items ])
highest_calories = calorie_sums[-1]
top_three = sum(calorie_sums[-3:])
logging.info("Part 1 result is {}".format(highest_calories))
logging.info("Part 2 result is {}".format(top_three))
