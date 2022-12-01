def main():
    totals = [0, 0, 0]
    current_total = 0
    min_total = 0
    min_total_index = 0
    with open("01/input.txt", encoding="ascii") as input_file:
        for line in input_file:
            line = line.strip()
            if line == "":
                if current_total > min_total:
                    totals[min_total_index] = current_total
                    min_total = min(totals)
                    min_total_index = totals.index(min_total)
                current_total = 0
            else:
                current_total += int(line)
    sum_totals = sum(totals)
    print(sum_totals)
    return sum_totals


if __name__ == "__main__":
    main()
