def main():
    with open("input", "r") as input_file:
        input_list = input_file.readlines()
    print(calculate_score(input_list))
    print(calculate_score_2(input_list))

def calculate_score(input_list):
    score_map = {
        "X": 1,
        "Y": 2,
        "Z": 3
    }
    index_map = {
        "A": 0,
        "B": 1,
        "C": 2,
        "X": 0,
        "Y": 1,
        "Z": 2
    }
    matches = []
    for line in input_list:
        matches.append((line[0],line[2]))
    score = 0
    for match in matches:
        score += score_map[match[1]]
        if index_map[match[0]] == index_map[match[1]]:
            score += 3
        elif (index_map[match[1]] + 2) % 3 == index_map[match[0]]:
            score += 6
    return score

def calculate_score_2(input_list):
    index_map = {
        "A": 0,
        "B": 1,
        "C": 2
    }
    matches = []
    for line in input_list:
        matches.append((line[0], line[2]))
    score = 0
    for match in matches:
        if match[1] == "X":
            score += ((index_map[match[0]] + 2) % 3) + 1
        elif match[1] == "Y":
            score += 3
            score += index_map[match[0]] + 1
        elif match[1] == "Z":
            score += 6
            score += ((index_map[match[0]] + 1) % 3) + 1
    return score

if __name__ == "__main__":
    main()
