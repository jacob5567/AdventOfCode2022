class Folder:
    def __init__(self, name, parent):
        self.name = name
        self.parent = parent
        self.subfolders = []
        self.files = []
        self.size = 0


class File:
    def __init__(self, name, size):
        self.name = name
        self.size = size


SMALL_FOLDER_SIZE = 100000
TOTAL_SPACE = 70000000
UNUSED_SPACE_NEEDED = 30000000


def main():
    with open("input", "r") as input_file:
        input_list = input_file.readlines()
    root = init_folder_structure(input_list)
    print(find_small_folder_sum(root))
    deletion_size = space_needed(root)
    print(smallest_folder_deletion(root, deletion_size))


def init_folder_structure(input_list):
    root = Folder("/", None)
    current_folder = root
    for line in input_list:
        if line != "\n":
            line = line.strip().split(" ")
            if line[0] == "$":
                if line[1] == "cd":
                    if line[2] == "/":
                        current_folder = root
                    elif line[2] == "..":
                        current_folder = current_folder.parent
                    else:
                        if line[2] in [f.name for f in current_folder.subfolders]:
                            current_folder = next(
                                f for f in current_folder.subfolders if f.name == line[2])
            elif line[0] == "dir":
                new_folder = Folder(line[1], current_folder)
                current_folder.subfolders.append(new_folder)
            else:
                new_file = File(line[1], int(line[0]))
                current_folder.files.append(new_file)
                folder_size_updater = current_folder
                while folder_size_updater != None:
                    folder_size_updater.size += int(line[0])
                    folder_size_updater = folder_size_updater.parent
    return root


def find_small_folder_sum(folder):
    if folder.size <= SMALL_FOLDER_SIZE:
        return folder.size + sum([find_small_folder_sum(f) for f in folder.subfolders])
    else:
        return sum([find_small_folder_sum(f) for f in folder.subfolders])


def space_needed(root):
    unused_space = TOTAL_SPACE - root.size
    minimum_size_to_be_deleted = UNUSED_SPACE_NEEDED - unused_space
    return minimum_size_to_be_deleted


def smallest_folder_deletion(folder, deletion_size):
    if folder.size >= deletion_size:
        return min(folder.size, min([smallest_folder_deletion(f, deletion_size) for f in folder.subfolders], default=TOTAL_SPACE))
    else:
        return min([smallest_folder_deletion(f, deletion_size) for f in folder.subfolders], default=TOTAL_SPACE)


if __name__ == "__main__":
    main()
