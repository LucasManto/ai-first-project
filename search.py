import numpy as np
import math
import time


def read_board(filepath='board.txt'):
    with open(filepath, 'r') as board_file:
        dimensions_string = board_file.readline()
        dimensions_string = dimensions_string.split(' ')
        n_rows = int(dimensions_string[0])
        n_cols = int(dimensions_string[1])

        board = []
        board = board_file.readlines()
        for i in range(n_rows):
            row = list(board[i])[:n_cols]
            board[i] = row

    return np.array(board), n_rows, n_cols


def define_limits(index, max):
    inf_limit = index - 1
    sup_limit = index + 2
    if inf_limit < 0:
        inf_limit = 0
    if sup_limit > max:
        sup_limit = max

    return inf_limit, sup_limit


def element(element, nodes):
    for n in nodes:
        if element in n:
            return True
    return False


def search_children(nodes, board, n_rows, n_cols):
    row_index = nodes[0][0][0]
    col_index = nodes[0][0][1]

    # Defining limits to possible ways in rows and colums
    row_inf_limit, row_sup_limit = define_limits(row_index, n_rows)
    col_inf_limit, col_sup_limit = define_limits(col_index, n_cols)

    # Creating ranges
    row_range = range(row_inf_limit, row_sup_limit)
    col_range = range(col_inf_limit, col_sup_limit)

    # Adding children indexes to list only if the children is not '_' and indexes are different from actual index
    children = [[[i, j]] for i in row_range for j in col_range if (board[i][j] != '_' and (i != row_index or j != col_index) and not element([i, j], nodes))]
    for c in children:
        c.extend(nodes[0])

    return children


def insert_dfs(children, nodes, target_index):
    nodes.pop(0)
    children.extend(nodes)
    return children


def insert_bfs(children, nodes, target_index):
    nodes.pop(0)
    nodes.extend(children)
    return nodes


def insert_bstf(children, nodes, target_index):
    nodes.pop(0)
    nodes.extend(children)
    # Sort nodes by euclidean distance between candidate node and father node,
    # prioritizing diagonal child
    nodes = sorted(nodes, key=lambda x: math.sqrt((abs(x[0][0]-x[1][0]) + abs(x[0][1]-x[1][1]))), reverse=True)
    return nodes


def distance_to_initial(path):
    distance = 0
    prev_node = path[0]
    for curr_node in path[1:]:
        distance += math.sqrt((abs(curr_node[0]-prev_node[0]) + abs(curr_node[1]-prev_node[1])))
        prev_node = curr_node
    return distance


def insert_a(children, nodes, target_index):
    nodes.pop(0)
    nodes.extend(children)
    # Sort nodes by euclidean distance between candidate node and father node,
    # prioritizing diagonal child and shorter distance to target
    nodes = sorted(nodes, key=lambda x: distance_to_initial(x) + (abs(x[0][0]-target_index[0]) + abs(x[0][1]-target_index[1])))
    return nodes


def find_path(start_index, target_index, board, n_rows, n_cols, algorithm='dfs'):
    assert algorithm in ['dfs', 'bfs', 'bstf', 'a*'], "The algorithm parameter should be dfs, bfs, bstf or a*"

    if algorithm is 'dfs':
        insert = insert_dfs
    elif algorithm is 'bfs':
        insert = insert_bfs
    elif algorithm is 'bstf':
        insert = insert_bstf
    else:
        insert = insert_a

    nodes = [[start_index]]
    while nodes != [] and nodes[0][0] != target_index:
        children = search_children(nodes, board, n_rows, n_cols)
        nodes = insert(children, nodes, target_index)

    if nodes != []:
        path = nodes[0]
        path.reverse()
    else:
        path = []

    return path


if __name__ == "__main__":
    board, n_rows, n_cols = read_board('board.txt')
    start_index = np.argwhere(board == '#')[0].tolist()
    target_index = np.argwhere(board == '$')[0].tolist()
    assert start_index is not [], "Start point not found at board"
    assert target_index is not [], "Target point not found at board"

    print('DFS:')
    start = time.time()
    path = find_path(start_index, target_index, board, n_rows, n_cols, algorithm='dfs')
    end = time.time()
    print('\t- Path: ', path)
    print('\t- Time: ', round(end-start, 5))

    print('BFS:')
    start = time.time()
    path = find_path(start_index, target_index, board, n_rows, n_cols, algorithm='bfs')
    end = time.time()
    print('\t- Path: ', path)
    print('\t- Time: ', round(end-start, 5))

    print('BSTF:')
    start = time.time()
    path = find_path(start_index, target_index, board, n_rows, n_cols, algorithm='bstf')
    end = time.time()
    print('\t- Path: ', path)
    print('\t- Time: ', round(end-start, 5))

    print('A*:')
    start = time.time()
    path = find_path(start_index, target_index, board, n_rows, n_cols, algorithm='a*')
    end = time.time()
    print('\t- Path: ', path)
    print('\t- Time: ', round(end-start, 5))