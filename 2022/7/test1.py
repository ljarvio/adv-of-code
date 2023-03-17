from collections import defaultdict
from itertools import accumulate

dirs = defaultdict(int)

for line in open('testdata.txt'):
    print(dirs)
    match line.split():
        # grand parent dir
        case '$', 'cd', '/': curr = ['']
        # go up one dir -> remove last dir
        case '$', 'cd', '..': curr.pop()
        # update 'working dir'
        case '$', 'cd', x: curr.append(x+'/')
        # ignore, not actionable
        case '$', 'ls': pass
        # ignore, not actionable
        case 'dir', _: pass
        # ignore filename, don't need to know that
        case size, _:
            print(f"size={size}, curr={curr}")
            for p in accumulate(curr):
                print(f"Pointer p={p}")
                dirs[p] += int(size)

print(sum(s for s in dirs.values() if s <= 100_000),
      min(s for s in dirs.values() if s >= dirs[''] - 40_000_000))


#logging.info("Part 1 result is {}".format(answer1))
#logging.info("Part 2 result is {}".format(answer2))

#submit_response = submit(answer1, session=aoc_session, year=2022, day=7, part='1', reopen=False, quiet=True)