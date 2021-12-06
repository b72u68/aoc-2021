import os
import sys


# get data from file
def get_data(filename):
    file_dir = os.path.join(os.getcwd(), filename)
    f = open(file_dir)
    data = [int(num) for num in f.readline().split(",")]
    return data


# solution for part 1
def part1(data):
    fishes = [0] * 9
    for fish in data:
        fishes[fish] += 1
    for _ in range(80):
        temp_fishes = [0] * 9
        for i in range(9):
            if i == 0:
                temp_fishes[6] = fishes[0]
                temp_fishes[8] += fishes[0]
            else:
                temp_fishes[i-1] += fishes[i]
        fishes = temp_fishes
    return sum(fishes)


# solution for part 2
def part2(data):
    fishes = [0] * 9
    for fish in data:
        fishes[fish] += 1
    for _ in range(256):
        temp_fishes = [0] * 9
        for i in range(9):
            if i == 0:
                temp_fishes[6] = fishes[0]
                temp_fishes[8] += fishes[0]
            else:
                temp_fishes[i-1] += fishes[i]
        fishes = temp_fishes
    return sum(fishes)


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
