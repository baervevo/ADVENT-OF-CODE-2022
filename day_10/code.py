with open('day_10.txt', 'r') as f:
    program = f.read().split('\n')

values = []
X = 1

w = 40
h = 6

for line in program:
    if line == 'noop':
        values.append(X)
    else:
        values.append(X)
        values.append(X)
        X += int(line.split()[1])

def render(cycle):
    drawing_pos = (cycle-1) % w
    middle = values[cycle-1]
    sprite = range(middle-1,middle+2)

    if drawing_pos in sprite:
        return '0'
    else:
        return ' '

crt = list(map(render, range(0,w*h+1)))

for i in range(1,w*h+1,w):
    print(''.join(crt[i:i+w]))