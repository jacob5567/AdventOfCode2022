def main():
    with open("input", "r") as input_file:
        input_list = input_file.readlines()
    cave = generate_cave(input_list)
    print(simulate_sand(cave))


def simulate_sand(cave):
    start_point = (0, 500)
    num_sand = 0
    sand = start_point
    while sand[0] < len(cave) - 1:
        sand = start_point
        while cave[sand[0]][sand[1]] != "o":
            if sand[0] == len(cave) - 1:
                break
            if cave[sand[0]+1][sand[1]] == ".":  # go down
                sand = (sand[0]+1, sand[1])
                cave[sand[0]][sand[1]] = "."
            elif cave[sand[0]+1][sand[1]-1] == ".":  # go left
                sand = (sand[0]+1, sand[1]-1)
                cave[sand[0]][sand[1]] = "."
            elif cave[sand[0]+1][sand[1]+1] == ".":  # go right
                sand = (sand[0]+1, sand[1]+1)
                cave[sand[0]][sand[1]] = "."
            else:
                cave[sand[0]][sand[1]] = "o"
                num_sand += 1
    return num_sand


def generate_cave(input_list):
    max_length = 0
    max_depth = 0
    for line in input_list:
        if line != "\n":
            line = line.split(" -> ")
            for pair in line:
                x, y = pair.split(",")
                if int(x) > max_length:
                    max_length = int(x)
                if int(y) > max_depth:
                    max_depth = int(y)
    cave = [["." for _ in range(max_length + 1)] for _ in range(max_depth + 1)]

    # add start point
    cave[0][500] = "+"

    # add rocks
    for line in input_list:
        if line != "\n":
            line = line.split(" -> ")
            prev_x, prev_y = -1, -1
            for pair in line:
                y, x = pair.split(",")
                x, y = int(x), int(y)
                cave[x][y] = "#"
                if prev_x != -1 and prev_y != -1:
                    if prev_x == x:
                        for i in range(min(prev_y, y), max(prev_y, y) + 1):
                            cave[x][i] = "#"
                    elif prev_y == y:
                        for i in range(min(prev_x, x), max(prev_x, x) + 1):
                            cave[i][y] = "#"
                prev_x, prev_y = x, y

    return cave


def print_cave(cave):
    for i in range(len(cave)):
        print(i, end="\t")
        for j in range(490, len(cave[0])):
            print(cave[i][j], end="")
        print()


if __name__ == "__main__":
    main()
