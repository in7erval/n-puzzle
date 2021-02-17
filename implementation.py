import collections
import heapq
import random as r

class SimpleGraph:

    def __init__(self):
        self.edges = dict()

    def neighbors(self, id):
        return self.edges[id]


def read_map(name_map):
    with open(name_map) as f:
        lines = f.readlines()
        height = len(lines)
        width = len(lines[0].replace(' .', ' ').replace('##', '#').replace('\n', ''))
        i, j = 0, 0
        walls = list()
        for line in lines:
            line = line.replace(' .', '.').replace('##', '#').strip()
            j = 0
            for x in line:
                if x == '#':
                    walls.append((j, i))
                j = j + 1
            i = i + 1
        print(walls)
        g = SquareGrid(width, height)
        g.walls = walls
        return g

class SquareGrid:

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.walls = []

    def in_bounds(self, id):
        (x, y) = id
        return 0 <= x < self.width and 0 <= y < self.height

    def passable(self, id):
        return id not in self.walls

    def neighbors(self, id):
        (x, y) = id
        results = [(x+1, y), (x, y-1), (x-1,y), (x, y+1)]
        if (x + y) % 2 == 0:
            results.reverse()
        results = filter(self.in_bounds, results)
        results = filter(self.passable, results)
        return results

    def draw_grid(self, path=None, cost_so_far=None, draw_init=False):
        for i in range(self.height):
            for j in range(self.width):
                if path and (j, i) in path:
                    print('X ', end='')
                elif cost_so_far and (j, i) in cost_so_far:
                    print(cost_so_far[(j, i)], end=' ')
                elif (j, i) in self.walls:
                    print('##', end='')
                else:
                    print('. ', end='')
            print()


class GridWithWeights(SquareGrid):

    def __init__(self, width, height):
        super().__init__(width, height)
        self.weights = dict()

    def cost(self, from_node, to_node):
        return self.weights.get(to_node, 1)

    def set_random_weights(self):
        for i in range(self.height):
            for j in range(self.width):
                if (j, i) not in self.walls:
                    self.weights[(j, i)] = r.randint(0, 9)

    def draw_weights(self):
        for i in range(self.height):
            for j in range(self.width):
                if (j, i) in self.weights:
                    print(self.weights[(j, i)], end=' ')
                else:
                    print('##', end='')
            print()


class Queue:

    def __init__(self):
        self.elements = collections.deque()

    def empty(self):
        return len(self.elements) == 0

    def put(self, x):
        self.elements.append(x)

    def get(self):
        return self.elements.popleft()


class PriorityQueue:

    def __init__(self):
        self.elements = list()

    def empty(self):
        return len(self.elements) == 0

    def put(self, item, priority):
        heapq.heappush(self.elements, (priority, item))

    def get(self):
        return heapq.heappop(self.elements)[1]