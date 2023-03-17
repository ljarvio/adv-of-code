debug = True
with open('data.txt') as f:
        ns = f.read().splitlines()
ns = [int(i) for i in ns]
diffs = [ b - a for a, b in zip(ns, ns[1:])]
p_diffs = [d for d in diffs if d > 0]

if debug:
    print(zip(ns, ns[1:]))
    print(len(ns))
    print(ns[:10])
    print(diffs[:10])
    print(p_diffs[:10])
print(f"There are {len(p_diffs)} positive differences")

