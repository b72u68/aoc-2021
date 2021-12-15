import os
import sys
import numpy as np
from queue import PriorityQueue


# get data from file
def get_data(filename):
    file_dir = os.path.join(os.getcwd(), filename)
    f = open(file_dir)

    data = []
    for line in f.readlines():
        data.append([int(num) for num in line.strip("\n")])

    return data


def dijkstra(grid, start, end):
    rows, cols = len(grid), len(grid[0])
    next_risks = PriorityQueue()
    next_risks.put((0, start))
    visited = {start}
    while next_risks:
        curr_risk, (i, j) = next_risks.get()
        neighbors = [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]
        if i == end[0] and j == end[1]:
            return curr_risk
        for row, col in neighbors:
            if 0 <= row < rows and 0 <= col < cols and (row, col) not in visited:
                risk = grid[row][col]
                next_risks.put((curr_risk + risk, (row, col)))
                visited.add((row, col))
    return


# solution for part 1
def part1(data):
    return dijkstra(data, (0, 0), (len(data)-1, len(data[0])-1))


# solution for part 2
def part2(filename):
    data = np.genfromtxt(filename, delimiter=1, dtype=np.uint16)
    data = np.block([[(data + i + j - 1) % 9 + 1 for i in range(5)] for j in range(5)])
    return dijkstra(data, (0, 0), (len(data)-1, len(data[0])-1))


if __name__ == "__main__":

    filename = "data.txt"

    if len(sys.argv) >= 2:
        filename = sys.argv[1]

    try:
        data = get_data(filename)
        print(part1(data))
        print(part2(filename))

    except Exception as e:
        print(e)
