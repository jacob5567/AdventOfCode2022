def main():
    with open("input", "r") as input_file:
        input_list = input_file.readlines()
    print(sum_priorities(input_list))
    print(sum_group(input_list))


def sum_priorities(input_list):
    priority_map = get_priority_map()
    sum = 0
    for line in input_list:
        first_half = line[:len(line) // 2]
        second_half = line[len(line) // 2:]
        repeats = set(first_half).intersection(set(second_half))
        for n in repeats:
            sum += priority_map[n]
    return sum

def sum_group(input_list):
    stripped_list = [line.strip() for line in input_list]
    priority_map = get_priority_map()
    sum = 0
    i = 0
    while i < len(stripped_list) - 2:
        bag_1 = stripped_list[i]
        bag_2 = stripped_list[i + 1]
        bag_3 = stripped_list[i + 2]
        repeats = set(bag_1).intersection(set(bag_2)).intersection(set(bag_3))
        for n in repeats:
            sum += priority_map[n]
        i += 3
    return sum

def get_priority_map():
    priority_map = {}
    i = 1
    for letter in (chr(n) for n in range(ord("a"), ord("z") + 1)):
        priority_map[letter] = i
        i += 1
    for letter in (chr(n) for n in range(ord("A"), ord("Z") + 1)):
        priority_map[letter] = i
        i += 1
    return priority_map


if __name__ == "__main__":
    main()
