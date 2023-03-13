from itertools import *
from collections import defaultdict
from math import inf as INF
import time

class Valve():
    def __init__(self, label, rate, neighbours):
        self.label = label
        self.rate = rate
        self.neighbours = neighbours
        self.distances = defaultdict(lambda: INF)

    def convertLabels(self, valves):
        l = []
        for neighbour in self.neighbours:
            for valve in valves:
                if valve.label == neighbour:
                    l.append(valve)

        self.neighbours = l

def floyd_warshall(g):
    for node in g:
        distances = node.distances

        distances[node] = 0

        for nb in node.neighbours:
            distances[nb] = 1

    for a, b, c in product(g,g,g):
        bc, ba, ac = b.distances[c], b.distances[a], a.distances[c]

        if ba + ac < bc:
            b.distances[c] = ba + ac

def pathFind(valves, here, t = 26, path = {}):
    for valve in valves:
        new_t = t - (here.distances[valve] + 1)

        if t < 2:
            continue

        new_path = path.copy()
        new_path[valve] = new_t
        yield from pathFind(valves - {valve}, valve, new_t, new_path)

    yield path

def score(path):
    t = 0
    for step, x in path.items():
        t += step.rate * x
    return t

a = time.perf_counter()

with open('day_16.txt', 'r') as f:
    lines = f.read().split('\n')

valves = []
for line in lines:
    line = line.split()

    label = line[1]
    flow = int(line[4].strip('rate=')[:-1])
    neighbours = [x.strip(',') for x in line[9:]]

    v = Valve(label, flow, neighbours)
    valves.append(v)

    if v.label == 'AA':
        start_valve = v

for valve in valves:
    valve.convertLabels(valves)
    
floyd_warshall(valves)

good = set([valve for valve in valves if valve.rate != 0])

solutions = list(pathFind(good, start_valve))
    
best = max(map(score, solutions))
print(best)

b = time.perf_counter()
print(round((b-a), 2))
c = time.perf_counter()

best = 0
max_scores = defaultdict(int)
for solution in solutions:
    v = frozenset(solution)
    s = score(solution)

    if s > max_scores[v]: max_scores[v] = s

h = []
for (s1, score1), (s2, score2) in combinations(max_scores.items(), 2):
    if not s1 & s2:
        h.append(score1+score2)
        
print(max(h))

d = time.perf_counter()
print(round((d-c),2))