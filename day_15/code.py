with open('day_15.txt', 'r') as f:
    lines = f.read().split('\n')

class Sensor():
    def __init__(self, position, closest):
        self.position = position
        self.closest = closest
        self.distance = abs(self.closest[0] - self.position[0]) + abs(self.closest[1] - self.position[1])
        self.circumference = set()

        x = self.position[0]
        y = self.position[1]
        d = self.distance

        for Dx in range(d*-1,d+1):
            Dy = d - abs(Dx)
            self.circumference |= {(x+Dx,y+Dy), (x+Dx,y-Dy)}

sensors = []
beacons = []

for line in lines:
    line = line.split()

    Sx = int(line[2][2:-1])
    Sy = int(line[3][2:-1])

    Bx = int(line[8][2:-1])
    By = int(line[9][2:])

    sensor = Sensor((Sx,Sy), (Bx,By))
    sensors.append(sensor)
    beacons.append((Bx,By))

print('Stage 1')

for sensor in sensors:
    x = sensor.position[0]
    y = sensor.position[1]

    for point in sensor.circumference:
        if point[0] < x:
            new_point = (point[0]-1,point[1])
        elif point[0] > x:
            new_point = (point[0]+1,point[1])
        elif point[1] > y and point[0] == x:
            new_point = (point[0],point[1]+1)
        elif point[1] < y and point[0] == x:
            new_point = (point[0],point[1]-1)

        Nx = new_point[0]
        Ny = new_point[1]

        visible = False

        for sensor in sensors:
            Sx = sensor.position[0]
            Sy = sensor.position[1]

            if abs(Sx - Nx) + abs(Sy - Ny) <= sensor.distance:
                visible = True

        if visible == False and 0 <= Nx <= 4000000 and 0 <= Ny <= 4000000:
            print((Nx*4000000)+Ny)
            break