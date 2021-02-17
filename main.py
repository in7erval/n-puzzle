from implementation import PriorityQueue
from search_algos import reconstruct_path
from utils import find_coordinates, print_puzzle, read_from_stdin, get_neighbours, get_blank_matrix, get_goal_puzzle, \
    linear_puzzle_path
from visualizer import visualizer


def heuristic(a: tuple, b: tuple):
    max_num = len(a)**2
    sum = 0
    for i in range(1, max_num):
        (x1, y1) = find_coordinates(a, i)
        (x2, y2) = find_coordinates(b, i)
        sum += abs(x1 - x2) + abs(y1 - y2)
    return sum


def a_star_search(start, goal):
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
        for n in get_neighbours(current):
            new_cost = cost_so_far[current] + 1
            if n not in cost_so_far or new_cost < cost_so_far[n]:
                cost_so_far[n] = new_cost
                priority = new_cost + heuristic(goal, n)
                frontier.put(n, priority)
                came_from[n] = current
    return came_from, cost_so_far


# puzzle = ((3, 7, 4),
#           (6, 2, 0),
#           (5, 8, 1))
puzzle = read_from_stdin()
goal_puzzle = get_goal_puzzle(len(puzzle))
came_from, cost_so_far = a_star_search(puzzle, goal_puzzle)
path = reconstruct_path(came_from, puzzle, goal_puzzle)
for p in path:
    print_puzzle(p)
    print('-----------')
print('----------------------------------------')
print_puzzle(puzzle)
print()
print_puzzle(goal_puzzle)
print('path_len: %d\ncame_from_size: %d\ncost_so_far_size: %d' % (len(path), len(came_from), len(cost_so_far)))
visualizer(linear_puzzle_path(path), len(puzzle))