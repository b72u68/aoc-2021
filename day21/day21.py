import os
import sys
import functools
import itertools


# get data from file
def get_data(filename):
    file_dir = os.path.join(os.getcwd(), filename)
    f = open(file_dir)
    lines = f.readlines()

    p1 = int(lines[0].strip("\n"))
    p2 = int(lines[1].strip("\n"))

    return p1, p2


def move(position, start_roll):
    for _ in range(3):
        start_roll += 1
        if start_roll > 100:
            start_roll -= 100
        position = (position + start_roll) % 10
        if position == 0:
            position = 10
    return position, start_roll


# solution for part 1
def part1(data):
    p1, p2 = data
    s1, s2 = 0, 0
    start_roll = 0
    turn = 0
    while s1 < 1000 and s2 < 1000:
        if turn % 2 == 0:
            p1, start_roll = move(p1, start_roll)
            s1 += p1
        else:
            p2, start_roll = move(p2, start_roll)
            s2 += p2
        turn += 1
    return turn * 3 * min(s1, s2)


# solution for part 2
def part2(data):
    rf = [(3,1), (4,3), (5,6), (6,7), (7,6), (8,3), (9,1)]

    def count(p1, s1, p2, s2):
        if s2 <= 0:
            return (0, 1)
        w1, w2 = 0, 0
        for (r, f) in rf:
            c2, c1 = count(p2, s2, (p1 + r) % 10, s1 - 1 - (p1 + r) % 10)
            w1, w2 = w1 + f * c1, w2 + f * c2

        return w1, w2

    p1, p2 = data
    return max(count(p1-1, 21, p2-1, 21))


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
