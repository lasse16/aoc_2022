def main():
    with open("03/input.txt", encoding="ascii") as input_file:
        total_priority = 0
        for line in input_file:
            line = line.strip()
            compartment_limit = len(line) // 2
            first_compartment = set(line[compartment_limit:])
            second_compartment = set(line[:compartment_limit])
            doubled_char = first_compartment.intersection(second_compartment)
            total_priority += convert_to_priority(doubled_char.pop())
        print(total_priority)
        return total_priority


def convert_to_priority(letter):
    if letter.islower():
        return ord(letter) - 96
    return ord(letter) - 64 + 26


if __name__ == "__main__":
    main()
