import os
import sys


def get_data(filename):
    file_dir = os.path.join(os.getcwd(), filename)
    f = open(file_dir)
    data = [int(x) for x in f.readlines()]
    return data


def part1(data):
    result = 0
    for i in range(1, len(data)):
        if data[i] > data[i-1]:
            result += 1
    return result


def part2(data):
    result = 0
    window = 3
    for i in range(1, len(data)-window+1):
        if data[i+window-1] > data[i-1]:
            result += 1
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
