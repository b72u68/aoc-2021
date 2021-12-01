f = open("./data.txt")
data = [int(x) for x in f.readlines()]


def part1():
    result = 0
    for i in range(1, len(data)):
        if data[i] > data[i-1]:
            result += 1
    return result


def part2():
    result = 0
    window = 3
    for i in range(1, len(data)-window+1):
        if data[i+window-1] > data[i-1]:
            result += 1
    return result


print(part1())
print(part2())
