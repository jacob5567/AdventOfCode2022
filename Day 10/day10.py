def main():
    with open("input", "r") as input_file:
        input_list = input_file.readlines()
    print(calculate_signal_strength(input_list))


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


def increment_and_check(cycle_number, current_x, strength_sum):
    cycle_number += 1
    if cycle_number in watched_cycles:
        strength_sum += (current_x * cycle_number)
    return cycle_number, current_x, strength_sum


if __name__ == "__main__":
    main()
