import os
import sys
import math


# get data from file
def get_data(filename):
    file_dir = os.path.join(os.getcwd(), filename)
    f = open(file_dir)
    data = [int(num) for num in f.readline().split(",")]
    return data


# solution for part 1
def part1(data):
    n = len(data)
    crabs = sorted(data)
    median = crabs[n//2] if n % 2 == 1 else (crabs[n//2-1] + crabs[n//2]) // 2
    return sum([abs(crab - median) for crab in crabs])


# solution for part 2
def part2(data):
    mean_ceil = math.ceil(sum(data)/len(data))
    mean_floor = sum(data)//len(data)
    result_ceil = 0
    result_floor = 0
    for crab in data:
        n_ceil = abs(crab - mean_ceil)
        n_floor = abs(crab - mean_floor)
        result_ceil += n_ceil*(n_ceil + 1) // 2
        result_floor += n_floor*(n_floor + 1) // 2
    return min(result_ceil, result_floor)


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
