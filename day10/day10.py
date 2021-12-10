import os
import sys

MATCH_CLOSE = {"{": "}", "(": ")", "<": ">", "[": "]"}
MATCH_OPEN = {"}": "{", ")": "(", ">": "<", "]": "["}
CLOSES = MATCH_OPEN.keys()
OPENS = MATCH_CLOSE.keys()

# get data from file
def get_data(filename):
    file_dir = os.path.join(os.getcwd(), filename)
    f = open(file_dir)

    # process data here
    data = [line.strip("\n") for line in f.readlines()]

    return data


# solution for part 1
def part1(data):
    CLOSE_POINTS = {"}": 1197, ")": 3, ">": 25137, "]": 57}
    result = 0
    for line in data:
        stack = []
        for c in line:
            if c in OPENS:
                stack.append(c)
            elif c in CLOSES:
                if stack and MATCH_OPEN[c] == stack[-1]:
                    stack.pop()
                else:
                    result += CLOSE_POINTS[c]
                    break
    return result


# solution for part 2
def part2(data):
    CLOSE_POINTS = {"}": 3, ")": 1, ">": 4, "]": 2}
    scores = []
    for line in data:
        score = 0
        stack = []
        is_corrupted = False
        for c in line:
            if c in OPENS:
                stack.append(c)
            elif c in CLOSES:
                if stack and MATCH_OPEN[c] == stack[-1]:
                    stack.pop()
                else:
                    is_corrupted = True
                    break
        if is_corrupted:
            continue
        while stack:
            close = MATCH_CLOSE[stack.pop()]
            score = score * 5 + CLOSE_POINTS[close]
        scores.append(score)
    scores.sort()
    return scores[len(scores)//2]


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
