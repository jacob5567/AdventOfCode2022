def main():
    input_file = open("input", "r")
    input_list = input_file.readlines()
    input_file.close()
    print(find_max_calories(input_list))
    print(find_top3_sum(input_list))

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

def find_top3_sum(input_list):
    sums = list()
    current_sum = 0
    num_elves = 0
    for line in input_list:
        if line == "\n":
            num_elves += 1
            if sums == []:
                sums = [current_sum]
            else:
                i = 0
                while(i != len(sums) and current_sum > sums[i]):
                    i += 1
                sums[i:i] = [current_sum]
            current_sum = 0
        else:
            current_sum += int(line)
    return sum(sums[-3:])

if __name__ == "__main__":
    main()
