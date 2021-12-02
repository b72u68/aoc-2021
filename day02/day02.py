f = open("./data.txt")
data = [line.split(" ") for line in f.readlines()]


def part1():
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


def part2():
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


print(part1())
print(part2())
