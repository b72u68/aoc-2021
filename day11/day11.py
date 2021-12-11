import os
import sys
import copy


# get data from file
def get_data(filename):
    file_dir = os.path.join(os.getcwd(), filename)
    f = open(file_dir)

    data = []
    for line in f.readlines():
        data.append([int(x) for x in line.strip("\n")])

    return data


def flash(data, i, j, visited=set()):
    moves = [[1, 0], [-1, 0], [1, 1], [1, -1], [-1, 1], [-1, -1], [0, 1], [0, -1]]
    result = 1 if data[i][j] == 9 else 0
    for di, dj in moves:
        next_i = i + di
        next_j = j + dj
        if 0 <= next_i < len(data) and 0 <= next_j < len(data[i]):
            if data[next_i][next_j] < 9:
                data[next_i][next_j] += 1
            elif (next_i, next_j) not in visited:
                visited.add((next_i, next_j))
                result += flash(data, next_i, next_j, visited)
    return result


def print_data(data):
    color = '\033[93m'
    endc = '\033[0m'
    for i in range(len(data)):
        row = ""
        for j in range(len(data[i])):
            if data[i][j] == 0:
                row += color + str(data[i][j]) + endc
            else:
                row += str(data[i][j])
        print(row)
    print()


# solution for part 1
def part1(data):
    data = copy.deepcopy(data)
    result = 0
    for _ in range(100):
        flashes = set()
        visited = set()
        for i in range(len(data)):
            for j in range(len(data)):
                if data[i][j] != 9:
                    data[i][j] += 1
                else:
                    flashes.add((i, j))

        while flashes:
            i, j = flashes.pop()
            if (i, j) not in visited:
                visited.add((i, j))
                result += flash(data, i, j, visited)
                for fi, fj in visited:
                    data[fi][fj] = 0

    return result


# solution for part 2
def part2(data):
    data = copy.deepcopy(data)
    step = 0
    while True:
        step += 1
        result = 0
        flashes = set()
        visited = set()
        for i in range(len(data)):
            for j in range(len(data)):
                if data[i][j] != 9:
                    data[i][j] += 1
                else:
                    flashes.add((i, j))

        while flashes:
            i, j = flashes.pop()
            if (i, j) not in visited:
                visited.add((i, j))
                result += flash(data, i, j, visited)
                for fi, fj in visited:
                    data[fi][fj] = 0

        if result == len(data) * len(data[i]):
            return step


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
