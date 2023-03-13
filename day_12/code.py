import sys
with open('day_12.txt', 'r') as f:
    lines = f.read().split('\n')

grid = [[ord(x) - 96 for x in line] for line in lines]

class Node():
    def __init__(self, position):
        self.position = position
        self.cost = None

        self.value = grid[self.position[1]][self.position[0]]
        if self.value == -27:
            self.value = 26
        elif self.value == -13:
            self.value = 1

    def __eq__(self, o):
        return self.position == o.position

    def neighbours(self):
        x = self.position[0]
        y = self.position[1]
        ls = []

        for V in [(0,1),(0,-1),(1,0),(-1,0)]:
            x2 = x + V[0]
            y2 = y + V[1]

            if x2 in range(0, len(grid[0])) and y2 in range(0, len(grid)):
                for node in nodes:
                    if node.position == (x2,y2):
                        if self.value - node.value >= -1: ##  >= -1 - part 1, <= 1 - part 2
                            ls.append(node)

        return ls

def dijkstra(start, end = None):
    for node in nodes:
        node.cost = sys.maxsize

    start.cost = 0
    node_list = nodes.copy()

    while node_list:
        node = sorted(node_list, key = lambda x : x.cost)[0]
        node_list.remove(node)

        for neighbour in node.neighbours():
            if neighbour in node_list:
                if node.cost + 1 < neighbour.cost:
                    neighbour.cost = node.cost + 1

                if neighbour == end: ## if neighbour == end - part 1, if neighbour.value == 1 - part 2
                    return end.cost

nodes = []

for y, row in enumerate(grid):
    for x, column in enumerate(row):
        if grid[y][x] == -27:
            end_node = Node((x,y))
            nodes.append(end_node)
        elif grid[y][x] == -13:
            start_node = Node((x,y))
            nodes.append(start_node)
        else:
            nodes.append(Node((x,y)))

length = dijkstra(start_node, end_node) ## dijkstra(start_node, end_node) - part 1, dijkstra(end_node) - part 2
print(length)