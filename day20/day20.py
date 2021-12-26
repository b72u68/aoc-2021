import os
import sys


# get data from file
def get_data(filename):
    file_dir = os.path.join(os.getcwd(), filename)
    f = open(file_dir)
    lines = f.readlines()

    algo = [x for x in lines[0].rstrip()]
    image = []
    for line in lines[2:]:
        image.append([x for x in line.rstrip()])
    return algo, image


def enhance(image, algo, times):
    dirs = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 0], [0, 1], [1, -1],
            [1, 0], [1, 1]]
    inf_spc = "0"

    for _ in range(times):
        rows = len(image)
        cols = len(image[0])

        enh_image = [['.' for _ in range(cols + 2)] for _ in range(rows + 2)]
        for row in range(-1, rows + 1):
            for col in range(-1, cols + 1):
                pixel = ""
                for rc, cc in dirs:
                    p_row = row + rc
                    p_col = col + cc
                    if 0 <= p_row < rows and 0 <= p_col < cols:
                        pixel += "1" if image[p_row][p_col] == "#" else "0"
                    else:
                        pixel += inf_spc
                enh_image[row + 1][col + 1] = algo[int(pixel, 2)]
        inf_spc = "1" if algo[int((inf_spc * 9), 2)] == "#" else "0"
        image = enh_image

    return image


def count_lights(image):
    return sum([line.count("#") for line in image])


def print_image(image):
    color = "\033[93m"
    endc = "\033[0m"
    for i in range(len(image)):
        row = ""
        for j in range(len(image[i])):
            if image[i][j] == ".":
                row += "."
            else:
                row += color + "#" + endc
        print(row)


# solution for part 1
def part1(data):
    algo, image = data
    image = enhance(image, algo, 2)
    return count_lights(image)


# solution for part 2
def part2(data):
    algo, image = data
    image = enhance(image, algo, 50)
    return count_lights(image)


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
