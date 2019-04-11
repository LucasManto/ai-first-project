import numpy as np


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


def search_children(node, board, n_rows, n_cols):
    return []


def insert_dfs(children, nodes):
    pass


def insert_bfs(children, nodes):
    pass


def insert_bstf(children, nodes):
    pass


def insert_a(children, nodes):
    pass


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

    # TODO: Implementation of searching and adding possible paths to list
    nodes = [[start_index]]
    # while nodes[0] != target_index or nodes != []:
    #     children = search_children(nodes[0], board, n_rows, n_cols)
    #     insert(children, nodes)

    # path = nodes[0]
    # path.reverse()
    return path


if __name__ == "__main__":
    board, n_rows, n_cols = read_board('board.txt')
    start_index = np.argwhere(board == '#')[0].tolist()
    target_index = np.argwhere(board == '$')[0].tolist()
    assert start_index is not [], "Start point not found at board"
    assert target_index is not [], "Target point not found at board"
    path = find_path(start_index, target_index, board, n_rows, n_cols)
    print(path)