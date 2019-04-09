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


if __name__ == "__main__":
    board = read_board('board.txt')