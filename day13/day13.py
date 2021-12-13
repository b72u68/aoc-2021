import os
import sys


# get data from file
def get_data(filename):
    file_dir = os.path.join(os.getcwd(), filename)
    f = open(file_dir)
    lines = f.readlines()

    size = [0, 0]
    coords = []
    folds = []

    for i in range(len(lines)):
        line = lines[i].strip("\n")
        if not line:
            break
        x, y = line.split(",")
        if int(x)+1 > size[0]:
            size[0] = int(x) + 1
        if int(y)+1 > size[1]:
            size[1] = int(y) + 1
        coords.append([int(x), int(y)])

    for i in range(i+1, len(lines)):
        dir, coord = lines[i][11:].split("=")
        folds.append([dir, int(coord)])

    return [size, coords, folds]


def print_board(board):
    color = "\033[93m"
    endc = "\033[0m"
    for i in range(len(board)):
        row = ""
        for j in range(len(board[i])):
            if not board[i][j]:
                row += "."
            else:
                row += color + "#" + endc
        print(row)


# solution for part 1
def part1(data):
    size, coords, folds = data
    board = [[False] * size[0] for _ in range(size[1])]

    for x, y in coords:
        board[y][x] = True

    for dir, coord in folds:
        if dir == "y":
            new_board = [[False] * len(board[0]) for _ in range(coord)]

            for i in range(len(new_board)):
                for j in range(len(new_board[i])):
                    new_board[i][j] = board[i][j] or board[len(board)-i-1][j]

            board = new_board

        else:
            new_board = [[False] * coord for _ in range(len(board))]

            for i in range(len(new_board)):
                for j in range(len(new_board[i])):
                    new_board[i][j] = board[i][j] or board[i][len(board[i])-j-1]

            board = new_board

        break

    result = 0
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j]:
                result += 1

    return result


# solution for part 2
def part2(data):
    size, coords, folds = data
    board = [[False] * size[0] for _ in range(size[1])]

    for x, y in coords:
        board[y][x] = True

    for dir, coord in folds:
        if dir == "y":
            new_board = [[False] * len(board[0]) for _ in range(coord)]

            for i in range(len(new_board)):
                for j in range(len(new_board[i])):
                    new_board[i][j] = board[i][j] or board[len(board)-i-1][j]

            board = new_board

        else:
            new_board = [[False] * coord for _ in range(len(board))]

            for i in range(len(new_board)):
                for j in range(len(new_board[i])):
                    new_board[i][j] = board[i][j] or board[i][len(board[i])-j-1]

            board = new_board

    print_board(board)

    return


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
