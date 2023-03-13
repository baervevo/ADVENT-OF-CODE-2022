import time
from itertools import *

def exposedSurface(cubes):
    e = 0
    for cube in cubes:
        x, y, z = cube[0], cube[1], cube[2]
        a, b = (0,1), (0,-1)
        vectors = {x for x in product(a,a,a) if sum(x) == 1} | {x for x in product(b,b,b) if sum(x) == -1}

        for V in vectors:
            new_cube = (x + V[0], y + V[1], z + V[2])
            if new_cube not in cubes:
                e += 1
    return e

def edgeFind(graph, start, cubes):
    q, v = [], set()
    q.append(start)
    v |= {start}

    while q:
        node = q.pop(0)

        x, y, z = node[0], node[1], node[2]
        a, b = (0,1), (0,-1)
        vectors = {x for x in product(a,a,a) if sum(x) == 1} | {x for x in product(b,b,b) if sum(x) == -1}

        for V in vectors:
            new_cube = (x + V[0], y + V[1], z + V[2])
            if new_cube in graph and new_cube not in cubes and new_cube not in v:
                v |= {new_cube}
                q.append(new_cube)

    return v

a = time.perf_counter()

with open('day_18.txt', 'r') as f:
    lines = f.read().split('\n')

cubes = set()
for line in lines:
    line = line.split(',')
    cubes |= {(int(line[0]), int(line[1]), int(line[2]))}

surface = exposedSurface(cubes)
print(surface)

b = time.perf_counter()
print(round((b-a),5))
b = time.perf_counter()

all_x = [c[0] for c in cubes]
all_y = [c[1] for c in cubes]
all_z = [c[2] for c in cubes]

x_range = range(min(all_x)-1, max(all_x)+2)
y_range = range(min(all_y)-1, max(all_y)+2)
z_range = range(min(all_z)-1, max(all_z)+2)
start = (x_range[0],y_range[0],z_range[0])

space = set(product(x_range,y_range,z_range))
exterior_space = edgeFind(space, start, cubes)

droplet = space.difference(exterior_space)

surface2 = exposedSurface(droplet)
print(surface2)

c = time.perf_counter()
print(round((c-b),5))