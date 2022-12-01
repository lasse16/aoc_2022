def main():
    max_carry_total, current_total = 0, 0
    with open("01/input.txt", encoding="ascii") as input_file:
        for line in input_file:
            line = line.strip()
            if line == "":
                if current_total > max_carry_total:
                    max_carry_total = current_total
                current_total = 0
            else:
                current_total += int(line)
    print(max_carry_total)
    return max_carry_total


if __name__ == "__main__":
    main()
