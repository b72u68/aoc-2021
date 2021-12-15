import os
import sys
import copy


# get data from file
def get_data(filename):
    file_dir = os.path.join(os.getcwd(), filename)
    f = open(file_dir)
    lines = f.readlines()

    template = list(lines[0].strip("\n"))
    rules = {}
    for i in range(2, len(lines)):
        pair, insert = lines[i].strip("\n").split(" -> ")
        rules[pair] = insert

    return [template, rules]


# solution for part 1
def part1(data):
    template, rules = copy.deepcopy(data)
    for _ in range(10):
        i = 0
        while i < len(template)-1:
            pair = "".join(template[i:i+2])
            if pair in rules:
                insert = rules[pair]
                template.insert(i+1, insert)
                i += 2
            else:
                i += 1

    count = {}
    for c in template:
        count.setdefault(c, 0)
        count[c] += 1
    return max(count.values()) - min(count.values())


# solution for part 2
def part2(data):
    template, rules = copy.deepcopy(data)
    d = {}
    count = {}

    for i in range(len(template)-1):
        pair = "".join(template[i:i+2])
        d.setdefault(pair, 0)
        d[pair] += 1

    for i in range(len(template)):
        count.setdefault(template[i], 0)
        count[template[i]] += 1

    for _ in range(40):
        temp_d = copy.deepcopy(d)
        for pair in d:
            insert = rules[pair]
            first_pair = pair[0] + insert
            second_pair = insert + pair[1]

            temp_d[pair] -= d[pair]

            temp_d.setdefault(first_pair, 0)
            temp_d.setdefault(second_pair, 0)

            temp_d[first_pair] += 1 * d[pair]
            temp_d[second_pair] += 1 * d[pair]

            count.setdefault(insert, 0)
            count[insert] += 1 * d[pair]

            if temp_d[pair] == 0:
                del temp_d[pair]

        d = temp_d

    return max(count.values()) - min(count.values())


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
