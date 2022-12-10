def main():
    with open("input", "r") as input_file:
        input_list = input_file.readlines()
    print(calculate_signal_strength(input_list))
    draw_screen(input_list)


watched_cycles = [x * 40 + 20 for x in range(6)]


def calculate_signal_strength(input_list):
    cycle_number = 0
    current_x = 1
    strength_sum = 0

    for line in input_list:
        if line.strip() == "noop":
            cycle_number, current_x, strength_sum = increment_and_check(
                cycle_number, current_x, strength_sum)
        elif line.split(" ")[0] == "addx":
            cycle_number, current_x, strength_sum = increment_and_check(
                cycle_number, current_x, strength_sum)
            cycle_number, current_x, strength_sum = increment_and_check(
                cycle_number, current_x, strength_sum)
            current_x += int(line.split(" ")[1])
    return strength_sum


def draw_screen(input_list):
    cycle_number = 0
    current_x = 1
    cycle_map = {}

    for line in input_list:
        if line.strip() == "noop":
            cycle_number, current_x, cycle_map = increment_and_store(
                cycle_number, current_x, cycle_map)
        elif line.split(" ")[0] == "addx":
            cycle_number, current_x, cycle_map = increment_and_store(
                cycle_number, current_x, cycle_map)
            cycle_number, current_x, cycle_map = increment_and_store(
                cycle_number, current_x, cycle_map)
            current_x += int(line.split(" ")[1])

    for i in range(1, 241):
        if i % 40 - 1 in range(cycle_map[i]-1, cycle_map[i]+2):
            print("#", end="")
        else:
            print(".", end="")
        if i % 40 == 0:
            print("")


def increment_and_check(cycle_number, current_x, strength_sum):
    cycle_number += 1
    if cycle_number in watched_cycles:
        strength_sum += (current_x * cycle_number)
    return cycle_number, current_x, strength_sum


def increment_and_store(cycle_number, current_x, cycle_map):
    cycle_number += 1
    cycle_map[cycle_number] = current_x
    return cycle_number, current_x, cycle_map


if __name__ == "__main__":
    main()
