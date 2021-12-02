import os
import sys


def get_data(filename):
    file_dir = os.path.join(os.getcwd(), filename)
    f = open(file_dir)
    data = [line.split(" ") for line in f.readlines()]
    return data


def part1(data):
    x = 0
    y = 0
    for action, steps in data:
        steps = int(steps)
        if action == "forward":
            x += steps
        elif action == "up":
            y -= steps
        elif action == "down":
            y += steps
    return x * y


def part2(data):
    x = 0
    y = 0
    aim = 0
    for action, steps in data:
        steps = int(steps)
        if action == "down":
            aim += steps
        elif action == "up":
            aim -= steps
        elif action == "forward":
            x += steps
            y += aim * steps
    return x * y


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
