class Monkey:
    def __init__(self, number, operation, test, test_true, test_false, starting_items=[]):
        self.number = number
        self.operation = operation
        self.test = test
        self.test_true = test_true
        self.test_false = test_false
        self.items = starting_items

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


def main():
    with open("input", "r") as input_file:
        input = input_file.read()
    read_monkeys(input)


def read_monkeys(input):
    monkeys = []
    current_info = [0, "", "", 0, 0, []]
    for block in input.split("\n\n"):
        split_data = block.split("\n")
        current_info[0] = int(split_data[0].split(" ")[1][:-1])
        current_info[1] = split_data[2].split(":")[1].strip()
        current_info[2] = int(split_data[3].split(" ")[-1])
        current_info[3] = int(split_data[4].split(" ")[-1])
        current_info[4] = int(split_data[5].split(" ")[-1])
        current_info[5] = [int(item) for item in split_data[1].split(":")[
            1].strip().split(", ")]
        monkeys.append(Monkey(*current_info))
    print(*monkeys, sep="\n\n")
    return monkeys


if __name__ == "__main__":
    main()
