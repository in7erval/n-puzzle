import sys

from implementation import Queue


def print_puzzle(puzzle: tuple):
    for i in range(len(puzzle)):
        for j in range(len(puzzle[i])):
            print(puzzle[i][j], end=' ')
        print()


def find_space(puzz: tuple):
    rows = len(puzz)
    for i in range(rows):
        for j in range(rows):
            if puzz[i][j] == 0:
                return i, j


def copy_tuple(tup: tuple):
    if isinstance(tup, tuple):
        return tuple(copy_tuple(x) for x in tup)
    return tup


def tuple2list(tup: tuple) -> list:
    l = list()
    for x in tup:
        l.append(list(x))
    return l


def list2tuple(l: list) -> tuple:
    l1 = list()
    for x in l:
        l1.append(tuple(x))
    return tuple(l1)


def print_queue(q: Queue):
    l = list(q.elements)
    if None in l:
        l.remove(None)
    print("___________")
    num_elems = len(l)
    rows = len(l[0])
    for row in range(rows):
        for i in range(num_elems):
            for j in range(len(l[i])):
                print(l[i][row][j], end=' ')
            print('\t',end='')
        print()


def find_coordinates(puzz, value: int) -> tuple:
    for y in range(len(puzz)):
        for x in range(len(puzz[y])):
            if puzz[y][x] == value:
                return x, y


def read_from_stdin() -> tuple:
    rows = list()
    for x in sys.stdin:
        row = list()
        for num_str in x.strip().split(' '):
            if num_str != '':
                row.append(int(num_str))
        rows.append(row)
    return list2tuple(rows)


def get_neighbours(puzz: tuple):
    directions = list()
    buf = up(puzz)
    if buf:
        directions.append(buf)
    buf = down(puzz)
    if buf:
        directions.append(buf)
    buf = left(puzz)
    if buf:
        directions.append(buf)
    buf = right(puzz)
    if buf:
        directions.append(buf)
    return directions


def up(puzz: tuple):
    space_pos = find_space(puzz)
    if space_pos[0] > 0:
        copy = tuple2list(puzz)
        elem = copy[space_pos[0] - 1][space_pos[1]]
        copy[space_pos[0] - 1][space_pos[1]] = copy[space_pos[0]][space_pos[1]]
        copy[space_pos[0]][space_pos[1]] = elem
        return list2tuple(copy)


def down(puzz: tuple):
    space_pos = find_space(puzz)
    if space_pos[0] < len(puzz) - 1:
        copy = tuple2list(puzz)
        elem = copy[space_pos[0] + 1][space_pos[1]]
        copy[space_pos[0] + 1][space_pos[1]] = copy[space_pos[0]][space_pos[1]]
        copy[space_pos[0]][space_pos[1]] = elem
        return list2tuple(copy)


def left(puzz: tuple):
    space_pos = find_space(puzz)
    if space_pos[1] > 0:
        copy = tuple2list(puzz)
        elem = copy[space_pos[0]][space_pos[1] - 1]
        copy[space_pos[0]][space_pos[1] - 1] = copy[space_pos[0]][space_pos[1]]
        copy[space_pos[0]][space_pos[1]] = elem
        return list2tuple(copy)


def right(puzz: tuple):
    space_pos = find_space(puzz)
    if space_pos[1] < len(puzz) - 1:
        copy = tuple2list(puzz)
        elem = copy[space_pos[0]][space_pos[1] + 1]
        copy[space_pos[0]][space_pos[1] + 1] = copy[space_pos[0]][space_pos[1]]
        copy[space_pos[0]][space_pos[1]] = elem
        return list2tuple(copy)


def get_blank_matrix(size: int):
    matrix = list()
    for i in range(size):
        matrix_row = list()
        for j in range(size):
            matrix_row.append(0)
        matrix.append(matrix_row)
    return matrix


def get_goal_puzzle(size: int):
    matrix = get_blank_matrix(size)
    c = 1
    for a in range(size):
        for j in range(a, size - a):
            matrix[a][j] = c
            c += 1
        for i in range(a + 1, size - a):
            matrix[i][size - a - 1] = c
            c += 1
        for j in range(size - a - 2, a - 1, -1):
            matrix[size - a - 1][j] = c
            c += 1
        for i in range(size - a - 2, a, -1):
            matrix[i][a] = c
            c += 1

    (x, y) = find_coordinates(matrix, size*size)
    matrix[y][x] = 0
    return list2tuple(matrix)


def linear_puzzle_path(path: list):
    l = list()
    for p in path:
        l1 = list()
        for x in p:
            for y in x:
                l1.append(y)
        l.append(tuple(l1))
    return l
