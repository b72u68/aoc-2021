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
    n = len(data)
    crabs = sorted(data)
    median = crabs[n//2] if n % 2 == 1 else (crabs[n//2-1] + crabs[n//2]) // 2
    return sum([abs(crab - median) for crab in crabs])


# solution for part 2
def part2(data):
    mean = sum(data)/len(data)
    if mean - int(mean) < 0.6:
        mean = int(mean)
    else:
        mean = int(mean) + 1
    result = 0
    for crab in data:
        n = abs(crab - mean)
        result += n*(n+1)//2
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
