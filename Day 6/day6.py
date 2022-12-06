def main():
    with open("input", "r") as input_file:
        datastream = input_file.readline().strip()
    print(find_first_marker(datastream, 4))
    print(find_first_marker(datastream, 14))


def find_first_marker(datastream, marker_length):
    i = marker_length - 1
    while i < len(datastream):
        if len(set(datastream[i-(marker_length-1):i+1])) == marker_length:
            return i + 1
        i += 1


if __name__ == "__main__":
    main()
