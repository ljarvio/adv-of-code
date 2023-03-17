import heapq
from math import inf

# pathfinding: https://www.redblobgames.com/pathfinding/a-star/introduction.html
# from https://www.reddit.com/r/adventofcode/comments/zjnruc/comment/j113gbh/?utm_source=share&utm_medium=web2x&context=3

def nearest_neighbors(x, y):
    return [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]

def climb(start, end, heightmap): 
    visited = {start} 
    queue = list()
    length = 0
    while start != end:
        for q in nearest_neighbors(*start):
            # .get gives Inf if key does not exist -> diff = -Inf
            diff = heightmap[start] - heightmap.get(q, inf)
            if q not in visited and diff >= -1:
                visited.add(q)
                heapq.heappush(queue, (diff, length + 1, q))
        if not queue:
            return inf
        _, length, start = heapq.heappop(queue)
    return length

# INPUT PARSING
with open('data.txt') as f: 
    heightmap = dict() 
    min_height_pos = list() 
    for y, row in enumerate(f.read().splitlines()): 
        for x, h in enumerate(row): 
            match h: 
                case "S": 
                    start, h = (x, y), "a" 
                    min_height_pos.append((x, y)) 
                case "E": 
                    end, h = (x, y), "z" 
                case "a": 
                    min_height_pos.append((x, y)) 
            heightmap[(x, y)] = ord(h) - 97

# PART 1
print(climb(start, end, heightmap))

# PART 2
print(min(climb(p, end, heightmap) for p in min_height_pos))
