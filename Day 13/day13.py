class PacketPair:
    def __init__(self, packet_1, packet_2):
        self.packet_1 = packet_1
        self.packet_2 = packet_2

    def is_ordered(self):
        return self.compare(self.packet_1, self.packet_2)

    def compare(self, left, right, level=0):
        print(f"{'  ' * level}- Compare {left} vs {right}")
        if type(left) == int and type(right) == int:
            if left != right:
                if left < right:
                    print(f"{'  ' * (level + 1)}- Left side is smaller, so inputs are in the right order")
                    return True
                else:
                    print(f"{'  ' * (level + 1)}- Right side is smaller, so inputs are not in the right order")
                    return False
                # return left < right
            else:
                return None
        elif type(left) == list and type(right) == list:
            l, r = 0, 0
            while l < len(left) and r < len(right):
                result = self.compare(left[l], right[r], level + 1)
                if result is None:
                    l += 1
                    r += 1
                else:
                    return result
            else:
                if len(left) == len(right):
                    return None
                elif l == len(left):
                    print(f"{'  ' * (level + 1)}- Left side ran out of items, so inputs are in the right order")
                    return True
                elif r == len(right):
                    print(f"{'  ' * (level + 1)}- Right side ran out of items, so inputs are not in the right order")
                    return False
        elif type(left) == int and type(right) == list:
            print(f"{'  ' * level}- Mixed types; convert left to [{left}] and retry comparison")
            return self.compare([left], right, level + 1)
        elif type(left) == list and type(right) == int:
            print(f"{'  ' * level}- Mixed types; convert right to [{right}] and retry comparison")
            return self.compare(left, [right], level + 1)
        else:
            return None

    def __str__(self):
        return f"PacketPair({self.packet_1}, {self.packet_2})"

    def __repr__(self):
        return self.__str__()


def main():
    with open("input", "r") as input_file:
        input = input_file.read().strip()
    print(sum_inorder_packets(read_packets(input)))


def read_packets(input):
    pairs = []
    input_list = input.split("\n\n")
    for input_pair in input_list:
        packet_1, packet_2 = input_pair.split("\n")
        pairs.append(PacketPair(read_packet(packet_1), read_packet(packet_2)))
    return pairs


def read_packet(packet_string):
    stack = []
    for char in packet_string:
        if char == "[":
            stack.append([])
        elif char == "]":
            if len(stack) > 1:
                stack[-2].append(stack.pop())
        elif char == ",":
            pass
        else:
            stack[-1].append(int(char))
    return stack[0]


def sum_inorder_packets(packets):
    sum = 0
    for i in range(len(packets)):
        print(f"\n== Pair {i + 1} ==")
        if packets[i].is_ordered():
            sum += i + 1
    return sum


if __name__ == "__main__":
    main()
