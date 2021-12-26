import os
import sys


# get data from file
def get_data(filename):
    file_dir = os.path.join(os.getcwd(), filename)
    f = open(file_dir)

    # process data here
    data = f.readlines()[0].strip("\n")[13:].split(", ")
    xrange = [int(x) for x in data[0][2:].split("..")]
    yrange = [int(y) for y in data[1][2:].split("..")]

    return [xrange, yrange]


def shoot(xrange, yrange, vx, vy):
    x, y = 0, 0
    highest_y = 0
    while True:
        if xrange[0] <= x <= xrange[1] and yrange[1] <= y <= yrange[0]:
            return True, highest_y
        if xrange[1] < x or yrange[1] > y:
            return False, None
        x += vx
        y += vy
        highest_y = max(highest_y, y)
        if vx < 0:
            vx += 1
        elif vx > 0:
            vx -= 1
        vy -= 1


# solution for part 1
def part1(data):
    _, yrange = data
    vy = -yrange[0] - 1
    y = 0
    while vy:
        y += vy
        vy -= 1
    return y


def is_hit(xrange, yrange, vx, vy):
    x, y = 0, 0
    while x <= max(xrange) and y >= min(yrange):
        if min(xrange) <= x <= max(xrange) and min(yrange) <= y <= max(yrange):
            return True
        x += vx
        y += vy
        if vx < 0:
            vx += 1
        if vx > 0:
            vx -= 1
        vy -= 1
    return False


# solution for part 2
def part2(data):
    xrange, yrange = data
    result = 0
    for vx in range(0, xrange[1]+1):
        for vy in range(yrange[0], -yrange[0]):
            if is_hit(xrange, yrange, vx, vy):
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
