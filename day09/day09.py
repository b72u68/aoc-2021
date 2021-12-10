import os
import sys


# get data from file
def get_data(filename):
    file_dir = os.path.join(os.getcwd(), filename)
    f = open(file_dir)

    data = []
    for line in f.readlines():
        data.append([int(x) for x in list(line.strip("\n"))])

    return data


# solution for part 1
def part1(data):
    result = 0
    for i in range(len(data)):
        for j in range(len(data[i])):
            is_low = True
            if i > 0 and data[i-1][j] <= data[i][j]:
                is_low = False
            if i < len(data)-1 and data[i+1][j] <= data[i][j]:
                is_low = False
            if j > 0 and data[i][j-1] <= data[i][j]:
                is_low = False
            if j < len(data[i])-1 and data[i][j+1] <= data[i][j]:
                is_low = False
            if is_low:
                result += data[i][j] + 1
    return result


def sink(data, i, j, visited=set()):
    result = 0
    if (i, j) not in visited:
        if i > 0 and data[i][j] < data[i-1][j] < 9:
            result += sink(data, i-1, j)
        if i < len(data)-1 and data[i][j] < data[i+1][j] < 9:
            result += sink(data, i+1, j)
        if j > 0 and data[i][j] < data[i][j-1] < 9:
            result += sink(data, i, j-1)
        if j < len(data[i])-1 and data[i][j] < data[i][j+1] < 9:
            result += sink(data, i, j+1)
        result += 1
        visited.add((i, j))
    return result


# solution for part 2
def part2(data):

    result = 1
    basins = []

    for i in range(len(data)):
        for j in range(len(data[i])):
            is_low = True
            if i > 0 and data[i-1][j] <= data[i][j]:
                is_low = False
            if i < len(data)-1 and data[i+1][j] <= data[i][j]:
                is_low = False
            if j > 0 and data[i][j-1] <= data[i][j]:
                is_low = False
            if j < len(data[i])-1 and data[i][j+1] <= data[i][j]:
                is_low = False
            if is_low:
                basins.append(sink(data, i, j))

    basins.sort()

    for i in range(3):
        result *= basins[-i-1]

    return result


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
