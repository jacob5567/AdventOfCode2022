def main():
    input_file = open("input", "r")
    input_list = input_file.readlines()
    input_file.close()
    print(find_max_calories(input_list))

def find_max_calories(input_list):
    current_max = 0
    current_sum = 0
    for line in input_list:
        if line == "\n":
            current_sum = 0
        else:
            current_sum += int(line)
            if current_sum > current_max:
                current_max = current_sum
    return current_max

if __name__ == "__main__":
    main()