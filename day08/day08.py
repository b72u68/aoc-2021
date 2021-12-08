import os
import sys


# get data from file
def get_data(filename):
    file_dir = os.path.join(os.getcwd(), filename)
    f = open(file_dir)
    data = []
    for line in f.readlines():
        input_raw, output_raw = line.strip("\n").split(" | ")
        data.append([input_raw.split(" "), output_raw.split(" ")])
    return data


# solution for part 1
def part1(data):
    outputs = [data[i][1] for i in range(len(data))]
    result = 0
    for output in outputs:
        for letters in output:
            if len(letters) in [2, 3, 4, 7]:
                result += 1
    return result


def count_letters(A):
    d = {}
    for c in "".join(A):
        d.setdefault(c, 0)
        d[c] += 1
    return d


# solution for part 2
def part2(data):
    '''
    Position:
            0
        1       2
            3
        4       5
            6
    '''
    NUM_MAP = {(0, 1, 2, 4, 5, 6): 0, (2, 5): 1, (0, 2, 3, 4, 6): 2, (0, 2, 3, 5, 6): 3,
               (1, 2, 3, 5): 4, (0, 1, 3, 5, 6): 5, (0, 1, 3, 4, 5, 6): 6, (0, 2, 5): 7,
               (0, 1, 2, 3, 4, 5, 6): 8, (0, 1, 2, 3, 5, 6): 9}

    mappings = []
    for input, output in data:

        position = [None] * 7
        combine = ["".join(sorted(x)) for x in input + output]
        combine = sorted(set(combine), key=lambda x: len(x))
        d = count_letters(combine)

        one = combine[0]
        seven = combine[1]
        four = combine[2]
        eight = combine[-1]

        position[0] = set(seven).difference(set(one)).pop()

        if d[one[0]] > d[one[1]]:
            position[2] = one[1]
            position[5] = one[0]
        else:
            position[2] = one[0]
            position[5] = one[1]

        pos_1_3 = list(set(four).difference(set(one)))

        if d[pos_1_3[0]] > d[pos_1_3[1]]:
            position[1] = pos_1_3[1]
            position[3] = pos_1_3[0]
        else:
            position[1] = pos_1_3[0]
            position[3] = pos_1_3[1]

        pos_4_6 = list(set(eight).difference(set(seven + four)))

        if d[pos_4_6[0]] > d[pos_4_6[1]]:
            position[4] = pos_4_6[1]
            position[6] = pos_4_6[0]
        else:
            position[4] = pos_4_6[0]
            position[6] = pos_4_6[1]

        mappings.append(position)

    result = 0
    for i in range(len(data)):
        output = data[i][1]
        mapping = mappings[i]
        num_output = 0
        for o in output:
            idx_mapping = []
            for c in o:
                idx_mapping.append(mapping.index(c))
            num_output = num_output * 10 + NUM_MAP[tuple(sorted(idx_mapping))]
        result += num_output
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
