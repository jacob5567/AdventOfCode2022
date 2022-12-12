class Monkey:
    def __init__(self, number, operation, test, test_true, test_false, starting_items=[]):
        self.number = number
        self.operation = operation
        self.test = test
        self.test_true = test_true
        self.test_false = test_false
        self.items = starting_items

    def do_operation(self, item):
        old = item
        return eval(self.operation)

    def __str__(self):
        return (
            f"Monkey {self.number}:\n"
            f"  Starting items: {', '.join(map(str, self.items))}\n"
            f"  Operation: {self.operation}\n"
            f"  Test: divisible by {self.test}\n"
            f"    If true: throw to monkey {self.test_true}\n"
            f"    If false: throw to monkey {self.test_false}"
        )

    def __repr__(self):
        return self.__str__()

    def print_items(self):
        print(f"Monkey {self.number}: {', '.join(map(str, self.items))}")


def main():
    with open("input", "r") as input_file:
        input = input_file.read()
    monkey_list = read_monkeys(input)
    print(monkey_business(monkey_list, 20, True))
    monkey_list = read_monkeys(input)
    print(monkey_business(monkey_list, 10000, False))


def read_monkeys(input):
    monkeys = []
    current_info = [0, "", "", 0, 0, []]
    for block in input.split("\n\n"):
        split_data = block.split("\n")
        current_info[0] = int(split_data[0].split(" ")[1][:-1])
        current_info[1] = split_data[2].split(
            ":")[1].strip().split("=")[1].strip()
        current_info[2] = int(split_data[3].split(" ")[-1])
        current_info[3] = int(split_data[4].split(" ")[-1])
        current_info[4] = int(split_data[5].split(" ")[-1])
        current_info[5] = [int(item) for item in split_data[1].split(":")[
            1].strip().split(", ")]
        monkeys.append(Monkey(*current_info))
    return monkeys


def monkey_business(monkeys, num_rounds, do_divide):
    activity_map = {}
    divide_num = 1
    for monkey in monkeys:
        divide_num *= monkey.test
    monkeys = sorted(monkeys, key=lambda monkey: monkey.number)
    for i in range(num_rounds):
        for monkey in monkeys:
            for j in range(len(monkey.items)):
                # inspect item
                if monkey.number not in activity_map:
                    activity_map[monkey.number] = 0
                activity_map[monkey.number] += 1
                item = monkey.items.pop(0)
                # execture operation
                item = monkey.do_operation(item)
                # monkey gets bored
                if do_divide:
                    item = item // 3
                else:
                    item = item % divide_num
                # throw item
                monkeys[monkey.test_true if item % monkey.test ==
                        0 else monkey.test_false].items.append(item)
    top_two = sorted(activity_map.values())[-2:]
    return top_two[0] * top_two[1]


if __name__ == "__main__":
    main()
