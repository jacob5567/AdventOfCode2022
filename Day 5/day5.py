class BoxStack:
    def __init__(self, input_list):
        box_stack_lines = []
        self.num_columns = 0
        self.instructions = []
        for line in input_list:
            if line.strip() == "":
                continue
            if line.strip()[0] == "[":
                box_stack_lines.append(line)
            elif line.strip()[0] == "1":
                self.num_columns = int(line.strip()[len(line.strip()) - 1])
            elif line.strip()[0] == "m":
                instruction = line.strip().split(" ")
                self.instructions.append((int(instruction[1]), int(
                    instruction[3]), int(instruction[5])))

        stack_input = []
        for line in box_stack_lines:
            stack_input.append([line[i] for i in range(1, len(line), 4)])

        self.stack_array = []
        for i in range(self.num_columns):
            self.stack_array.append([])

        for i in range(len(stack_input)):
            current_row = stack_input.pop()
            for j in range(len(current_row)):
                if current_row[j] != " ":
                    self.add_box(current_row[j], j)

    def add_box(self, box, column):
        self.stack_array[column].append(box)

    def process_instructions(self):
        for instruction in self.instructions:
            self.move_boxes(instruction[0], instruction[1], instruction[2])
    
    def process_instructions_same_order(self):
        for instruction in self.instructions:
            self.move_boxes_same_order(instruction[0], instruction[1], instruction[2])

    def move_boxes(self, num_boxes, from_column, to_column):
        for i in range(num_boxes):
            self.stack_array[to_column - 1].append(
                self.stack_array[from_column - 1].pop())

    def move_boxes_same_order(self, num_boxes, from_column, to_column):
        temp_stack = []
        for i in range(num_boxes):
            temp_stack.append(self.stack_array[from_column - 1].pop())
        for i in range(num_boxes):
            self.stack_array[to_column - 1].append(temp_stack.pop())

    def top_boxes(self):
        top_boxes = []
        for column in self.stack_array:
            top_boxes.append(column[-1])
        return "".join(top_boxes)


def main():
    with open("input", "r") as input_file:
        input_list = input_file.readlines()
    box_stack = BoxStack(input_list)
    box_stack.process_instructions()
    print(box_stack.top_boxes())
    box_stack = BoxStack(input_list)
    box_stack.process_instructions_same_order()
    print(box_stack.top_boxes())


if __name__ == "__main__":
    main()
