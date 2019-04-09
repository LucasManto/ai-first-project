import numpy as np

def read_board(filepath='board.txt'):
    with open(filepath, 'r') as board_file:
        dimensions_string = board_file.readline()
        dimensions_string = dimensions_string.split(' ')
        n_rows = int(dimensions_string[0])
        n_cols = int(dimensions_string[1])

        board = []
        for _ in range(n_rows):
            row_string = board_file.readline()
            row = []
            for j in range(n_cols):
                row.append(row_string[j])
            board.append(row)

    return np.array(board)


def find_path(start_index, target_index, board, algorithm='dfs'):
    assert algorithm in ['dfs', 'bfs', 'bstf', 'a*'], "The algorithm parameter should be dfs, bfs, bstf or a*"

    if algorithm is 'dfs':
        pass
    elif algorithm is 'bfs':
        pass
    elif algorithm is 'bstf':
        pass
    else:
        pass

    path = []
    return path


if __name__ == "__main__":
    board = read_board('board.txt')
    start_index = np.argwhere(board == '#')
    target_index = np.argwhere(board == '$')
    path = find_path(start_index, target_index, board)
    print(path)