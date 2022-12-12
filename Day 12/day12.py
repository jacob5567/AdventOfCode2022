import collections


def main():
    with open("input", "r") as input_file:
        input_list = input_file.readlines()
    heightmap, start, end = read_heightmap(input_list)
    print(find_shortest_path(heightmap, start, end))


def read_heightmap(input_list):
    heightmap = []
    char_map = {x: ord(x)-96 for x in "abcdefghijklmnopqrstuvwxyz"}
    char_map["S"] = 1
    char_map["E"] = 26
    start = (0, 0)
    end = (0, 0)
    for i in range(len(input_list)):
        if "S" in input_list[i]:
            start = i, input_list[i].index("S")
        if "E" in input_list[i]:
            end = i, input_list[i].index("E")
        heightmap.append([char_map[x] for x in input_list[i].strip()])
    return heightmap, start, end


def find_shortest_path(heightmap, start, end):
    queue = collections.deque()
    queue.append(start)
    visited = [[False for i in range(len(heightmap[0]))]
               for j in range(len(heightmap))]
    visited[start[0]][start[1]] = 1
    while queue:
        current = queue.popleft()
        if current == end:
            return visited[current[0]][current[1]] - 1
        for n in get_neighbors(current, heightmap, visited):
            if n not in visited:
                visited[n[0]][n[1]] = visited[current[0]][current[1]] + 1
                queue.append(n)


def get_neighbors(current, heightmap, visited):
    neighbors = []
    for direction in ((0, 1), (0, -1), (1, 0), (-1, 0)):
        next = current[0] + direction[0], current[1] + direction[1]
        if 0 <= next[0] < len(heightmap) and 0 <= next[1] < len(heightmap[0]) and not visited[next[0]][next[1]]:
            if heightmap[next[0]][next[1]] - heightmap[current[0]][current[1]] <= 1:
                neighbors.append(next)
    return neighbors


if __name__ == "__main__":
    main()
