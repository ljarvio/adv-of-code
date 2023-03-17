import pandas as pd
debug = True

with open('data.txt') as f:
        ns = f.read().splitlines()
ns = [int(i) for i in ns]
numbers_series = pd.Series(ns)
windows = numbers_series.rolling(3)
moving_sums = windows.sum().tolist()
moving_sums = moving_sums[2:]

diffs = [ b - a for a, b in zip(moving_sums, moving_sums[1:])]
p_diffs = [d for d in diffs if d > 0]

if debug:
    print(f"moving_sums: {moving_sums[:10]}")
    print(f"p_diffs: {p_diffs[:10]}")
    
print(f"There are {len(p_diffs)} positive differences")

