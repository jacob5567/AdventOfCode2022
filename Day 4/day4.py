def main():
    with open("input", "r") as input_file:
        input_list = input_file.readlines()
    print(count_fully_contained_ranges(input_list))


def count_fully_contained_ranges(input_list):
    count = 0
    for pair in parse_ranges(input_list):
        if is_fully_contained(pair):
            count += 1
    return count


def is_fully_contained(pair):
    range_1, range_2 = pair
    if (range_1[0] <= range_2[0] and range_1[1] >= range_2[1]) or (range_2[0] <= range_1[0] and range_2[1] >= range_1[1]):
        return True
    return False


def parse_ranges(input_list):
    ranges = []
    for line in input_list:
        line = line.strip()
        if line != "":
            range_1, range_2 = line.split(",")
            range_1 = tuple(int(i) for i in range_1.split("-"))
            range_2 = tuple(int(i) for i in range_2.split("-"))
        ranges.append((range_1, range_2))
    return ranges


if __name__ == "__main__":
    main()
