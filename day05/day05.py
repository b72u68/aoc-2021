import os
import sys


# get data from file
def get_data(filename):
    file_dir = os.path.join(os.getcwd(), filename)
    f = open(file_dir)

    data = []

    for line in f.readlines():
        start, end = line.split(" -> ")
        x1 = int(start.split(",")[0])
        y1 = int(start.split(",")[1])
        x2 = int(end.split(",")[0])
        y2 = int(end.split(",")[1])
        data.append([[x1, y1], [x2, y2]])

    return data


# solution for part 1
def part1(data):
    points = {}
    result = 0

    for move in data:
        x1, y1 = move[0]
        x2, y2 = move[1]

        dx = 0 if x2 - x1 == 0 else 1 if x2 - x1 > 0 else -1
        dy = 0 if y2 - y1 == 0 else 1 if y2 - y1 > 0 else -1

        if dx == 0 or dy == 0:
            while x1 != x2 + dx or y1 != y2 + dy:
                points.setdefault((x1, y1), 0)
                points[(x1, y1)] += 1

                if points[(x1, y1)] == 2:
                    result += 1

                x1 += dx
                y1 += dy

    return result


# solution for part 2
def part2(data):
    points = {}
    result = 0

    for move in data:
        x1, y1 = move[0]
        x2, y2 = move[1]

        dx = 0 if x2 - x1 == 0 else 1 if x2 - x1 > 0 else -1
        dy = 0 if y2 - y1 == 0 else 1 if y2 - y1 > 0 else -1

        while x1 != x2 + dx or y1 != y2 + dy:
            points.setdefault((x1, y1), 0)
            points[(x1, y1)] += 1

            if points[(x1, y1)] == 2:
                result += 1

            x1 += dx
            y1 += dy

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
