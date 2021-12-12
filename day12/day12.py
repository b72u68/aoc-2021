import os
import sys


START = "start"
END = "end"


# get data from file
def get_data(filename):
    file_dir = os.path.join(os.getcwd(), filename)
    f = open(file_dir)

    data = {}
    for line in f.readlines():
        s, d = line.strip("\n").split("-")
        if s != END:
            data.setdefault(s, [])

            if d != START:
                data[s].append(d)

        if d != END:
            data.setdefault(d, [])

            if s != START:
                data[d].append(s)

    return data


def dfs(node, graph, path=[], visited=[]):
    if node not in graph:
        if node == END:
            return 1
        return 0
    if node.islower() and node in visited:
        return 0
    result = 0
    for cave in graph[node]:
        if node.islower():
            result += dfs(cave, graph, path + [node], visited + [node])
        else:
            result += dfs(cave, graph, path + [node], visited)
    return result


# solution for part 1
def part1(data):
    return dfs(START, data)


def dfs_svisited(node, graph, path=[], fvisited=[], svisited=[]):
    if node not in graph:
        if node == END:
            return 1
        return 0
    if node.islower() and node in svisited:
        return 0
    result = 0
    for cave in graph[node]:
        if node.islower():
            if node in fvisited:
                if svisited:
                    return 0
                else:
                    result += dfs_svisited(cave, graph, path + [node], fvisited, svisited + [node])
            else:
                result += dfs_svisited(cave, graph, path + [node], fvisited + [node], svisited)
        else:
            result += dfs_svisited(cave, graph, path + [node], fvisited, svisited)
    return result


# solution for part 2
def part2(data):
    return dfs_svisited(START, data)


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
