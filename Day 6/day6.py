def main():
    with open("input", "r") as input_file:
        datastream = input_file.readline().strip()
    print(find_first_marker(datastream))


def find_first_marker(datastream):
    i = 3
    while i < len(datastream):
        if len(set([datastream[i], datastream[i-1], datastream[i-2], datastream[i-3]])) == 4:
            return i + 1
        i += 1


if __name__ == "__main__":
    main()
