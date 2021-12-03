import os
import sys
import copy


# get data from file
def get_data(filename):
    file_dir = os.path.join(os.getcwd(), filename)
    f = open(file_dir)

    data = [line.strip("\n") for line in f.readlines()]

    return data


def binary_to_decimal(bit_string):
    n = len(bit_string)
    result = 0
    for i in range(n-1, -1, -1):
        result += 2**(n-1-i) * int(bit_string[i])
    return result


# solution for part 1
def part1(data):
    gamma = ""
    epsilon = ""
    for i in range(len(data[0])):
        count_1 = 0
        for j in range(len(data)):
            if data[j][i] == "1":
                count_1 += 1
            else:
                count_1 -= 1
        if count_1 > 1:
            gamma += "1"
            epsilon += "0"
        else:
            gamma += "0"
            epsilon += "1"
    gamma = binary_to_decimal(gamma)
    epsilon = binary_to_decimal(epsilon)
    return gamma * epsilon


# solution for part 2
def part2(data):

    d = {"oxygen": copy.deepcopy(data), "co2": copy.deepcopy(data)}

    for i in range(len(data[0])):

        for k, v in d.items():

            if len(d[k]) == 1:
                break
            index_0s = []
            index_1s = []

            for j in range(len(v)):
                if v[j][i] == "1":
                    index_1s.append(v[j])
                else:
                    index_0s.append(v[j])

            if len(index_0s) <= len(index_1s):
                if k == "oxygen":
                    d[k] = index_1s
                else:
                    d[k] = index_0s
            else:
                if k == "oxygen":
                    d[k] = index_0s
                else:
                    d[k] = index_1s

    oxygen = binary_to_decimal(d["oxygen"][0])
    co2 = binary_to_decimal(d["co2"][0])

    return oxygen * co2


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
