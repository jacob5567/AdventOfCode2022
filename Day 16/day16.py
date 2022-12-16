import re


class Valve:
    def __init__(self, name, rate=0, valves=[]):
        self.name = name
        self.rate = rate
        self.valves = valves

    def __str__(self):
        return f"Valve {self.name} has flow rate={self.rate}; tunnels lead to valves {self.valves}"

    def __repr__(self):
        return self.__str__()


def main():
    with open("input", "r") as input_file:
        input_list = input_file.readlines()
    # print(read_valves(input_list))
    valves = read_valves(input_list)
    move(valves, "AA", 30)


def read_valves(input_list):
    valves = {}
    for line in input_list:
        line = line.strip()
        if line == "":
            continue
        input_regex = re.compile(
            r"Valve ([A-Z]{2}) has flow rate=(\d+); tunnels? leads? to valves? (.*)")
        match = input_regex.match(line)
        if match:
            name, rate, valve_list = match.groups()
            valve_list = valve_list.split(", ")
            valves[name] = Valve(name, int(rate), valve_list)
    return valves


# distance between two nodes is 1
def dijkstra_find_distance_to_all_nodes(graph, node):
    distances = {node: 0}
    visited = set()
    while len(visited) < len(graph):
        min_distance = float("inf")
        min_node = None
        for node in distances:
            if node not in visited:
                if distances[node] < min_distance:
                    min_distance = distances[node]
                    min_node = node
        visited.add(min_node)
        for neighbor in graph[min_node].valves:
            if neighbor not in visited:
                if neighbor not in distances:
                    distances[neighbor] = distances[min_node] + 1
                else:
                    distances[neighbor] = min(
                        distances[neighbor], distances[min_node] + 1)
    return distances


def find_shortest_distance(graph, distances, time_remaining):
    flow_over_time = {}
    for node, distance in distances.items():
        flow_over_time[node] = graph[node].rate * \
            (time_remaining - (distance + 1))
    return max(flow_over_time, key=flow_over_time.get)


def move(graph, start, max_time):
    current = start
    open_valves = set()
    nonzero_valves = set()

    # calculate nonzero valves
    for valve in graph.keys():
        if graph[valve].rate > 0:
            nonzero_valves.add(valve)
    time_remaining = max_time
    countdown = -1
    pressure = 0
    while time_remaining > 0:
        if countdown == -1:
            # find best valve to go to
            distances = dijkstra_find_distance_to_all_nodes(graph, current)
            distances = {k: v for k, v in distances.items()
                         if k not in open_valves}
            next_valve = find_shortest_distance(
                graph, distances, time_remaining)
            countdown = distances[next_valve]
        elif countdown == 0:
            # open valve
            open_valves.add(next_valve)
            current = next_valve
            countdown = -1
        else:
            countdown -= 1

        for valve in open_valves:
            pressure += graph[valve].rate

        time_remaining -= 1

    print(pressure)


if __name__ == "__main__":
    main()
