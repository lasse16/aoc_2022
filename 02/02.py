from collections import Counter

scores_by_constellation = {
    "B X": 1,
    "C X": 2,
    "A X": 3,
    "A Y": 4,
    "B Y": 5,
    "C Y": 6,
    "C Z": 7,
    "A Z": 8,
    "B Z": 9,
}


def main():
    with open("02/input.txt", encoding="ascii") as target_file:
        played_constellations = Counter(target_file.read().splitlines())
        score = 0
        for constellation, count in played_constellations.items():
            score += scores_by_constellation[constellation] * count
        print(score)
        return score


if __name__ == "__main__":
    main()
