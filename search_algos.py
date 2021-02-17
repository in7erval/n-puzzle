from implementation import *


def breadth_first_search_1(graph, start):
    frontier = Queue()
    frontier.put(start)
    visited = dict()
    visited[start] = True

    while not frontier.empty():
        current = frontier.get()
        print("Visiting %r" % current)
        for n in graph.neighbors(current):
            if n not in visited:
                frontier.put(n)
                visited[n] = True


def breadth_first_search_2(graph, start):
    frontier = Queue()
    frontier.put(start)
    came_from = dict()
    came_from[start] = None

    while not frontier.empty():
        current = frontier.get()
        for n in graph.neighbors(current):
            if n not in came_from:
                frontier.put(n)
                came_from[n] = current
    return came_from


def breadth_first_search_3(graph, start, goal):
    frontier = Queue()
    frontier.put(start)
    came_from = dict()
    came_from[start] = None

    while not frontier.empty():
        current = frontier.get()
        if current == goal:
            break
        for n in graph.neighbors(current):
            if n not in came_from:
                frontier.put(n)
                came_from[n] = current
    return came_from


def dijkstra_search(graph, start, goal):
    frontier = PriorityQueue()
    frontier.put(start, 0)
    came_from = dict()
    cost_so_far = dict()
    came_from[start] = None
    cost_so_far[start] = 0

    while not frontier.empty():
        current = frontier.get()
        if current == goal:
            break
        for n in graph.neighbors(current):
            new_cost = cost_so_far[current] + graph.cost(current, n)
            if n not in cost_so_far or new_cost < cost_so_far[n]:
                cost_so_far[n] = new_cost
                priority = new_cost
                frontier.put(n, priority)
                came_from[n] = current
    return came_from, cost_so_far


def heuristic(a, b):
    (x1, y1) = a
    (x2, y2) = b
    return abs(x1 - x2) + abs(y1 - y2)


def a_star_search(graph, start, goal):
    frontier = PriorityQueue()
    frontier.put(start, 0)
    came_from = dict()
    cost_so_far = dict()
    came_from[start] = None
    cost_so_far[start] = 0

    while not frontier.empty():
        current = frontier.get()
        if current == goal:
            break
        for n in graph.neighbors(current):
            new_cost = cost_so_far[current] + graph.cost(current, n)
            if n not in cost_so_far or new_cost < cost_so_far[n]:
                cost_so_far[n] = new_cost
                priority = new_cost + heuristic(goal, n)
                frontier.put(n, priority)
                came_from[n] = current
    return came_from, cost_so_far


def reconstruct_path(came_from, start, goal):
    current = goal
    path = [current]
    while current != start:
        current = came_from[current]
        path.append(current)
    path.append(start)
    path.reverse()
    return path


if __name__ == '__main__':
    example_graph = SimpleGraph()
    example_graph.edges = {
        'A': ['B'],
        'B': ['A', 'C', 'D'],
        'C': ['A'],
        'D': ['E', 'A'],
        'E': ['B']
    }

    # breadth_first_search_1(example_graph, 'A')

    # g = SquareGrid(30, 15)
    g = read_map('grid')
    walls = g.walls
    g = GridWithWeights(g.width, g.height)
    g.walls = walls
    g.set_random_weights()
    g.draw_weights()
    # g.draw_grid()
    start = (0, 0)
    end = (28, 0)
    # parents = breadth_first_search_3(g, start, end)
    came_from_d, cost_so_far_d = dijkstra_search(g, start, end)
    path_d = reconstruct_path(came_from_d, start, end)
    came_from_a, cost_so_far_a = a_star_search(g, start, end)
    path_a = reconstruct_path(came_from_a, start, end)
    # print(s)
    # print(path)
    g.draw_grid(path=path_a)
    print()
    g.draw_grid(path=path_d)
    # g.draw_grid(cost_so_far=cost_so_far)
