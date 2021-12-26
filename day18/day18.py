import os
import sys
from functools import reduce
from itertools import permutations


# get data from file
def get_data(filename):
    file_dir = os.path.join(os.getcwd(), filename)
    f = open(file_dir)

    data = []
    for raw_line in f.readlines():
        line = raw_line.strip("\n")
        data.append(process_line(line))

    return data


def process_line(s):
    line, depth = [], 0
    for c in s:
        if c == "[":
            depth += 1
        elif c == "]":
            depth -= 1
        elif c.isdigit():
            line.append([int(c), depth])
    return line


def explode(x):
    for i, ((num1, depth1), (num2, depth2)) in enumerate(zip(x, x[1:])):
        if depth1 < 5 or depth1 != depth2:
            continue
        if i > 0:
            x[i-1][0] += num1
        if i < len(x)-2:
            x[i+2][0] += num2
        return True, x[:i] + [[0, depth1-1]] + x[i+2:]
    return False, x


def split(x):
    for i, (num, depth) in enumerate(x):
        if num < 10:
            continue
        down = num // 2
        up = num - down
        return True, x[:i] + [[down, depth+1], [up, depth+1]] + x[i+1:]
    return False, x


def add(a, b):
    x = [[num, depth+1] for num, depth in a + b]
    while True:
        change, x = explode(x)
        if change:
            continue
        change, x = split(x)
        if not change:
            break
    return x


def magnitude(x):
    while len(x) > 1:
        for i, ((num1, depth1), (num2, depth2)) in enumerate(zip(x, x[1:])):
            if depth1 != depth2:
                continue
            val = num1 * 3 + num2 * 2
            x = x[:i] + [[val, depth1-1]] + x[i+2:]
            break
    return x[0][0]


# solution for part 1
def part1(data):
    return magnitude(reduce(add, data))


# solution for part 2
def part2(data):
    return max(magnitude(add(a, b)) for a, b in permutations(data, 2))


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
