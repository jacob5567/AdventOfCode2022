def main():
    with open("input", "r") as input_file:
        input_list = input_file.readlines()
    print(count_tail_positions(input_list))


def count_tail_positions(input_list):
    direction_map = {
        "U": (0, 1),
        "D": (0, -1),
        "L": (-1, 0),
        "R": (1, 0)
    }
    tail_positions = set()
    head = (0, 0)
    tail = (0, 0)
    tail_positions.add(tail)
    for line in input_list:
        direction, distance = line.strip().split(" ")
        distance = int(distance)
        for _ in range(distance):
            head = (head[0] + direction_map[direction][0],
                    head[1] + direction_map[direction][1])
            if not is_touching(tail, head):
                vector = get_vector(tail, head)
                tail = (tail[0] + vector[0], tail[1] + vector[1])
                tail_positions.add(tail)
    return len(tail_positions)


def is_touching(tail, head):
    if tail == head:
        return True
    if tail[0] == head[0]:
        return abs(tail[1] - head[1]) == 1
    if tail[1] == head[1]:
        return abs(tail[0] - head[0]) == 1
    if abs(tail[0] - head[0]) == 1 and abs(tail[1] - head[1]) == 1:
        return True
    return False


def get_vector(tail, head):
    if tail[0] == head[0]:
        return (0, 1 if head[1] > tail[1] else - 1)
    if tail[1] == head[1]:
        return (1 if head[0] > tail[0] else -1, 0)
    return (1 if head[0] > tail[0] else -1, 1 if head[1] > tail[1] else -1)


if __name__ == "__main__":
    main()
