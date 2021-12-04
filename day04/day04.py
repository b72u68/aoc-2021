import os
import sys
import re
import copy


# get data from file
def get_data(filename):
    file_dir = os.path.join(os.getcwd(), filename)
    f = open(file_dir)

    raw = f.readlines()
    plays = [int(num) for num in raw[0].strip("\n").split(",")]
    boards = []

    raw.append("")
    board = []
    for i in range(2, len(raw)):
        line = re.sub(r'\s+', ' ', raw[i].strip("\n")).strip()
        if not line:
            if board:
                boards.append(board)
            board = []
            continue
        board.append([int(num) for num in line.split(" ")])

    return (plays, boards)


def check_col(A, col):
    rows = len(A)
    return sum([A[i][col] for i in range(rows)]) == -5


def check_row(A, row):
    cols = len(A[0])
    return sum([A[row][j] for j in range(cols)]) == -5


# solution for part 1
def part1(data):
    plays, boards = copy.deepcopy(data)
    board_sums = []

    for board in boards:
        board_sums.append((sum([sum(board[i]) for i in range(len(board))])))

    for play in plays:
        for board_idx in range(len(boards)):
            board = boards[board_idx]
            found = False
            for i in range(5):
                for j in range(5):
                    if boards[board_idx][i][j] == play:
                        board[i][j] = -1
                        board_sums[board_idx] -= play
                        if check_col(board, j) or check_row(board, i):
                            return board_sums[board_idx] * play
                        found = True
                        break
                if found:
                    break


# solution for part 2
def part2(data):
    plays, boards = copy.deepcopy(data)
    board_sums = []
    done_idx = set()

    for board in boards:
        board_sums.append((sum([sum(board[i]) for i in range(len(board))])))

    for play in plays:
        for board_idx in range(len(boards)):
            if board_idx not in done_idx:
                board = boards[board_idx]
                found = False
                for i in range(5):
                    for j in range(5):
                        if boards[board_idx][i][j] == play:
                            board[i][j] = -1
                            board_sums[board_idx] -= play
                            if check_col(board, j) or check_row(board, i):
                                done_idx.add(board_idx)
                                if len(done_idx) == len(boards):
                                    return board_sums[board_idx] * play
                            found = True
                            break
                    if found:
                        break


if __name__ == "__main__":

    filename = "data.txt"

    if len(sys.argv) >= 2:
        filename = sys.argv[1]

    try:
        data = get_data(filename)
        print(part1(data))
        print(part2(data))

    except Exception as e:
        print(e)
