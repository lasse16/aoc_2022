import re


def main():
    range_pattern = re.compile(r"(\d+)-(\d+),(\d+)-(\d+)")
    contained_ranges_count = 0
    with open("04/input.txt", encoding="ascii") as input_file:
        for line in input_file:
            range_limits = [int(x) for x in range_pattern.match(line).groups()]
            if not (
                range_limits[1] < range_limits[2] or range_limits[0] > range_limits[3]
            ):
                contained_ranges_count += 1
    print(contained_ranges_count)
    return contained_ranges_count


if __name__ == "__main__":
    main()
