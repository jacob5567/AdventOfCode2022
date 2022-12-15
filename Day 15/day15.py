import re
import math


def main():
    with open("input", "r") as input_file:
        input_list = input_file.readlines()
    sensor_map, y_map = generate_max_distances(input_list)
    print(calculate_invalid_positions(sensor_map, y_map, 2000000))


def generate_max_distances(input_list):
    min_x = 0
    max_x = 0
    min_y = 0
    max_y = 0
    for line in input_list:
        for x in re.findall("x=(-?\d+)", line):
            if int(x) < min_x:
                min_x = int(x)
            if int(x) > max_x:
                max_x = int(x)
        for y in re.findall("y=(-?\d+)", line):
            if int(y) < min_y:
                min_y = int(y)
            if int(y) > max_y:
                max_y = int(y)

    sensor_map = {}
    beacons = set()
    for line in input_list:
        x1, x2 = re.findall("x=(-?\d+)", line)
        y1, y2 = re.findall("y=(-?\d+)", line)
        sensor_map[(int(x1), int(y1))] = manhattan_distance(
            int(x1), int(y1), int(x2), int(y2))
        beacons.add((int(x2), int(y2)))

    y_map = {}
    for x, y in beacons:
        if y not in y_map:
            y_map[y] = 1
        else:
            y_map[y] += 1

    return sensor_map, y_map


def calculate_invalid_positions(sensor_map, y_map, y):
    min_x, max_x = find_min_max(sensor_map)
    invalid_positions = 0
    for x in range(min_x, max_x + 1):
        for sensor in sensor_map.keys():
            if manhattan_distance(x, y, sensor[0], sensor[1]) <= sensor_map[sensor]:
                invalid_positions += 1
                break
    if y not in y_map:
        return invalid_positions
    else:
        return invalid_positions - y_map[y]


def find_min_max(sensor_map):
    min_x, max_x = math.inf, -math.inf
    for x, y in sensor_map:
        if x - sensor_map[x, y] < min_x:
            min_x = x - sensor_map[x, y]
        if x + sensor_map[x, y] > max_x:
            max_x = x + sensor_map[x, y]
    return min_x, max_x


def manhattan_distance(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)


if __name__ == "__main__":
    main()
