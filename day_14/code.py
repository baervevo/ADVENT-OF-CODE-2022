import sys

with open('day_14.txt', 'r') as f:
    lines = f.read().split('\n')

rocks = []
grains = []

class Rock():
    def __init__(self, position):
        self.position = position

class Sand():
    def __init__(self, i):
        self.position = (500,0)
        self.i = i

    def __eq__(self,o):
        return self.position == o.position

    def neighbours(self):
        x = self.position[0]
        y = self.position[1]

        nbrs = []

        rock_positions = [x.position for x in rocks]
        grain_positions = [x.position for x in grains]

        for V in [(0,1),(-1,1),(1,1)]:
            new_position = (x+V[0],y+V[1])
            if new_position in rock_positions or new_position in grain_positions:
                continue
            else:
                nbrs.append(new_position)

        return nbrs

def fall(grain):
    moves = grain.neighbours()

    if len(moves) == 0 and grain.position == (500,0):
        return grain.i

    while len(moves) != 0:
        grain.position = moves[0]
        if grain.position[1] == floor.position[1] + 1:
            grains.append(grain)
            return None
        moves = grain.neighbours()

    grains.append(grain)
    return None

for line in lines:
    line = line.split(' -> ')
    for i, coordinate in enumerate(line):
        if i == 0: continue

        Ax = int(line[i-1].split(',')[0])
        Bx = int(coordinate.split(',')[0])

        Ay = int(line[i-1].split(',')[1])
        By = int(coordinate.split(',')[1])
        
        if Ax == Bx:
            h = (Ay,By)
            for m in range(min(h),max(h)+1):
                rocks.append(Rock((Ax,m)))
        elif Ay == By:
            h = (Ax,Bx)
            for n in range(min(h),max(h)+1):
                rocks.append(Rock((n,Ay)))

floor = sorted(rocks, key = lambda x : x.position[1], reverse = True)[0]

x = 1
while True:
    h = fall(Sand(x))
    if h is not None:
        print(h)
        break
    x += 1