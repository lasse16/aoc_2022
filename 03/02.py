def main():
    with open("03/input.txt", encoding="ascii") as input_file:
        total_priority = 0
        lines = input_file.readlines()
        for index in range(0, len(lines), 3):
            first_line = set(lines[index].strip())
            second_line = set(lines[index + 1].strip())
            third_line = set(lines[index + 2].strip())

            doubled_char = first_line.intersection(second_line).intersection(third_line)
            total_priority += convert_to_priority(doubled_char.pop())
        print(total_priority)
        return total_priority


def convert_to_priority(letter):
    if letter.islower():
        return ord(letter) - 96
    return ord(letter) - 64 + 26


if __name__ == "__main__":
    main()
